import pandas as pd
import numpy as np

my_series= [5,9,12,27]
my_var = pd.Series(my_series)
# print(my_var)
# print(my_var[2]) deprecated

my_index = ["a" ,"b", "c","d"]

my_var2 = pd.Series(my_series, my_index)
# print(my_var2)

# print(my_var2["b"])
# print(my_var2[1])

cars = {"tesla":12, "mercedes":42}
var_3 = pd.Series(cars)
# print(var_3)
# print(var_3["tesla"])

my_values = [1,2,3,4,5]
var_4 = pd.Series(my_values, index=["a","b","c","d","e"])
print(var_4)
