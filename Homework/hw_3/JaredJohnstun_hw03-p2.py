#Jared Johnstun
#Date: 9/16/2024
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

x0 = 0 #initial x position
y0 = float(sys.argv[1]) #initial y position
v0 = float(sys.argv[2]) #initial velocity
θ0 = float(sys.argv[3]) #inital angle of velocity relative to horizonal (in degrees) needs to be greater than zero
g = 9.8 #acceleration due to gravity (m/s^2)

#convert angle to radians
θ = np.deg2rad(θ0)

#define functions for x position, y position, and range of projectile
def Xpos(t,θ):
    #convert θ from degrees to radians
    
    x = x0 + (v0*t*np.cos(θ))
    return x

def Ypos(t,θ):
    #convert θ from degrees to radians
    
    y = y0 + ((v0*t)*(np.sin(θ))) - (0.5*g*(t*t))
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


#generate range of t values
t_in = t_range(θ)
#generate name of curve
'''
curve_angle = str(f'θ ={θ0: .1f} \N{DEGREE SIGN}')
initial_height = str(f'\nInitial Height = {y0: .1f} m')
initial_velocity = str(f'\nInitial Velocity = {v0: .1f} m/s')
'''


plt.figure()
plt.plot(
    Xpos(t_in, θ), #Collection of x values for given t
    Ypos(t_in, θ), #Collection of y values for given t
    color = 'purple',
    linestyle = '--',
    label = f'θ ={θ0: .1f} \N{DEGREE SIGN} \nInitial Height = {y0: .1f} m \nInitial Velocity = {v0: .1f} m/s'

)

plt.xlabel('X-position (m)')
plt.ylabel('Y-position (m)')
plt.title('Homework 3 Problem 2')
plt.legend()
plt.xlim(0)
plt.ylim(0)
print("Showing plot window.")	
print("Nothing else will happen until you close the plot window!")
plt.savefig("JaredJohnstun_hw03-p2_fig.pdf")
plt.show()