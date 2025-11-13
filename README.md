# SpicyPy Tutorial Project

## The Team



**Alex Stilson** <br>
<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="Alex Stilson"> <br>
* * <br>

**Kathle Tischner** <br>
<img src="{{ '/Pics/Kathle_Profile.png' | relative_url }}" 
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
