#Jared Johnstun
#Date: 10/16/2024
#Midterm 1

import sys
import numpy as np
import matplotlib.pyplot as plot

#Generate some needed constants
#x0 = 0 #change later, use input


#Using the following equations for General reference
#position s = si + vi*t + 1/2ai(t**2)
#velocity vi = v0 +ai(t)


#acceleration arrays for acc. constants of each part of the rocket launch
ax = [0.96, -1.39, 0.93]
ay = [3.9, -9.8, 6.9]

def Xpos(t, ax_index, x0):
    x = x0 + vel(0, ax_index, 'x' )*t + ((0.5*ax[ax_index])*(t**2))
    return x


def Ypos(t, y0, ay_index):
    y = y0 + vel(0, ay_index, 'y')*t + ((0.5*ax[ay_index])*(t**2))
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
        
        #map array to floating type
        ground_float = list(map(float, ground_1d))

    return ground_float

def ground_height(x0):
    ground = read_ground()
    gr_height = ground[x0]
    return gr_height

def get_x0():
    while True:
        try:
            x0 = input('Please enter an initial x starting position as a whole number in meters: ')
            x0_int = int(x0)
        except:
            print("What you entered was not an integer, please try again.")
            continue
        else:
            return x0_int
        
def make_t_ranges():



    return