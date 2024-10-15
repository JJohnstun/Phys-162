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

#Create needed global variables
x0 = 0
y0 = float(input("Please Enter the Initial Height of the Trajectory in meters: "))
th0_deg = []

#v0 = np.loadtxt('v0vals.txt', unpack=True)
g = 9.8 #gravity (m/s)

'''

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

#function to determine time of landing for each projectile
def tland(y0, v0, th0):
    t_land=[]
    for each in th0:
        t = 0
        while Ypos(t, th0, y0, v0) > 0:
            t +=0.01
            continue
        t_land[each] = t
        print('time of landing for projectile: ' + str(t))
    return t_land


#function that graphs given data
def plot_traj(y0, v0, th0, tmax, color):
    #create figure
    plt.figure()

    return
'''


for i in range(0, len(sys.argv)):
    #skip the index of sys.argv containing file name
    if i == 0:
        continue
    #write angle command options to th0 array for later use
    else:
        
        j = int(i) - 1
        print('i=')
        print(i)
        print('J=')
        print(j)
        #th0_deg[j] = sys.argv[i]



#convert angle to radians
th0 = np.deg2rad(th0_deg)

print(sys.argv)
