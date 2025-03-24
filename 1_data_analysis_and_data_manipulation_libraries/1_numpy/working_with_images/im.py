import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.random.rand(3,3)
arr3 = np.zeros((4,4))

np.save('arr1.npy',arr1)

loaded_array = np.load('arr1.npy')
print(loaded_array)