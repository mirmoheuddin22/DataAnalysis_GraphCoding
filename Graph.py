import matplotlib.pyplot as plt
#Separate graph (Very basic plot).
x = [1, 3, 5, 10]
plt.plot(x)
plt.show()

y = [7, 12, 21, 22]
plt.plot(x,y)
plt.show()

# Let's plot a lovely looking plot.
#Line 1-points.
x = [3, 9, 14]
y = [2, 7, 30]
#Plotting x and y.
plt.plot(x, y, c='red', linewidth =3, label='Line1')

#Line 2-points.
x2 = [1, 15, 18]
y2 = [0, 3, 31]
#Plotting x2 and y2.
plt.plot(x2, y2, c='green', linewidth =2, label='Line2', linestyle='dashed', marker='s', markerfacecolor='orange', markersize=10)

#Label the axes and give the plot a title.
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two lines!')

#Limits of axes.
plt.ylim(1, 10)
plt.xlim(0, 30)
#Show the legend on the plot.
plt.legend()

#Get python to show the plot.
plt.show()
