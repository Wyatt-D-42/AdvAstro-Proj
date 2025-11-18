import spiceypy as spice
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch

def calculate_visibility(utc_start, utc_end, steps):
    """
    Calculates JWST orbit, DSN visibility windows, and visibility flags for plotting.
    """
    
    # --- Step 1: Setup and Load Kernels ---
    try:
        spice.furnsh('jwst_meta.txt')
        # The jwst_meta.txt file should list all required SPICE kernels, listed below:
        # KERNELS_TO_LOAD=(
        # 'naif0012.tls',                 Provides leap seconds              'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls',       
        # 'pck00010.tpc',                 Provides planetary constants       'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc',
        # 'de440.bsp',                    Provides planetary ephemerides     'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp'
        # 'jwst_pred.bsp',                Provides JWST ephemeris            'https://naif.jpl.nasa.gov/pub/naif/JWST/kernels/spk/jwst_pred.bsp'
        # 'earth_latest_high_prec.bpc',   Provides Earth orientation         'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/'
        # 'earthstns_itrf93_201023.bsp',  Provides DSN station positions     'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/stations/'
        # 'DSN_topo.tf'                   Provides DSN station frames        'https://naif.jpl.nasa.gov/pub/naif/FIDO/kernels/fk/DSN_topo.tf'
        # )
    except Exception as e:
        print(f"Error loading kernels: {e}")
        print("Please ensure jwst_meta.txt and all kernel files (.bsp, .tf, .tls) are in the same directory.")
        return None, None, None, None

    # --- Step 2: Define Time Window and Targets ---
    et_start = spice.str2et(utc_start)
    et_end = spice.str2et(utc_end)
    
    times_et = np.linspace(et_start, et_end, steps)
    times_utc = [spice.et2datetime(t) for t in times_et]

    # Define NAIF IDs from https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/naif_ids.html
    # JWST_ID = '-170'
    try:
        JWST_ID = str(spice.bodn2c('JWST')) # JWST NAIF ID using bodn2c which maps names to IDs
    except:
        print("ID not found in loaded kernels for 'JWST'. defaulting to -170.")
        JWST_ID = '-170'
    # SUN_EARTH_BARYCENTER_ID = '3'
    try:
        SUN_EARTH_BARYCENTER_ID = str(spice.bodn2c('SUN_EARTH_BARYCENTER'))
    except:
        print("ID not found in loaded kernels for 'SUN_EARTH_BARYCENTER'. defaulting to 3.")
        SUN_EARTH_BARYCENTER_ID = '3'
    # EARTH_ID = '399'
    try:
        EARTH_ID = str(spice.bodn2c('EARTH'))
    except:
        print("ID not found in loaded kernels for 'EARTH'. defaulting to 399.")
        EARTH_ID = '399'

    DSN_STATIONS = {
        'Goldstone': ('DSS-14_TOPO', '399014'), 
        'Madrid':    ('DSS-63_TOPO', '399063'), 
        'Canberra':  ('DSS-43_TOPO', '399043')  
    }
    
    MIN_ELEVATION_DEG = 0.0
    MIN_ELEVATION_RAD = np.deg2rad(MIN_ELEVATION_DEG)

    # --- Step 3: Calculate JWST Position for 3D Orbit Plot ---
    try:
        positions, _ = spice.spkpos( # Returns position and light time from target to observer
            targ=JWST_ID,
            et=times_et,
            ref='J2000',
            abcorr='NONE',
            obs=SUN_EARTH_BARYCENTER_ID
        )
        positions_T = positions.T
    except Exception as e:
        print(f"Error calculating JWST orbit position: {e}")
        spice.kclear()
        return None, None, None, None

    # --- Step 4: Calculate DSN Visibility Windows ---
    
    visibility_data = {station: [] for station in DSN_STATIONS} # List of visible times per station
    visibility_flags = np.zeros(steps, dtype=int) # 0 = Not visible
    station_colors = {'Goldstone': 1, 'Madrid': 2, 'Canberra': 3} # For 3D plot
    
    print(f"Calculating visibility for {steps} time steps...")

    for i, t in enumerate(times_et):
        is_visible_at_this_time = False
        
        for station_name, (station_frame, station_id) in DSN_STATIONS.items():
            try:
                # TEACHING NOTE: spkezr calculates the state (position + velocity) 
                # of a target (JWST) relative to an observer (DSN Station)
                # 'LT+S' corrects for Light Time and Stellar Aberration
                state, lt = spice.spkezr(
                    targ=JWST_ID,
                    et=t,
                    ref=station_frame, # Topocentric frame (Z is up, X is North)
                    abcorr='LT+S',
                    obs=station_id
                )
                
                # Extract position (x, y, z) from state vector
                position_topo = state[:3] 
                
                # Convert rectangular coordinates (x, y, z) to range, azimuth, elevation
                r, az_rad, el_rad = spice.recrad(position_topo) 
                
                # SPICE returns azimuth in radians (0 to 2pi). 
                # SPICE 'lat' is elevation (-pi/2 to pi/2).
                
                if el_rad > MIN_ELEVATION_RAD:
                    # Store data for Sky Plot: (Time, Azimuth in Deg, Elevation in Deg)
                    # Note: We convert to degrees here for easier plotting later
                    visibility_data[station_name].append(
                        (times_utc[i], np.rad2deg(az_rad), np.rad2deg(el_rad))
                    )
                    
                    if not is_visible_at_this_time:
                        visibility_flags[i] = station_colors[station_name]
                        is_visible_at_this_time = True
                        
            except Exception as e:
                # uncomment the line below for detailed debugging
                # print(f"Error for {station_name} at {spice.et2utc(t, 'C', 0)}: {e}")
                pass
                
    
    print("Calculation complete.")
    return positions_T, visibility_data, times_utc, visibility_flags

