import numpy as np

list = [1,2,3,3]
print("List : ",list)

numpy_array = np.array(list)
print("Array : ",numpy_array)

#for more about NumPy check my GitHub repository
# https://github.com/avarshvir/Python-Learning-Journey/tree/main/python_11_numpy

vector = np.array([1,2,3,4,5])
print("vector : ",vector)
print("no. of elements in vector is : ",len(vector))
print("Dimension of vector is : ",len(vector.shape))
print(vector.shape)

matrices = np.array([[1,2,5],[3,4,4]])
print("matrices : ",matrices)
print("elements : ",matrices.shape)
print("Dimension : ",len(matrices.shape))