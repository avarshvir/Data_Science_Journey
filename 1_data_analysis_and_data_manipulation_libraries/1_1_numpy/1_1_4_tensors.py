import numpy as np
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor_3d)
print(tensor_3d.T)


# Create a 4D tensor (batch_size, height, width, channels)
tensor_4d = np.random.rand(32, 64, 64, 3)
print(tensor_4d)
# This tensor represents a batch of 32 images, each with a size of 64x64 pixels and 3 color channels.