def plot_orbit_3d(positions_T, visibility_flags):
    """
    Generates a 3D plot of the JWST halo orbit, color-coded by DSN visibility.
    """
    if positions_T is None:
        return

    print("Generating 3D orbit plot...")
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    colors_map = {
        0: 'grey', 
        1: '#E69F00', # Goldstone (Orange)
        2: '#56B4E9', # Madrid (Blue)
        3: '#009E73'  # Canberra (Green)
    }
    labels_map = {
        0: 'Not Visible', 
        1: 'Visible (Goldstone)', 
        2: 'Visible (Madrid)', 
        3: 'Visible (Canberra)'
    }
    
    # Map flags to colors for plotting
    plot_colors = [colors_map.get(flag, 'red') for flag in visibility_flags]

    ax.scatter(positions_T[0], positions_T[1], positions_T[2], c=plot_colors, s=2)
    
    ax.scatter([0], [0], [0], color='red', s=100, label=None)

    ax.set_title('JWST Halo Orbit (Relative to Sun-Earth Barycenter)', fontsize=16)
    ax.set_xlabel('X (km)', fontsize=12)
    ax.set_ylabel('Y (km)', fontsize=12)
    ax.set_zlabel('Z (km)', fontsize=12)
    
    max_range = np.max(np.abs(positions_T))
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    
    # --- Create custom legend ---
    legend_elements = [
        Patch(facecolor=colors_map[0], label=labels_map[0]),
        Patch(facecolor=colors_map[1], label=labels_map[1]),
        Patch(facecolor=colors_map[2], label=labels_map[2]),
        Patch(facecolor=colors_map[3], label=labels_map[3]),
        plt.Line2D([0], [0], marker='o', color='w', label='Sun-Earth Barycenter',
                   markerfacecolor='red', markersize=10) # For the barycenter
    ]
    ax.legend(handles=legend_elements)
    
    plt.tight_layout()
    plt.show()

