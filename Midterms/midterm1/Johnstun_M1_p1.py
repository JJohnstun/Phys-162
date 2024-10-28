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

def v_mag(t, a_index):
    vx = vel(t, a_index, 'x')
    vy = vel(t, a_index, 'y')
    v_mag = np.sqrt((vx**2) + (vy**2))
    return v_mag

def read_ground():
    ground_1d = []
    ground_2d = []
    loader = ''
    if len(sys.argv) < 2:
        return np.zeros(5)
    
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
    if x_input >= len(ground):
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
        
def make_t_ranges():
    #t_range for part 1 is from 0 to 76 seconds
    t_range1 = np.linspace(0, 76, 7600)
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

#function desinged to take the values in make_t_ranges and generate continuous values
#from t = 0 to t_land, as opposed from when each segment starts and stops
def t_continuous(part1, part2, part3):
    #take the last entry from each time array and add them together
    #update part 2 to continue from part 1,
    t2_new = []
    for i in range(0, len(part2)):
        t_new = part1[-1] + part2[i]
        t2_new.append(t_new)
    
    #repeat with part 3
    t3_new = []
    for i in range(0, len(part3)):
        t_new = t2_new[-1] + part3[i]
        t3_new.append(t_new)
    return part1, t2_new, t3_new

def did_you_crash(velocity):
    if velocity < 5:
        return 'smooth landing, looking good'
    elif velocity < 25:
        return 'rough landing, you lived to tell the tale'
    else:
        return 'epic crash, you will be remembered.'

if len(sys.argv) < 2:
    print('ground file not specified, default values being used')
#Generate important values needed to plot figures
get_x0_y0()
t1, t2, t3 = make_t_ranges()
cont1, cont2, cont3 = t_continuous(t1, t2, t3)
time_cont = [cont1, cont2, cont3]
#time_cont_inter = [t1[-1], t2[-1], t3[-1]]

x1 = pos(t1, 0, 'x')
y1 = pos(t1, 0, 'y')
x2 = pos(t2, 1, 'x')
y2 = pos(t2, 1, 'y')
x3 = pos(t3, 2, 'x')
y3 = pos(t3, 2, 'y')
x_final = round(x3[-1])
gy = []
for x in range(0, x_final):
    gy.append(ground_height(x))


#create figure
plt.figure()

#create subplot for each graph
main = plt.subplot2grid((4, 4), (0,0), rowspan=4, colspan=2)
position = plt.subplot2grid((4, 4), (0,2), rowspan=1, colspan=2)
v_speed = plt.subplot2grid((4, 4), (1,2), rowspan=1, colspan=2)
v_x = plt.subplot2grid((4, 4), (2,2), rowspan=1, colspan=2)
v_y = plt.subplot2grid((4, 4), (3,2), rowspan=1, colspan=2)

#array containing subplots handles for faster plotting
sub_plot = [position, v_speed, v_x, v_y]

#common attributes across each subplot
colors = ['red', 'blue', 'purple', 'black']
markers = ['*', 's', 'v']
#Main subplot features
x_values = [x1, x2, x3, np.linspace(0, x_final, x_final)]
y_values = [y1, y2, y3, gy]
line_width = [1.5, 1.5, 1.5, 2.5]
annotations = ['Engine turns off', 'Slow down', 'Landing point']
part_labels = ['Engine on, ', 'Engine off, ', 'Slowing down, ']
annot_locations = ['right', 'left', 'left']
#features for the other 4 plots
v_mags = [v_mag(t1, 0), v_mag(t2, 1), v_mag(t3, 2)]
v_mag_points = [v_mag(t1[-1], 0), v_mag(t2[-1], 1), v_mag(t3[-1], 2)]
v_xs = [vel(t1, 0, 'x'), vel(t2, 1, 'x'), vel(t3, 2, 'x')]
v_ys = [vel(t1, 0, 'y'), vel(t2, 1, 'y'), vel(t3, 2, 'y')]
t_intersections = [cont1[-1], cont2[-1], cont3[-1]]


