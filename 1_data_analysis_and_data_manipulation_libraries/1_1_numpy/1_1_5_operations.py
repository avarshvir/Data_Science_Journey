import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr3= np.array([[1,2],[3,4]])

print("Addition : ",arr1+arr2)
print("Subtraction : ",arr1-arr2)
print("Simple Multiplication : ",arr1*arr2)
print("Division : ",arr2/arr1)
print("Multiplication : ",arr1@arr2)
print("Transpose : ",arr3.T)
print("Slicing : ",arr1[:3])
print("Slicing 2 : ",arr2[:])