def plot_visibility_timeline(visibility_data, all_times_utc):
    """
    Generates a 2D timeline (Gantt-style) plot of DSN visibility.
    (This function remains unchanged)
    """
    if visibility_data is None:
        return

    print("Generating 2D visibility timeline plot...")
    fig, ax = plt.subplots(figsize=(15, 6))
    
    station_names = list(visibility_data.keys())
    colors = {'Goldstone': '#E69F00', 'Madrid': '#56B4E9', 'Canberra': '#009E73'}

    for i, station in enumerate(station_names):
        visible_times = visibility_data[station]
        if not visible_times:
            print(f"No visible times found for {station}.")
            continue
            
        # ax.vlines(visible_times, i - 0.4, i + 0.4, color=colors[station], lw=2, label=station)
        visible_times_only = [x[0] for x in visible_times]
        ax.vlines(visible_times_only, i - 0.4, i + 0.4, color=colors[station], lw=2, label=station)

    ax.set_yticks(range(len(station_names)))
    ax.set_yticklabels(station_names, fontsize=12)
    ax.set_ylim(-0.5, len(station_names) - 0.5)

    ax.set_xlabel('Date (UTC)', fontsize=12)
    ax.set_xlim(all_times_utc[0], all_times_utc[-1])
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=6, maxticks=10))
    fig.autofmt_xdate()

    ax.set_title('JWST Visibility from DSN Stations (Elevation > 0°)', fontsize=16)
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    
    handles = [plt.Rectangle((0,0),1,1, color=colors[station]) for station in station_names]
    ax.legend(handles, station_names, loc='upper right')
    
    plt.tight_layout()
    plt.show()

def plot_sky_tracks(visibility_data):
    """
    Generates sky plot for each DSN station.
    """
    if visibility_data is None:
        return

    print("Generating sky track plots...")
    
    station_names = list(visibility_data.keys())
    colors = {'Goldstone': '#E69F00', 'Madrid': '#56B4E9', 'Canberra': '#009E73'}
    
    fig, axes = plt.subplots(
        1, len(station_names), 
        figsize=(18, 6), 
        subplot_kw={'projection': 'polar'}
    )
    
    if len(station_names) == 1:
        axes = [axes] 

    for ax, station in zip(axes, station_names):
        visible_times_data = visibility_data[station]
        
        if not visible_times_data:
            ax.set_title(f"{station} (No Visibility)")
            continue
            
        azimuths_rad = np.deg2rad([item[1] for item in visible_times_data])
        elevations_deg = [item[2] for item in visible_times_data]
        co_elevations = 90 - np.array(elevations_deg)
        
        ax.scatter(azimuths_rad, co_elevations, c=colors[station], s=2, label=station)
        
        ax.set_title(f"JWST Sky Track from {station}", pad=20)
        ax.set_theta_zero_location('N') 
        ax.set_theta_direction(-1) 
        
        ax.set_yticks([0, 30, 60, 90]) 
        ax.set_yticklabels(['90°', '60°', '30°', '0°'])
        ax.set_ylim(0, 90) 

    plt.tight_layout()
    plt.savefig("jwst_sky_tracks.png") # Save the plot
    plt.close() # Close the figure to save memory

def calculate_rotating_frame_data(utc_start, utc_end, steps):
    """
    Calculates JWST position in a Sun-Earth Rotating Frame (RLP).
    This removes the Earth's orbital motion to reveal the 'Halo' shape.
    """
    print("Calculating Rotating Frame transformation (Sun-Earth L2)...")
    
    et_start = spice.str2et(utc_start)
    et_end = spice.str2et(utc_end)
    times = np.linspace(et_start, et_end, steps)
    
    # Pre-calculate IDs to save time in the loop
    try:
        jwst_id = str(spice.bodn2c('JWST'))
        earth_id = str(spice.bodn2c('EARTH'))
        sun_id = str(spice.bodn2c('SUN'))
    except:
        print("Error: IDs not found. Ensure kernels are loaded.")
        return None

    xs, ys, zs = [], [], []

    for t in times:
        try:
            # 1. Get JWST position relative to EARTH (Observer)
            # We use Earth as the center of this rotating frame
            pos_jwst_earth, _ = spice.spkpos(jwst_id, t, 'J2000', 'NONE', earth_id) # Target, ET, Ref Frame, Aberration Correction, Observer

            # 2. Get Earth state relative to SUN to define the rotation
            # We need velocity to find the orbital plane normal
            state_earth_sun, _ = spice.spkezr(earth_id, t, 'J2000', 'NONE', sun_id) # Target, ET, Ref Frame, Aberration Correction, Observer
            pos_earth_sun = state_earth_sun[:3]
            vel_earth_sun = state_earth_sun[3:]

            # 3. Define the Rotating Frame Axes
            # Axis X: Points from Sun to Earth
            vec_x = pos_earth_sun
            # Axis Z: Orbital Plane Normal (Cross product of Position and Velocity)
            vec_z = spice.vcrss(pos_earth_sun, vel_earth_sun)

            # 4. Create Rotation Matrix 
            # spice.twovec creates a transformation matrix based on two vectors. This transforms from J2000 to Rotating Frame
            # Arg 2=1 means 'vec_x' defines the X-axis (1)
            # Arg 4=3 means 'vec_z' defines the Z-axis (3)
            transform_matrix = spice.twovec(vec_x, 1, vec_z, 3)

            # 5. Apply Rotation
            # Multiply matrix by the J2000 position vector
            pos_rotated = spice.mxv(transform_matrix, pos_jwst_earth)

            xs.append(pos_rotated[0])
            ys.append(pos_rotated[1])
            zs.append(pos_rotated[2])
            
        except Exception as e:
            continue

    return np.array(xs), np.array(ys), np.array(zs)

