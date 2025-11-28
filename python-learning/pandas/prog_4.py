import pandas as pd
import numpy as np

my_df = pd.read_csv("pandas/pandas_practice.csv")
# print(my_df['name'].value_counts())
# print(my_df["marks"].value_counts())
# print(my_df['name'].value_counts()["Rohit"])
# print(my_df.groupby("marks").size())
# print(my_df.groupby('name').count()) 
# print(my_df.apply(pd.value_counts))

my_data = pd.read_csv("pandas/pandas_practice.csv")
gender = ["Male", "Female","Male","Female","Male","3g"]
my_data["Gender"]= gender
# print(my_data)
my_data["alive/dead"] = True
my_data["Married"] = [np.nan] *len(my_data)
# print(my_data)
# my_data.insert(1,"adopted",True)
# print(my_data)
# my_data2 = my_data.assign(Horse = True)
# print(my_data2)

# print(my_data.drop("Gender" ,axis = 1, inplace= True))
# print(my_data) #inplace permanently deletes the columns
# print(my_data.drop(3))#remove index 3 from rows

# print(my_data.loc[2])
# print(my_data.iloc[2])
# print(my_data.loc[1,"name"])
# print(my_data.loc[[1,3],["name","marks"]])

data = pd.read_csv("pandas/dog_data.csv")
# print(data == "BROWN")
print(data[data=="BROWN"])
print(data[data=="BROWN"]["Color"])
print(data[data=="BROWN"][["Color","Breed"]])

# print(data[(data["Color"] == "BROWN") & (data["Breed"] =='MIXED') ].__len__())
# print(data[(data["Color"] == "BROWN"g) | (data["Breed"] =='MIXED') ])
# print(data[(data["Color"] == "BROWN") | (data["Breed"] =='MIXED') ][["DogName", "Breed"]])

#index reset

my_data["header"] = ["Person1","Person2","Person3","Person4","Person5","Person6"]

# print(my_data)
# print (my_data.set_index("header" , inplace = True))
# print(my_data)
# print(my_data.reset_index("header", inplace = True))
# print(my_data)
# print(my_data.drop("header",axis = 1, inplace= True))
# print(my_data)