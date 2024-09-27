#Jared Johnstun
#Date: 9/18/2024

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

'''
End Goal:
Ask user for y0 in meters
get a list of th0's in degrees from cmd line
read list of v0's from first line of txt file, comma separated

'''


x0 = 0
y0 = float(input("Please Enter the Initial Height of the Trajectory in meters: "))
th00 = float(input("Enter initial angle in degrees: "))
v0 = float(input("Enter initial velocity m/s: "))
g = 9.8
#convert angle to radians
th0 = np.deg2rad(th00)

#define functions for x position, y position, and range of projectile
def Xpos(t,θ):
    #convert θ from degrees to radians
    
    x = x0 + (v0*t*np.cos(θ))
    return x

def Ypos(t, th0, y0, v0):
    #convert θ from degrees to radians
    
    y = y0 + ((v0*t)*(np.sin(th0))) - (0.5*g*(t*t))
    return y

#Create function to generate values of t for the given information:
def t_range(θ):
    #start from t = 0
    t = 0
    counter = 0
    while Ypos(t, θ) >= 0:
        t +=0.05
        counter +=1
        continue
    values = np.linspace(0, t, counter)
    return values


def plot_traj(y0, v0, th0, tmax, color):
    print('placeholder')
    return

def tland(y0, v0, th0):
    t = 0
    while Ypos(t, th0, y0, v0) > 0:
        t +=0.005
        continue
    t_land = t
    print(t_land)
    return t_land

test = tland(y0, v0, th0)


#get input of v0 values from txt file.