def plot_rotating_frame(x, y, z, visibility_flags):
    """
    Plots the trajectory in the Rotating Frame with DSN Visibility colors.
    """
    if x is None: return

    print("Generating Rotating Frame plot...")
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # --- Color Mapping Strategy ---
    colors_map = {
        0: 'grey', 
        1: '#E69F00', # Goldstone (Orange)
        2: '#56B4E9', # Madrid (Blue)
        3: '#009E73'  # Canberra (Green)
    }
    labels_map = {
        0: 'Not Visible', 
        1: 'Visible (Goldstone)', 
        2: 'Visible (Madrid)', 
        3: 'Visible (Canberra)'
    }
    
    # Convert the integer flags (0,1,2,3) into a list of hex color strings
    plot_colors = [colors_map.get(flag, 'grey') for flag in visibility_flags]

    # Plot the Trajectory
    # Note: We removed 'cmap' and 'label' and used 'c=plot_colors'
    ax.scatter(x, y, z, c=plot_colors, s=2)
    
    # Plot Reference Points
    ax.scatter([0], [0], [0], color='blue', s=200, label='Earth')
    ax.scatter([1.5e6], [0], [0], color='red', marker='x', s=100, label='Approx. L2 Point')

    # Labels and Titles
    ax.set_title('JWST in Sun-Earth Rotating Frame\nColor-coded by DSN Visibility', fontsize=14)
    ax.set_xlabel('X (km) [Sun -> Earth Axis]')
    ax.set_ylabel('Y (km) [Tangential]')
    ax.set_zlabel('Z (km) [Vertical]')

    # Set View
    ax.view_init(elev=20, azim=-120)
    
    # Set Limits
    max_range = 2.0e6 
    ax.set_xlim(0, max_range)
    ax.set_ylim(-max_range/2, max_range/2)
    ax.set_zlim(-max_range/2, max_range/2)

    # --- Create Custom Legend ---
    # We manually create legend handles because the scatter plot uses a list of colors
    legend_elements = [
        Patch(facecolor=colors_map[0], label=labels_map[0]),
        Patch(facecolor=colors_map[1], label=labels_map[1]),
        Patch(facecolor=colors_map[2], label=labels_map[2]),
        Patch(facecolor=colors_map[3], label=labels_map[3]),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Earth'),
        plt.Line2D([0], [0], marker='x', color='red', linestyle='None', markersize=10, label='L2 Point')
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    plt.tight_layout()
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    
    UTC_START = '2025-06-01'
    UTC_END = '2025-12-31'
    TIME_STEPS = 10000 # <-- Increase steps for a denser 3D plot
    
    positions_3d, visibility_windows, all_utc_times, visibility_flags = calculate_visibility(UTC_START, UTC_END, TIME_STEPS)
    
    if positions_3d is not None and visibility_windows is not None:

        # Generate 3D plot from the calculated data
        plot_orbit_3d(positions_3d, visibility_flags)
        
        # Generate timeline plot from the same data
        plot_visibility_timeline(visibility_windows, all_utc_times)

        # Generate sky track plots
        plot_sky_tracks(visibility_windows)

        rot_x, rot_y, rot_z = calculate_rotating_frame_data(UTC_START, UTC_END, TIME_STEPS)
        plot_rotating_frame(rot_x, rot_y, rot_z, visibility_flags)

        # Clear loaded SPICE kernels now that all SPICE-based work is complete
        spice.kclear()
    else:
        print("\nAnalysis failed. Please check kernel files and error messages.")