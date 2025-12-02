## SpicyPy Tutorial Project

# The Team
**Alex Stilson** <br>
**Kathle Tischner** <br>
**Sydney Perkins** <br>
**Wyatt Daugs** <br>

<!--
<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="Alex Stilson"> <br>
* * <br>

<img src="{{ '/Pics/Kathle_Profile.jpg' | relative_url }}" 
     width="100" 
     alt="kathle Tishner"> <br>
* * <br>

<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="Sydney Perkins"> <br>
* * <br>

<img src="{{ '/Pics/Wyatt_Profile.jpg' | relative_url }}" 
     width="100" 
     alt="Wyatt Daugs"> <br>
*Wyatt is pursuing a Master's Degree in Space Systems Engineering. He likes to read and build Hobby Rockets.* <br>
-->
* * * * * * * * * * * *
 <br>

# The Project

For this project, we elected to make some tutorials using SpicyPy, as there are few tutorials available for this program, and it is a widely used program that we may encounter in our careers as engineers in the Space Sector. <br>

To start, we considered a few useful scenarios that showcase unique orbits or traits to implement in SpicyPy, and then provided a tutorial on how to implement these scenarios. The first scenario we chose is to show the James Webb Space Telescope (JWST) in its orbit centered at L1 and in an ECI frame. We also made and plotted access times for the JWST with the NASA Deep Space Network antennas. Another scenario we implemented was a spacecraft in the Near Rectilinear Halo Orbit (NRHO) around the moon, as that is an orbit that will be highly utillized in upcoming lunar missions with the Artemis Program.

# A brief aside about SPICE
Spacecraft, Planet, Instrument, C-matrix, Events (SPICE) is a program developed by NASA to plan space missions and model results from such missions. SPICE uses data sets known as kernels which contain navigation and ancillary information to provide precise information about various mission components. The most common kernels contain ephemeris data for spacecraft and celestial bodies, data about instruments like view angle and orientations, orientation matrices, and event data. 
Originally implemented in FORTRAN, the SPICE toolkit now works with most common coding languages, including Python. The SPICE Toolkit that has been implemented for use in Python is known as SPICYPy. For more information about SPICE, visit the [SPICE HOMEPAGE](https://naif.jpl.nasa.gov/naif/aboutspice.html)

# James Webb Space Telescope
We started out with the James Webb Space Telescope (JWST). We used existing kernels to plot the orbit of the JWST. 

The following figure shows the orbit of the JWST around the L2 Lagrange point of the Earth-Sun system over a 6-month period.

<img src="{{ '/Project_Files/JWST_Visibility/jwst_orbit_3d.jpg' | relative_url }}" 
     width="600" 
     alt="JWST Orbit"> <br>

The next task we performed was to determine the contact times of the JWST with the Deep Space Network (DSN) ground stations. Using existing kernels for the DSN, we then implemented an algorithm that detected anytime the angle between a DSN ground station and the JWST was greater than 0 degrees (representing above the horizon). If this condition was met, then the two entities could communicate. The following plots were generated from this process. 

The following plot shows the sky track of the JWST over the 3 primary DSN sites: Goldstone, Madrid, and Canberra, over a 6-month period.

<img src="{{ '/Project_Files/JWST_Visibility/jwst_sky_tracks.jpg' | relative_url }}" 
     width="600" 
     alt="JWST Sky Tracks"> <br>
     
The following plot shows the contact times between the JWST and the 3 DSN sites over a 6-month period.

<img src="{{ '/Project_Files/JWST_Visibility/jwst_visibility_timeline.jpg' | relative_url }}" 
     width="600" 
     alt="JWST Visibility"> <br>

The code and files used for this can be found in our GitHub repository here
[JWST Files](https://github.com/Wyatt-D-42/AdvAstro-Proj/tree/6440cc315f37cd719c8b994e55e6b4078ef94e86/Project_Files/JWST_Visibility)

Instructions on how to set up the files to correctly reference the kernels, including a video tutorial, can be found here
[JWST Visibility README](Project_Files/JWST_Visibility/readme.md) — Documentation and usage notes for the JWST visibility tutorial (SpiceyPy kernels, meta-kernel, and run instructions).




# Lunar Gateway Halo Orbit
With the Gateway Orbit, which is the orbit NASA plans to use for the Lunar Gateway Space Station to support the Artemis Program, we wanted to show this orbit from different reference frames to showcase this function of SPICE. The Gateway Orbit is a Near Rectilinear Halo Orbit (NRHO) around the L2 Lagrange Point of the Earth-Moon system. Using existing spice kernels, we plotted the orbit of a spacecraft in the Gateway Orbit in a Moon Centered Inertial (MCI) Frame, the Earth Centered Inertial (ECI) Frame, and the Sun Centered Inertial (SCI) Frame.

The following figure shows the Gateway Orbit in the MCI frame. 

<img src="{{ '/Project_Files/Gateway_Orbit/Gateway_Orbit.jpeg' | relative_url }}" 
     width="600" 
     alt="JWST Visibility"> <br>

The following figure shows the Gateway Orbit in the ECI frame. 

<img src="{{ '/Project_Files/Gateway_Orbit/Gateway_Orbit_ECI.jpeg' | relative_url }}" 
     width="600" 
     alt="JWST Visibility"> <br>
     
The following figure shows the Gateway Orbit in the SCI frame. 

<img src="{{ '/Project_Files/Gateway_Orbit/Gateway_Orbit_SCI.jpeg' | relative_url }}" 
     width="600" 
     alt="JWST Visibility"> <br>

The code and files used for this can be found in our GitHub repository here
[GATEWAY Files](https://github.com/Wyatt-D-42/AdvAstro-Proj/tree/3be3e2f25cbae3d3b29f5d6f7396c576ec30e545/Project_Files/Gateway_Orbit)

Instructions on how to set up the files to correctly reference the kernels can be found here
[GATEWAY README](Project_Files/Gateway_Orbit/readme.md) — Documentation and usage notes for the Gateway Orbit (SpiceyPy kernels, meta-kernel, and run instructions).


# Challenges We Faced
The biggest challenge we faced was finding the existing spice kernels to use in our code. NASA has created many different kernels for many missions, but it can be difficult to find where they are published. Many of them are posted on NASA's SPICE homepage, but not all of them. Often, the needed kernels are found on an old webpage that hasn't been updated since the related mission or in archives that are not kept up to date. This made finding some of the kernels needed for this project somewhat difficult.

Another difficulty we faced was just figuring out all the functions of SPICE. There is not very much recent documentation on SPICE, and especially not very much for SpicyPy, which is one of the reasons we decided to do this project. So it was sometimes a challenge to find the correct functions that we needed to complete this project and learn how they worked to implement them correctly.
