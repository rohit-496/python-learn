import matplotlib.pyplot as plt
import numpy as np

x1 = [0,1,2,3,4,5,6,7]
y1 = [55,60,65,62,68,70,75,78]
x2 = [0,1,2,2,4,5,6,7]
y2 = [50,58,62,78,93,65,88,65]
#x = hours and y = no of marks scored
plt.scatter(x1,y1,
            alpha = 0.8,
           s = 20,
           color ="navy",
           label = "class A")
plt.grid()
plt.scatter(x2,y2,
            alpha = 0.8,
           s = 20,
           color ="brown",
           label ="class B")
plt.title("Shittal's stamina")
plt.xlabel("No. of hours studied",
           color = "black",
           )
plt.ylabel("Marks obtained",
           color = "black",
           )
plt.legend(loc = "upper left")
plt.show()