import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,10)#linspace is for creating a vector, start,end,number of points.
y = np.sin(x)

#create plot
plt.plot(x,y)
plt.title("this is a sine function")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.savefig('plot.png')

plt.show()

