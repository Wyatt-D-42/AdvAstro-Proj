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
        # KERNELS_TO_LOAD=(
        # 'naif0012.tls',                 Provides leap seconds
        # 'pck00011.tpc',                 Provides planetary constants
        # 'de440.bsp',                    Provides planetary ephemerides
        # 'jwst_pred.bsp',                Provides JWST ephemeris
        # 'earth_latest_high_prec.bpc',   Provides Earth orientation
        # 'earthstns_itrf93_201023.bsp',  Provides DSN station positions
        # 'DSN_topo.tf'                   Provides DSN station frames
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
    JWST_ID = '-170'
    SUN_EARTH_BARYCENTER_ID = '3'
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
        
        # Check each station for this time step
        for station_name, (station_frame, station_id) in DSN_STATIONS.items():
            try:
                # Get JWST state relative to the DSN station
                state, lt = spice.spkezr( # Returns state vector and light time
                    targ=JWST_ID,
                    et=t,
                    ref=station_frame,
                    abcorr='LT+S',
                    obs=station_id
                )
                
                vec_topo = state[:3] # state = [x, y, z, vx, vy, vz] in station topocentric frame
                rng, lon, lat = spice.recrad(vec_topo) # Convert to spherical coords
                elevation = lat # lat = asin(z/r) lon = atan2(y, x)    z is up in topocentric frame

                if elevation > MIN_ELEVATION_RAD: # If the elevation is above minimum, or horizon
                    # Add to timeline data
                    visibility_data[station_name].append(times_utc[i]) 
                    
                    # Set flag for 3D plot
                    # Use the *first* station that sees it for the color
                    if not is_visible_at_this_time:
                        visibility_flags[i] = station_colors[station_name]
                        is_visible_at_this_time = True
                        
            except Exception as e:
                # uncomment the line below for detailed debugging
                # print(f"Error for {station_name} at {spice.et2utc(t, 'C', 0)}: {e}")
                pass
                
    spice.kclear()
    
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
            
        ax.vlines(visible_times, i - 0.4, i + 0.4, color=colors[station], lw=2, label=station)

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
    else:
        print("\nAnalysis failed. Please check kernel files and error messages.")