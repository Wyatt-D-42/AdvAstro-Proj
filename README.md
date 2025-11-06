# SpicyPy Tutorial Project

## The Team



**Alex Stilson** <br>
<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="Alex Stilson"> <br>
* * <br>

**Kathle Tischner** <br>
<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="kathle Tishner"> <br>
* * <br>

**Sidney Perkins** <br>
<img src="{{ '/Pics/InsertImageHere.jpg' | relative_url }}" 
     width="200" 
     alt="Sydney Perkins"> <br>
* * <br>






'''

clear all; close all; clc

A = [0,1;-1,-2];
B = [0;1];
C = [1,0];

State_space = ss(A,B,C,[]);
G = tf(State_space);

OS = 6;
damp = -log(OS/100)/ sqrt(pi^2+(log(OS/100))^2);
T_s = 6;
damp_min = 4/T_s;


figure;
rlocus(G);
sgrid(damp,[])
Ax = [-5,2,-5,5];
axis(Ax)
xline(-damp_min,'-.',{damp_min})

%from locus choose
K = 1.25;

TF_CL = feedback(series(K,G),1);

%choose a z_lag, this was adjusted unitl requirements were met
z_lag = .65;

K_Gc = zpk(-z_lag,0,K);

TF_PI = feedback(series(K_Gc,G),1);

figure
step(TF_CL,TF_PI,20) 
info = stepinfo(TF_PI);
Overshoot = info.Overshoot
SettleTime = info.SettlingTime
title('Unit Step Response')
legend('P Controller', 'PI Controller')

'''

**Wyatt Daugs** <br>
<img src="{{ '/Pics/Wyatt_Profile.jpg' | relative_url }}" 
     width="100" 
     alt="Wyatt Daugs"> <br>
*Wyatt is pursuing a Master's Degree in Space Systems Engineering. He likes to read and build Hobby Rockets.* <br>
