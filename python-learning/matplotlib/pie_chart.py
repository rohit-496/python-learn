import matplotlib.pyplot as plt
import numpy as np

categories =["Freshmen","Sophomores","Juniors","Seniors"]
values = np.array([300,250,275,255])
colors = ["red","yellow","blue","green"]
plt.pie(values , labels=categories,
        autopct="%.2f %%",
        colors=colors,
        explode = [0,0,0,0.1],
        shadow=True,
        startangle= 90)
plt.title("Shittal's kothi")
plt.show()