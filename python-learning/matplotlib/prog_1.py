import matplotlib.pyplot as plt
import numpy as np
# print(matplotlib.__version__)
x =np.array([2023,2024,2025,2026])
y =np.array([15,30,35,100])
y2 = np.array([30,40,50,69])
y3 = np.array([20,25,30,34])
# plt.plot(x,y)
line_style = dict(marker =".",
        markersize =10,
        markerfacecolor ="black",
        markeredgecolor ="black",
        linestyle ="solid",
        linewidth =2,
        )
# plt.plot(x,y2,marker =".",
#         markersize =20,
#         markerfacecolor ="black",
#         markeredgecolor ="black",
#         linestyle ="dashdot",
#         linewidth =10,
#         color ="pink")
plt.plot(x,y,**line_style, color= "green")
plt.plot(x,y2,**line_style , color ="navy")
plt.plot(x,y3,**line_style , color ="cyan")
plt.title("Shittal's body count over the years",
            fontsize = 20,
            family="Arial",
            fontweight ='bold',
            color ="black")
plt.xlabel("Year",
           fontsize = 10,
            family="Arial",
            fontweight ='bold')
plt.ylabel("Shittal's Body count",
           fontsize = 10,
            family="Arial",
            fontweight ='bold')
plt.xticks(x)
plt.tick_params(axis = "both",
                color ="navy")


plt.show()

