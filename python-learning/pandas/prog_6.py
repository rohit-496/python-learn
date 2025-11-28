import pandas as pd 
import numpy as np

my_df = pd.read_csv("pandas/dog_data.csv")
# print(my_df['DogName'])
# print(my_df['DogName'].value_counts())

# print(my_df["DogName"].unique())
# print(pd.DataFrame(my_df["DogName"].unique()))


#apply function used to apply any function by creating it 
stuff = {
    "corporation":["apple", "google", "meta","apple"],
    "employee" : ["john", "april","wes","seth"],
    "salary": [100,200,300,123]
}
my_df = pd.DataFrame(stuff)

def times1000(x):
    return format(x*1000,",d")

my_df["salary"] =my_df["salary"].apply(times1000)
print(my_df)
# print(pd.DataFrame(my_df["salary"].apply(times1000)))

def namer(x):
    if x == "john":
        return "John Chamal"
    else:
        return "Vakk"

# print(my_df['employee'].apply(namer))
# print(my_df["salary"].apply(lambda x:format(x*1000 , ",d")))

#apply function multiple columns

my_df["salary"] = my_df["salary"].apply(times1000)
# print(my_df)

# def namer(x):
#     return "codemy: "+x

# my_df[["corporation", "employee"]] =(my_df[["corporation", "employee"]].applymap(namer))
# print(my_df)

# print(my_df["salary"].sort_values())
# print(my_df.sort_values('salary'))
# print(my_df.sort_values('salary', ascending=False))
# print(my_df.sort_values("corporation"))