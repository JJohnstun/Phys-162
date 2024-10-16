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



def Xpos(t, x0):
    return

def Ypos(x):
    return

def read_ground():
    loader = sys.argv
    ground_file = loader[1]
    #load in ground file
    ground = np.loadtxt(ground_file)
    ground_1d = []

    for row in ground:
        #iterate through each column:
        for column in row:
            ground_1d.append(column)
    
    
    return ground_1d

test = read_ground()
print(test)
