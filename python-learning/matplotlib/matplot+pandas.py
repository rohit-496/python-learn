import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("matplotlib/dog_data.csv")
type_count = (df["Breed"].value_counts(ascending = True))

plt.barh(type_count.index, type_count.values)

plt.show()
# print(df["Breed"].value_counts())