#big loop to plot all  4 graphs relatively efficiently
for i in range(0,4):
    point_index = i+1
    shift_index = i-1
    graph_label = ''
    if i == 3: #if statement to exclude legend from ground line
        graph_label = ''
        main.plot(
            x_values[i],
            y_values[i],
            color = colors[i],
            linestyle = '-',
            linewidth = line_width[i],
            label = graph_label
        )
    else:
        graph_label = part_labels[i] + r'$\vec{a}$''= ('f'${ax[i]},{ay[i]} ) m/s^{2}$'
        main.plot(
            x_values[i],
            y_values[i],
            color = colors[i],
            linestyle = '-',
            linewidth = line_width[i],
            label = graph_label
        )

  

    #plot the intersection points as separate command
    #reference index of intersection points is shifted due to storing
    #starting conditions
    if i > 3: #if statement alleviates index error for including ground curve
        continue
    elif i == 0:
        #first plot on right has two curve plots, so separate elif exists
        for j in range(0,3):
            skip_index = j+1
            #plot x(t)
            sub_plot[i].plot(
                time_cont[j],
                x_values[j],
                color = colors[j],
                linestyle = 'dashdot'
            )
            #plot y(t)
            sub_plot[i].plot(
                time_cont[j],
                y_values[j],
                color = colors[j]
            )
            #plot x - intersection point
            sub_plot[i].plot(
                t_intersections[j],
                x0[skip_index],
                color = colors[j],
                marker = markers[j]
            )
            #plot y - intersection point
            sub_plot[i].plot(
                t_intersections[j],
                y0[skip_index],
                color = colors[j],
                marker = markers[j]
            )

    else:
        
        main.plot(
            x0[i],
            y0[i],
            color = colors[shift_index],
            marker = markers[shift_index],
            markersize = 5.0
        )
        #annotate the intersection points
        main.text(
            x0[i],
            y0[i],
            annotations[shift_index],
            ha = annot_locations[shift_index],
            va = 'bottom',
            fontsize = 10,
            color = colors[shift_index]
        )

        #for each other sub plot iterate through each trajectory part and plot
        for j in range(1,4):
            shift_index = i-1
            if j == 1:
                sub_plot[j].plot(
                    time_cont[shift_index],
                    v_mags[shift_index],
                    color = colors[shift_index]
                )
                #plot the intersection point of relevance
                sub_plot[j].plot(
                    t_intersections[shift_index],
                    v_mag_points[shift_index],
                    color = colors[shift_index],
                    marker = markers[shift_index]
                )
                
            elif j == 2:
                sub_plot[j].plot(
                    time_cont[shift_index],
                    v_xs[shift_index],
                    color = colors[shift_index],
                    linestyle = '--'
                )
                #plot the relevant intersection point:
                sub_plot[j].plot(
                    t_intersections[shift_index],
                    vx0[i],
                    color = colors[shift_index],
                    marker = markers[shift_index]
                )

            elif j == 3:
                sub_plot[j].plot(
                    time_cont[shift_index],
                    v_ys[shift_index],
                    color = colors[shift_index],
                    linestyle = ':'
                )
                sub_plot[j].plot(
                    t_intersections[shift_index],
                    vy0[i],
                    color = colors[shift_index],
                    marker = markers[shift_index]
                )

    #tweak some common subplot settings:
    sub_plot[i].set_xlim(0)
    sub_plot[i].set_xlabel('t (min)')
    sub_plot[i].set_xticks(np.linspace(0, 180, 7), np.linspace(0, 3, 7))
    sub_plot[i].spines['right'].set_visible(False)
    sub_plot[i].spines['top'].set_visible(False)

            
main.set_xlabel('x (km)')
main.set_ylabel('y (km)')
tick_xvalues = np.linspace(0, 4000, 5)
tick_xlabel = np.linspace(0, 4, 5)
tick_yvalues = np.linspace(0, 16000, 9)
tick_ylabel = np.linspace(0, 16, 9)

main.set_xticks(tick_xvalues, tick_xlabel)
main.set_yticks(tick_yvalues, tick_ylabel)
main.set_xlim(0)
main.legend().set_loc('upper left')

#tweak unique settings in each subplot
sub_plot[0].set_yticks(np.linspace(0, 12000, 3), np.linspace(0, 12, 3))
sub_plot[2].spines['bottom'].set_position(('data', 0))
sub_plot[3].spines['bottom'].set_position(('data', 0))
sub_y_labels = ['position (km)', 'v (m/s)', '$v_x$ (m/s)', '$v_y$ (m/s)']
for each in range(0,4):
    sub_plot[each].set_ylabel(sub_y_labels[each])

landing_message = did_you_crash(v_mag(t3[-1], 2))
print(landing_message)
plt.tight_layout()
plt.savefig("JaredJohnstun_M1_p1_fig.pdf")
plt.show()