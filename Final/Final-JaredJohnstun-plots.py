#Jared Johnstun
#Date created: 12/9/2024

import sys
import numpy as np
import matplotlib.pyplot as plt


time = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=0)
Vr = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=2)
Vc = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=3)
Vl = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=4)
Vd = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=1)
y_values = [Vr, Vc, Vl]
colors = ['blue', 'red', 'green']






#create figure
plt.figure()

#create subplot for each graph
elem_trans = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=1)
elem_steady = plt.subplot2grid((2, 2), (0, 1), rowspan=1, colspan=1)
volt_trans = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=1)
volt_steady = plt.subplot2grid((2, 2), (1, 1), rowspan=1, colspan=1)

for i in range(0,2):
    elem_trans.plot(
        time,
        y_values[i],
        color = colors[i],
        linestyle = '-'
    )

volt_trans.plot(
    time,
    Vd,
    color = 'black',
    linestyle = '-'
)
volt_trans.plot(
    time,
    Vr,
    color = 'green',
    linestyle = '-'
)
plt.show()