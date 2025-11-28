import matplotlib.pyplot as plt
import numpy as np

categories =["Grains","Fruits","Vegetables","Protein","Dairy"]
values = np.array([4,3,2,5,3])
plt.bar(categories, values,
        color="navy"
        )
plt.xlabel("Grocery",
           fontweight = "bold",
           fontsize = 10)
plt.ylabel("No. of items",
           fontweight = "bold",
           fontsize = 10)


plt.show()