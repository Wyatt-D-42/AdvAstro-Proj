# SpicyPy Tutorial Project

## The Team



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

For this project, we elected to make some tutorials using SpicyPy as there are few tutorials available for this program and it is a widely used program that we may encounter in our careers as Engineers in the Space Sector. <br>

To start we thought of a few useful scenarios that show unique orbits or traits to implement in SpicyPy and then provide a tutorial on how to implement these scenarios. The first scenario we chose is to show the James Webb Space Telescope (JWST) in its orbit centered at L1 and in a ECI frame. We also made and plotted access times for the JWST with the NASA Deep Space Network antennas. Another scenario we implemented was a spacecraft in the Near Rectilinear Halo Orbit (NRHO) around the moon as that is a orbit that will be highly used in upcoming lunar missions with the Artemis Program.

# James Webb Space Telescope 


```

clear all; close all; clc
% example code to test github
A = [0,1;-1,-2];
B = [0;1];
C = [1,0];

State_space = ss(A,B,C,[]);
G = tf(State_space);

OS = 6;
damp = -log(OS/100)/ sqrt(pi^2+(log(OS/100))^2);
T_s = 6;
damp_min = 4/T_s;

```

## Project Readmes

- [JWST Visibility README](Project_Files/JWST_Visibility/readme.md) — Documentation and usage notes for the JWST visibility tutorial (SpiceyPy kernels, meta-kernel, and run instructions).

