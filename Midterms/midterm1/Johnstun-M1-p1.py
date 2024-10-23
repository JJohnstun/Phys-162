#Jared Johnstun
#Date: 10/16/2024
#Midterm 1

import sys
import numpy as np
import matplotlib.pyplot as plot

#Generate some needed constants
x0 = 0 #change later, use input
y0 = 0 #change later, determine this from ground function

#Using the following equations for General reference
#position s = si + vi*t + 1/2ai(t**2)
#velocity vi = v0 +ai(t)

#acceleration constants for "engine on" part (m/s^2)
a1x = 0.96
a1y = 3.9

#acceleration constants for "engine off" part (m/s^2)
a2x = -1.39
a2y = -9.8

#acceleratikno constants for "landing" part (m/s*2)

a3x = 0.93
a3y = 6.9
#create arrays for reference
ax = [0.96, -1.39, 0.93]
ay = [3.9, -9.8, 6.9]

def Xpos(t, x0, ax_index):
    x = x0 + vel(t, ax_index, 'x' ) + 0.5*((ax[ax_index])**2)
    return x

def Ypos(t, y0, ay_index):
    y = y0 + vel(t, ay_index, 'y') + 0.5((ay[ay_index])**2)
    return y

def vel(t, a_index, dir):
    
    v0 = 0
    
    if dir == 'x':
        vx = v0 + ax[a_index]*t
        return vx
    elif dir == 'y':
        vy = v0 + ay[a_index]*t
        return vy
    else:
        print('direction wasnt either x or y, review velocity function')

def read_ground():
    ground_1d = []
    ground_2d = []
    loader = sys.argv
    ground_file = loader[1]
    #load in ground file
    with open(ground_file, 'r') as ground:
        for line in ground:
            line = line.strip().split(', ')
            ground_2d.append(line)
            #at this point you have a 2d array of varying width with proper delimiting
        #iterate through 2d array and flatten it
        for row in ground_2d:
            for column in row:
                ground_1d.append(column)
        
    
    
    return ground_1d



test = read_ground()
print(test)
