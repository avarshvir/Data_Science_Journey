import numpy as np

li1 = [1,2,3,4]
li2 = [1,2,3,4]

arr1 = np.array(li1)
arr2 = np.array(li2)

print("Array 1D: ",arr1)
print("No. of Elements in 1d Array:",len(arr1))
print("Dimenstion of array:",arr1.shape)

print("----------------------------------------------------------")
print("Operations")
#addition
result_addition = arr1 + arr2
print("Addition : ",result_addition)

#subtraction
result_subtraction = arr1 - arr2
print("Subtraction : ",result_subtraction)

#multiplication
result_multiplication = arr1 * arr2
print("Multiplication : ",result_multiplication)

#division
result_division = arr1/arr2
print("Division : ",result_division)

#modulus
result_modulus = arr1 % arr2
print("Modulus : ",result_modulus)

#dot product
dot_product = np.dot(arr1, arr2)
print("Dot Product : ",dot_product)