#Jared Johnstun
#Date 9/17/2024
#Homework 3 Problem 3

import os
import sys
import matplotlib.pyplot as plt
import numpy as np
#obtain the various columns of data from provided text file
x = np.loadtxt('hw03-data.txt', skiprows=3, usecols=0)
y = np.loadtxt('hw03-data.txt', skiprows=3, usecols=1)
z = np.loadtxt('hw03-data.txt', skiprows=3, usecols=3)

#plot first graph of x vs y
plt.plot(
    x, #xvalues for first graph
    y, #y positions for first graph (testing)
    color = 'red',
    linestyle = '--',
    label = 'x vs y'
)

#plot second graph of x vs z
plt.plot(
    x, #xvalues for first graph
    z, #y positions for first graph (testing)
    color = 'blue',
    linestyle = '--',
    label = 'x vs z'
)

#plot third graph of x vs (z/y)
output = z/y
plt.plot(
    x, #xvalues for first graph
    output, #y positions for first graph (testing)
    color = 'purple',
    linestyle = '--',
    label = 'x vs (z/y)'
)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Homework 3 Problem 3')
plt.legend()
print("Showing plot window.")	
print("Nothing else will happen until you close the plot window!")
plt.savefig('JaredJohnstun_hw03-p3_fig.pdf')
plt.show()

#Compute Sum and Average of each array and print to screen
x_sum = np.sum(x)
x_average = np.average(x)
x_line = str(f'sum of array x is {x_sum: .2f} average = {x_average: .3f}')


y_sum = np.sum(y)
y_average = np.average(y)
y_line = str(f'sum of array x is {y_sum: .2f} average = {y_average: .3f}')

z_sum = np.sum(z)
z_average = np.average(z)
z_line = str(f'sum of array x is {z_sum: .2f} average = {z_average: .3f}')

print(x_line)
print(y_line)
print(z_line)