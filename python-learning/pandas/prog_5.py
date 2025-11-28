import pandas as pd
import numpy as np

# stuff = {"A":[1,2,3,4,5], "B":[np.nan,np.nan,5,6,7] , "C":[7,8,9,10,11]}
# my_df = pd.DataFrame(stuff)
# # print(my_df)
# # my_df.dropna() #drops entire row which contain Nan
# # print(my_df.dropna(thresh=2, axis = 1))

# print(my_df.fillna(value = int(99)))
# # print(my_df.fillna(value = my_df["B"].mean()))
# print(my_df.fillna(value = my_df["B"].sum()))

stuff = {
    "corporation":["apple", "google", "meta","apple","google","meta"],
    "employee" : ["john ", "april","wes","seth","michael","rohit"],
    "salary": [200,220,190,130,120,150]
}
my_df = pd.DataFrame(stuff)
# print(my_df)
company = (my_df.groupby("corporation"))
# print(company)
print(company.sum())
print(company.mean())
print(my_df.groupby("corporation")["salary"].mean())
print(company.max())
# print(company.std())
 