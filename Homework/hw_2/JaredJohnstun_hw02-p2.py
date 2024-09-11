#Jared Johnstun
#Date: 9/9/2024

import numpy as np
import matplotlib.pyplot as plt

#define initial condition variables:
x0 = 0 #initial x position
y0 = 0 #initial y position
v0 = 20 #initial velocity
θ0 = 45 #inital angle of velocity relative to horizonal (in degrees) needs to be greater than zero
g = 9.8 #acceleration due to gravity (m/s^2)

#define functions for x position, y position, and range of projectile
def Xpos(t,θ):
    #convert θ from degrees to radians
    angle = np.deg2rad(θ)
    x = x0 + (v0*t*np.cos(angle))
    return x

def Ypos(t,θ):
    #convert θ from degrees to radians
    angle = np.deg2rad(θ)
    y = y0 + ((v0*t)*(np.sin(angle))) - (0.5*g*(t*t))
    return y

def Range(θ):
    angle = np.deg2rad(θ)
    R = ((v0**2)/g)*np.sin(2*angle)
    return R

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



#Create First Plot
θ_range = np.linspace(30, 60, 7)

#Create subplot for zoomed in figure

#Array of colors to iterate over when making graphs
colors = ['magenta', 'r', 'y', 'g', 'c', 'b', 'purple']
linestyles = ['solid', 'dotted', 'dashed', 'dashdot', ':', '-.', ' ']
i=0 # pointer to Color array index
for θ in θ_range:
    #generate range of t values
    t_in = t_range(θ)
    #generate name of curve
    curve_angle = str(θ)
    
    plt.plot(
        Xpos(t_in, θ), #Collection of x values for given t
        Ypos(t_in, θ), #Collection of y values for given t
        color = colors[i],
        linestyle = linestyles[i],
        label = "θ initial (deg) = " + curve_angle

    )
    #increment Colors array index
    i += 1

    #iterate through angles and plot Range values from Range Function
    range_plots = plt.plot(
        Range(θ), # given x value of plot
        0,
        markeredgecolor = "black",
        marker = "+"
    )


plt.xlabel('X-position (m)')
plt.ylabel('Y-position (m)')
plt.title('Comparisons of x-y position and Range Functions')
plt.legend()
plt.xlim(0)
plt.ylim(0)
print("Showing plot window.")	
print("Nothing else will happen until you close the plot window!")
plt.savefig("Homework/Hw_2/JaredJohnstun_hw02-p2_image.pdf")

plt.title('Zoomed In Figure')
plt.xlim(35, 45)
plt.ylim(-0.01, .1)
plt.savefig("Homework/Hw_2/JaredJohnstun_hw02-p2_zoom_image.pdf")
plt.show()


