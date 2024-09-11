#Jared Johnstun
#Date: 9/9/2024

import numpy as np
import matplotlib.pyplot as plt

#define initial condition variables:
x0 = 0 #initial x position
y0 = 0 #initial y position
v0 = 20 #initial velocity
θ0 = 45 #inital angle of velocity relative to horizonal (in degrees) needs to be greater than zero
g = -9.8 #acceleration due to gravity (m/s^2)

#define functions for x position, y position, and range of projectile
def x(t,θ):
    #convert θ from degrees to radians
    np.deg2rad(θ)
    x = x0 + (v0*t*np.cos(θ))
    return x

def y(t,θ):
    #convert θ from degrees to radians
    np.deg2rad(θ)
    y = y0 + (v0*t*np.sin(θ)) - (0.5*g*t**2)
    return y

def Range(θ):
    R = ((v0**2)/g)*np.sin(2*θ)
    return R

#Create function to generate values of t for the given information:
def t_range():
    t=0,
    counter = 0
    while y(t,θ0) >0 :
        t +=0.2
        counter +=1
        return np.linspace(0, t, counter)
    
#Create First Plot
θ_range = np.linspace(30, 60, 8)

for θ in θ_range:
    #generate range of t values
    t_in = t_range()
    #plug them into functions to get 
    


