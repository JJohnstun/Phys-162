#Jared Johnstun
#Date: 10/16/2024
#Midterm 1

import sys
import numpy as np
import matplotlib.pyplot as plt

#Generate some needed constants
#x0 = 0 #change later, use input


#Using the following equations for General reference
#position s = si + vi*t + 1/2ai(t**2)
#velocity vi = v0 +ai(t)


#acceleration arrays for acc. constants of each part of the rocket launch
ax = [0.96, -1.39, 0.93]
ay = [3.9, -9.8, 6.9]
#array's of initial conditions for each section of trajectory, will be appended to as trajectories are calculated
x0 = []
y0 = []
vx0 = [0]
vy0 = [0]
t_total = []

def pos(t, index, dir):
    if dir == 'x':
        x = x0[index] + vel(0, index, 'x' )*t + ((0.5*ax[index])*(t**2))
        return x
    
    elif dir == 'y':
        y = y0[index] + vel(0, index, 'y')*t + ((0.5*ay[index])*(t**2))
        return y


def vel(t, a_index, dir):
    
    if dir == 'x':
        vx = vx0[a_index] + ax[a_index]*t
        return vx
    elif dir == 'y':
        vy = vy0[a_index] + ay[a_index]*t
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

def ground_height(x_input):
    ground = read_ground()
    if x_input > len(ground):
        gr_height = ground[-1]
    else: 
        gr_height = ground[x_input]
    
    return gr_height

def get_x0_y0():
    while True:
        try:
            x00 = input('Please enter an initial x starting position as a whole number in meters: ')
            x00_int = int(x00)
        except:
            print("What you entered was not an integer, please try again.")
            continue
        else:
            #write to array's for future reference
            x0.append(x00_int)
            y0.append(ground_height(x00_int))
            break

def append_arrays(t_stop, ref_index):
    #generate values needed for appending
    x_inter1 = pos(t_stop, ref_index, 'x')
    y_inter1 = pos(t_stop, ref_index, 'y')
    vx_inter1 = vel(t_stop, ref_index, 'x')
    vy_inter1 = vel(t_stop, ref_index, 'y')
    #append those values
    x0.append(x_inter1)
    y0.append(y_inter1)
    vx0.append(vx_inter1)
    vy0.append(vy_inter1)
    '''
    #print the values for my own reference
    print('time passed through phase = ' + str(t_stop))
    print(x0)
    print(y0)
    print(vx0)
    print(vy0)
    '''
        
def make_t_ranges():
    #t_range for part 1 is from 0 to 76 seconds
    t_range1 = np.linspace(0, 76, 7700)
    #append reference arrays with conditions at t=76
    append_arrays(76, 0)


    #loop through increments of time until desired height is reached
    t2 = 0 # given time part 2 starts - will continue to update this value
    counter = 0
    while pos(t2, 1, 'y') >= 3573:
        
        t2 += 0.01
        counter +=1
        continue
    t_range2 = np.linspace(0, t2, counter)
    #append reference arrays with conditions at whatever time h=3573
    append_arrays(t2, 1)
    t_start = t2
    #t now equals time of second intersection. continue to increment t until it now intersects with ground.
    
    t3 = 0
    counter = 0
    try:
        while pos(t3, 2, 'y') > ground_height(round(pos(t3, 2, 'x'))):
            t3 +=0.01
            counter += 1
            continue
    #Ground may not extend as far as the rocket goes, create compensation for that contingency
    except IndexError:
        print('time = ' + str(t2))
        print('ending position in meters: ' + str(round(pos(t2, 2, 'x'))))

    #append arrays with final landing points
    append_arrays(t3, 2)
    

    t_range3 = np.linspace(0, t3, counter)

    return t_range1, t_range2, t_range3

    

#begin plotting figure
get_x0_y0()
t1, t2, t3 = make_t_ranges()
x1 = pos(t1, 0, 'x')
y1 = pos(t1, 0, 'y')
x2 = pos(t2, 1, 'x')
y2 = pos(t2, 1, 'y')
x3 = pos(t3, 2, 'x')
y3 = pos(t3, 2, 'y')
x_final = round(x3[-1])
x_final += 1
gy = []
print(x_final)
print(len(read_ground()))
for x in range(0, x_final):
    gy.append(ground_height(x))
print(len(gy))

plt.figure()
main = plt.subplot2grid((4, 4), (0,0), rowspan=4, colspan=2)
main.plot(
    x1,
    y1,
    color = 'blue',
    linestyle = '-',
    label = 'test'
)
main.plot(
    x2,
    y2,
    color = 'red',
    label = ''

)
main.plot(
    x3,
    y3,
    color = 'purple',
    label = ''
)

main.plot(
    np.linspace(0, x_final, x_final),
    gy,
    color = 'black',
    linestyle = '-'
)

main.set_xlabel('x (km)')
main.set_ylabel('y (km)')
tick_xvalues = [0,1000,2000,3000,4000]
tick_xlabel = ['0', '1.0', '2.0', '3.0', '4.0']

main.set_xticks(tick_xvalues, tick_xlabel)
plt.savefig("JaredJohnstun_M1_p1_fig.pdf")
plt.show()