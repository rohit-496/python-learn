#linear algebra
import numpy as np
# a = np.array([1,2,3,4])  # create array

# b = np.ones((3,3)) # 3*3 matrix from one
# c = np.full((3,2),2) # 3*2 matrix full of the element 2
# print(np.matmul(b,c)) # matrix multiply

# d= np.identity(3)
# print(d) #identity matrix
# print(np.linalg.det(d)) #determinant of the matrix

arr = np.array([[1,2,3,4],
                [5,6,7,8]
                ])
# print(np.delete(arr,1,axis=0))
print(np.delete(arr,1,axis=1))
# print(np.append(arr,[[2,3,4,5],[5,6,7,8]],axis= 0))
a2 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])
res3 = np.concatenate((a2, b2), axis=0)
# print("Concatenate 2D axis=0:\n", res3)


a = np.array([[1, 1],
               [2, 2],
                 [3, 3]])
# print(np.insert(a,2,[0,2],axis=0))
# Insert different values for each row at column index 1:
vals = [[13], [2], [33]]  # shape (3, 1)
res2 = np.insert(a, [1],vals, axis=1)
# print(res2)
new_row = np.array([9, 9])
res3 = np.insert(a, 1, new_row, axis=0)
print(res3)

b = np.array([[1,2,3,4,5]])
# print(np.insert(b,[1],[5,6,7,8,9],axis =0))