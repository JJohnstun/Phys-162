import numpy as np
import matplotlib.pyplot as plt
from sys import argv

k = 15.
a = 0.2

def f(y, u, t):
	return -0.5*k*y - a*u


def ODE2step(t0, y0, u0, dt):
	t = t0 + dt
	y = y0 + dt*u0
	u = u0 + dt*f(y0, u0, t0)
	return t, y, u

def solveODE(dt, t0, tf, y0, dy0, file):
	N = int((tf-t0)/dt)	# number of steps

	name = f'{file}-{dt}.dat'
	fout = open(name, 'w')
	t = t0
	y = y0
	dy = dy0
	fout.write(f'{t} {y} {dy}\n')
	for i in range(N):
		t, y, dy = ODE2step(t, y, dy, dt)
		fout.write(f'{t} {y} {dy}\n')
	fout.close()
	return name


tmax = 10.0		# max time for solution
y0 = 1.0		# initial value y(0)
dy0 = 0.0		# initial value y'(0)

if len(argv) > 1:
	k = float(argv[1])
if len(argv) > 2:
	a = float(argv[2])
if len(argv) > 3:
	dt = float(argv[3])

files = []
dtlist = []
#files.append( solveODE(0.1, 0., tmax, y0, dy0,  "ode2") ); dtlist.append(0.1)
files.append( solveODE(0.01, 0., tmax, y0, dy0,  "ode2") ); dtlist.append(0.01)
files.append( solveODE(0.005, 0., tmax, y0, dy0, "ode2") ); dtlist.append(0.005)
files.append( solveODE(0.001, 0., tmax, y0, dy0, "ode2") ); dtlist.append(0.001)
files.append( solveODE(dt, 0., tmax, y0, dy0, "ode2") ); dtlist.append(dt)

plt.figure()
plt.xlabel('t (s)')
plt.ylabel('y(t) (m)')
plt.title(f'Numerical solution')

for file, dt in zip(files, dtlist):
	t, y = np.loadtxt(file, usecols=(0,1), unpack=True)
	plt.plot(t, y, label=f'dt = {dt} s')


plt.legend()
plt.show()