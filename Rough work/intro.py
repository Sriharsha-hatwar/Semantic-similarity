#numpy tutorial 
#homogeneous multidimensional array
#dimensions are called as 'axes'
#the number of axes is rank.
import numpy as np
'''
cvalues = [25.3 , 24.8 , 26.9 , 23.9]
C = np.array(cvalues)
print(cvalues)
print(C)
print("Converting the values into fahrenheit")
print(C * 9 / 5 + 32)
'''


#a = np.arange(1,20,3.5) #equivalent to range() #1 4.5 ... ........ 
#b = np.arange(10,1) #[]
#print(a)
#print(b)

#50 values between 1 and 10

#print(np.linspace(1,10)) # divides the range of 1-10 into 50 parts
#print(np.linspace(1,10,False)) # = []
#print(np.linspace(1,10,100,False))
#print(np.linspace(1,10,100))
#samples, spacing = np.linspace(1, 10, retstep=True)
#print(samples,"--",spacing)
'''
X = np.arange(1,11,1)
Y = np.linspace(1,10,10)
print(X)
print(Y)
print(X+Y)
'''
#-------------------------------------------------------------------
y = np.array(42)
#print(y)
#print("x :",x)
#print("Type of x : ",type(x))
#print("The dim of x is :",np.ndim(x))
x = np.array([1,2,3,4,5,6])
#print("x :",x)
#print("Type of x : ",type(x))
#print("Type of each ele in x , ",x.dtype)
#print("The dim of x is :",np.ndim(x))
B = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8],
               [4.6, 6.7, 7.8]
               ])
A = np.array([
    [[1,2],[2,3],[3,4]],
    [[1,2],[4,5],[6,5]]
])

#print(A)
#print("Type of x : ",type(A))
#print("The dim of x is :",np.ndim(A))
#print(np.shape(A))
#print(np.shape(B))
#print(np.shape(x))
#print(np.shape(y)) #intersting.
#We can use shape to change the shape of an array.
#that must correspond to number of elements in the nparray
#for example.
#B.shape = (3,4)
#print("After changing the shape:",B)
#the method of accessing -> A[1,0] is better than A[1][0]
A = np.array([
    [11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35],
    [41,42,43,44,45],
    [51,52,53,54,55],
])
#print(A[:3,2:])
#print(A[:,:])
X = np.arange(28).reshape(4,7)
#print(X)
#print(X[::2,::3])

##IMPORTANT :
#           getting a patricular set of elements using [] slice operator creates a view so modifying it will modified.
#           But iit is not in the case of list wherin we get the copy of the array.

#np.may__share__memory(np.array_one , np_array_2) -- to check if they share same memory.
#------------------------------------------------------------------------------------------------------------------------------
#Arrays of ones and zeros.

A = np.ones((2,3),dtype=int)
#print(A)
B  = np.zeros((2,4),dtype=int)
#print(B)
#Another interesting way to create an array, so that it should be equivalent to tha array specified.
C = np.ones_like(X)
D = np.zeros_like(X)
#print(X)
#print(C)
#print(D)
#--------------------------------------------------------------------
#Returning Copy of a numpy array

a = np.array([
    [42, 22, 12],
    [44, 53, 66]
],order='F'
)
b = a.copy()
#print(a)
a[1,1] = 200
#print(a)
#print(b)
#----------------------------------------------------------------------
#Creating a identity matrix :
identity_matrix = np.identity(4, dtype=int)
#print(identity_matrix)
#Another function that is used to create indentity matrix 
iden = np.eye(4,5,k=0,dtype=int)
#print(iden)
#----------------------------------------------------------------------
#Question :
print(a[0:1: , ::])