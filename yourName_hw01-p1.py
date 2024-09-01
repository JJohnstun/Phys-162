import matplotlib.pyplot as plt

print("Python script has started.")
print("Creating a simple plot...")
plt.figure()
plt.plot([1, 2, 3, 4, 5, 6, 7],	# list of x-values to plot
	[1, 4, 2, 5, 8, 3, 5],  		# list of y-values to plot
	color="purple",        	#  Line color
	linestyle="-",     	#  Line style
	marker="o",         	#  Symbol used at data point
	markeredgecolor="blue"  # Symbol color
	)
plt.xlabel('The X Axis')
plt.ylabel('The Y Axis')
plt.title('This is the plot title')
plt.legend
print("Showing plot window.")
print("Nothing else will happen until you close the plot window!")
plt.savefig("plot.pdf")
plt.show()
print("Python script is done.")