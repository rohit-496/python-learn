#statistics
import numpy as np
# stats = np.array([1,2,3,4,5])
# print(np.min(stats))
# print (np.max(stats))
# print(np.median(stats))

# stat = np.array([[1,2,3],
#                 [4,3,2]])
# print(np.min(stat,axis = 0))

#reorganizing arrays

# before = np.array([[1,2,3,4],[5,6,6,8]])
# print(before)
# after = before.reshape((4,2))
# print(after)
#we can shape until  it has fixed amount of elements

#vertical stacking vectors


'''v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
v3 = np.vstack([v1,v2,v1,v2])
print (v3)

h3 =  np.hstack([v1,v2])
print(h3)
'''
#Miscellaneous
#for some reasons we don't want to use pandas to extract some data from files so in that case we can load trhe data into numpy arays without any problem

 
# filedata = np.genfromtxt("data.txt", delimeter = ',')
# load data from a file in an array seperated by a comma and for each line it makes a 1d array

# filedata.astype('int32')

'''Advanced indexing and Boolean masking'''
# filedata>50
# it returns true or false acoording to the condition of the file

# filedata([filedata>50]) #it returns an array of data which is greater than 50

'''index with a list in numpy'''

'''a = np.array([1,2,3,4,5,6,7])
print(a[1,2,8])

np.any(filedata>50, axis = 0) #returns an array across the rows with boolean true or false if any value across the row is > 50

np.all(filedata>50,axis =  0) #checks and return true or falls if all data across the rows is >50

((filedata>50) & (filedata<100))
(~((filedata>50) & (filedata<100)))
#multiple condition

'''
arr= np.array([[1, 2 ,3 ,4 ,5],
            [6 ,7 ,8 ,9 ,10],
            [11 ,12, 13 ,14 ,15],
            [16 ,17, 18, 19 ,20],
            [21, 22, 23 ,24, 25],
            [26, 27, 28 ,29 ,30]])


# print(arr[[0,1,2,3] , [1,2,3,4]])
# print(arr[0,3:5], arr[4:6,3:5])
# print(arr[[0,4,5], 3:])
