import matplotlib.pyplot as plt
import numpy as np

x= [1,2,3,4,5]
y = [5,10,15,20,25]

# plt.grid()
plt.grid(axis = "y",
         linewidth = 2,
         color ="lightgray",
         linestyle="dotted")
plt.plot(x,y)
plt.show()