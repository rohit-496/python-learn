 # numpy for efficient memory storage and faster than lists... uses contigous memory blocks                 
import numpy as np

# a = np.array([1,2,3],dtype='int32' )

# print(a.dtype)
# b= np.array([1,3,5])
# # # while in lists this is not possible
# # print (a*b)

b = np.array([[9,0,8,0]
              ,[6,0,5,4]])
# print(b.ndim) # which d array
# print(b.shape) #dimention a * b 
# print(b.dtype) #datatype
# print(b.size) #no of elements
# print(b[1,2])

#get specific element by[r,c]
# print(b[0,:])
# print(b[:,2])
# print(b[2:])
# print(b[::-1])
# print(b[:,2])
print(b[0:1,0:2])

# a = np.zeros((2,3))
# a = np.ones((2,3))
# # print(a)
# print(np.full((2,3),99))
# print(np.full(b.shape,4))

#random decimal numbrs
# print(np.random.rand(4,2)) 4*2 matrix banauchha jun random number le fill hunchha
# print(np.random.random_sample(b.shape)) #b ko shaoe ko rnaodm number le fill gardinchha

# print(np.random.randint(7,size=(3,4))) #positional value smma ko rnadom integer linxa
# print(np.random.randint(7,8,size=(3,4))) #positional value smma ko rnadom integer linxa

# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3, axis= 0)
# r2 = np.repeat(arr,3, axis= 1)
# print (r1,r2)
# print(np.identity(5))

arr = np.array([[1,2]
                ,[3,4]])
# # r1 = np.repeat(arr, 2, axis=0)   # repeat rows
# # r2 = np.repeat(arr, 2, axis=1)   # repeat columns
# r1 = np.repeat(arr[0], 2, axis=0)  # repeat rows
# print(r1)
# r3 = np.sum(arr,axis = 1)
# print(r3)


# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 9 0 1 
# 1 0 0 0 1
# 1 1 1 1 1 
 
# output =np.ones((5,5)) 
# z = np.zeros((3,3))
# z[1,1]= 9

# output[1:4,1:4] = z
# print(output)

# In this b and a points to the same things so it updates value of a when we update b
# a = np.array([1,2,3])
# b = a[:]
# print(b)
# b[0] = 100
# print(a,b)

# Correct method
# a = np.array([1,2,3])
# b = a.copy()
# b[0] = 100
# print(a,b)

