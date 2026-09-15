# numpy is a powerful library for numerical computing in Python. 
# It provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
import numpy as np

array = np.array([1, 2, 3, 4, 5])  # Create a 1D array
second_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Create a 2D array
third_array = np.array([[   [1,2,3], # the elements here are (0,0,0), (0,0,1), (0,0,2)
                            [4,5,6], # the elements here are (0,1,0), (0,1,1), (0,1,2)
                            [7,8,9]  # the elements here are (0,2,0), (0,2,1), (0,2,2)
                        ], 
                        [
                            ['A','B','C'], # these are (1,0,0), (1,0,1), (1,0,2)
                            ['D','E','F'], # these are (1,1,0), (1,1,1), (1,1,2) 
                            ['G','H','I']   # these are (1,2,0), (1,2,1), (1,2,2)
                        ]
                        ])

# check the dimensions of the array
print(array.ndim)  # Output: 1, since it's a 1D array
print(array.shape)  # Output: (5,), since it's a 1D array with 5 elements



# Print 'A1B5D9' from the third_array
print(third_array[1,0,0] + third_array[0,0,0]
      + third_array[1,0,1] + third_array[0, 1, 1]
      + third_array[1,1,0] + third_array[0, 2, 2]
    )