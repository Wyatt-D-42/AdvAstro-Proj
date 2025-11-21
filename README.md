## SpicyPy Tutorial Project

# The Team



**Alex Stilson** <br>
<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="Alex Stilson"> <br>
* * <br>

**Kathle Tischner** <br>
<img src="{{ '/Pics/Kathle_Profile.jpg' | relative_url }}" 
     width="100" 
     alt="kathle Tishner"> <br>
* * <br>

**Sidney Perkins** <br>
<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="Sydney Perkins"> <br>
* * <br>

**Wyatt Daugs** <br>
<img src="{{ '/Pics/Wyatt_Profile.jpg' | relative_url }}" 
     width="100" 
     alt="Wyatt Daugs"> <br>
*Wyatt is pursuing a Master's Degree in Space Systems Engineering. He likes to read and build Hobby Rockets.* <br>



* * * * * * * * * * * *
 <br>

# The Project

For this project, we elected to make some tutorials using SpicyPy, as there are few tutorials available for this program, and it is a widely used program that we may encounter in our careers as engineers in the Space Sector. <br>

To start we thought of a few useful scenarios that show unique orbits or traits to implement in SpicyPy and then provide a tutorial on how to implement these scenarios. The first scenario we chose is to show the James Webb Space Telescope (JWST) in its orbit centered at L1 and in a ECI frame. We also made and plotted access times for the JWST with the NASA Deep Space Network antennas. Another scenario we implemented was a spacecraft in the Near Rectilinear Halo Orbit (NRHO) around the moon as that is a orbit that will be highly used in upcoming lunar missions with the Artemis Program.

# A breif aside about SPICE
Spacecraft, Planet, Instrument, C-matrix, Events (SPICE) is a program developed by NASA to plan space missions and model results from such missions. SPICE uses data sets known as kernels which contain navigation and ancillary information to privde precise information about various mission components. The most common kernals contain ephemeris data for spacecraft and celestial bodies, data about instrumnets like view andle and orientations, orientation matrices, and event data. 
Originally implemented in FORTRAN, the SPICE toolkit now works with most commmon coding languages, including Python. The SPICE Toolkit that has been implemented for use in Python is known as SPICYPy. For more information about SPICE visit https://naif.jpl.nasa.gov/naif/aboutspice.html

# James Webb Space Telescope
We started out with the James Webb Space Telescope (JWST). We used existing kernels to plot the orbit of the JWST  
<img src="{{ '/Project_Files/JWST_Visibility/jwst_orbit_3d.jpg' | relative_url }}" 
     width="500" 
     alt="JWST Orbit"> <br>


<img src="{{ '/Project_Files/JWST_Visibility/jwst_sky_tracks.jpg' | relative_url }}" 
     width="500" 
     alt="JWST Sky Tracks"> <br>

<img src="{{ '/Project_Files/JWST_Visibility/jwst_visibility_timeline.jpg' | relative_url }}" 
     width="500" 
     alt="JWST Visibility"> <br>

# Lunar Gateway Halo Orbit
<img src="{{ '/Project_Files/Gateway_Orbit/Gateway_Orbit.jpeg' | relative_url }}" 
     width="500" 
     alt="JWST Visibility"> <br>

<img src="{{ '/Project_Files/Gateway_Orbit/Gateway_Orbit_ECI.jpeg' | relative_url }}" 
     width="500" 
     alt="JWST Visibility"> <br>

<img src="{{ '/Project_Files/Gateway_Orbit/Gateway_Orbit_SCI.jpeg' | relative_url }}" 
     width="500" 
     alt="JWST Visibility"> <br>


## Project Readmes

- [JWST Visibility README](Project_Files/JWST_Visibility/readme.md) — Documentation and usage notes for the JWST visibility tutorial (SpiceyPy kernels, meta-kernel, and run instructions).

