#Jared Johnstun
#Date created: 12/9/2024

import sys
import numpy as np
import matplotlib.pyplot as plt


time_trans = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=0)
Vr_trans = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=2)
Vc_trans = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=3)
Vl_trans = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=4)
Vd_trans = np.loadtxt('freq - 40000 - trans.txt', skiprows=1, usecols=1)

time_steady = np.loadtxt('freq - 40000 - steady.txt', skiprows=1, usecols=0)
Vr_steady = np.loadtxt('freq - 40000 - steady.txt', skiprows=1, usecols=2)
Vc_steady = np.loadtxt('freq - 40000 - steady.txt', skiprows=1, usecols=3)
Vl_steady = np.loadtxt('freq - 40000 - steady.txt', skiprows=1, usecols=4)
Vd_steady = np.loadtxt('freq - 40000 - steady.txt', skiprows=1, usecols=1)


y_values_trans = [Vc_trans, Vl_trans, Vr_trans]
y_values_steady = [Vc_steady, Vl_steady, Vr_steady]
y_values_volts_trans = [Vr_trans, Vd_trans]
y_values_volts_steady = [Vr_steady, Vd_steady]
elem_colors = ['red', 'blue', 'green']
volt_colors = ['green', 'orange']
elem_legends = ['$V_C$(t) [V]', '$V_L$(t) [V]', '$V_R$(t) [V]']
volt_legends = ['$V_R$(t) [V]', '$V_d$(t) [V]']






#create figure
plt.figure()

#create subplot for each graph
elem_trans = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=1)
elem_steady = plt.subplot2grid((2, 2), (0, 1), rowspan=1, colspan=1)
volt_trans = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=1)
volt_steady = plt.subplot2grid((2, 2), (1, 1), rowspan=1, colspan=1)

#plot the voltages for the transient periods
for i in range(0,3):
    elem_trans.plot(
        time_trans,
        y_values_trans[i],
        color = elem_colors[i],
        linestyle = '-'
    )

#plot the voltages for the steady periods
for i in range(0,3):
    elem_steady.plot(
        time_steady,
        y_values_steady[i],
        color = elem_colors[i],
        linestyle = '-',
        label = elem_legends[i]
    )

#plot driving & resistance voltages for transient periods
for i in range(0, 2):
    volt_trans.plot(
        time_trans,
        y_values_volts_trans[i],
        color = volt_colors[i],
        linestyle = '-'
 
   )


#plot driving & resistance voltages for steady periods
for i in range(0, 2):
    volt_steady.plot(
        time_steady,
        y_values_volts_steady[i],
        color = volt_colors[i],
        linestyle = '-',
        label = volt_legends[i]
 
   )
#Beautify graphs
trans_xvalues = np.linspace(0, 0.00015, 4)
trans_xlabel = np.linspace(0, 6, 4, dtype= int)

steady_xvalues = np.linspace(0.001375, 0.0015, 6)
steady_xlabel = np.linspace(55, 60, 6, dtype=int)


#set tick marks for top 2 graphs
elem_trans.tick_params(top = True, labeltop = True, labelbottom = False)
elem_trans.set_ylabel('Voltage [V]')
elem_trans.set_xticks(trans_xvalues, trans_xlabel)
elem_steady.tick_params(top = True, labeltop = True, labelbottom = False)
elem_steady.set_ylabel('Voltage [V]')
elem_steady.set_xticks(steady_xvalues, steady_xlabel)
elem_steady.set_ylim(elem_trans.get_ylim())


#set tick marks for bottom 2 graphs

volt_trans.tick_params(top=True)
volt_trans.set_xticks(trans_xvalues, trans_xlabel)
volt_trans.set_xlim(elem_trans.get_xlim())
volt_trans.set_xlabel('t [period ' + r'$T$' + ']')
volt_trans.set_ylabel('Voltage [V]')
volt_steady.tick_params(top=True)
volt_steady.set_xticks(steady_xvalues, steady_xlabel)
volt_steady.set_xlim(elem_steady.get_xlim())
volt_steady.set_xlabel('t [period ' + r'$T$' + ']')
volt_steady.set_ylabel('Voltage [V]')


#set legend boxes on right graphs
elem_steady.legend(loc='upper right', bbox_to_anchor = (1.6, 1.05))
volt_steady.legend(loc='upper right', bbox_to_anchor = (1.6, 1.05))

title = 'Driven LRC Circuit, ' + r'$R$' + '=1.078 ' + r'$k\Omega$' + ', ' + r'$C$' + '=0.40 ' + r'$nF$' + ', ' + r'$L$' + '=20.5 ' + r'$mH$'
plt.suptitle(title)
plt.tight_layout()
plt.savefig("Final-JaredJohnstun-fig.pdf")
plt.show()