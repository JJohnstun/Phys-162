import matplotlib.pyplot as plt

print("Python script has started.")
print("Creating a simple plot...")
plt.figure()
#first plot with added values and other changes
line_1 = plt.plot([1, 2, 3, 4, 5, 6, 7],	# list of x-values to plot
	[1, 4, 2, 5, 8, 3, 5],  		# list of y-values to plot
	color="purple",        	#  Line color
	linestyle="-",     	#  Line style
	marker="o",         	#  Symbol used at data point
	markeredgecolor="blue",  # Symbol color
    label ="Purple Line"
	)

#second added plot
line_2 = plt.plot( [1, 2, 3, 4, 5, 6, 7], #list of the x-values
    [4, 7, 12, 14, 16, 19, 3], #list of the y - values
    color = "orange", #Line color
	linestyle = "--", #line style
    marker = "+", #symbol used at data point
    markeredgecolor = "red", #Symbol color
    label = "Orange Line"
	)
plt.xlabel('The X Axis')
plt.ylabel('The Y Axis')
plt.title('This is the plot title')
plt.legend()
print("Showing plot window.")
print("Nothing else will happen until you close the plot window!")
plt.savefig("JaredJohnstun_hw01-p2_image.pdf")
plt.show()
print("Python script is done.")