# Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations.
#  It is used to make arrays compatible for element-wise operations without the need for explicit replication of data.

# Rules for broadcasting:
# They are equal in shape, OR
# The shape of one of them is 1, OR
# One of the arrays doesn't have that dimension. (e.g an [1D array can be broadcasted to a 2D array by adding a new axis)

import numpy as np
array1 = np.array([[4, 5, 6],
                   [7, 8, 9]
                ])
array2 = np.array([3])
array3 = np.array([[1, 2, 3, 4]])
                #    [4, 5, 6],
                #    [7, 8, 9]
            # ])
print("Shape of 1st:", array1.shape) # output is (2, 3) since it's a 2D array with 2 rows and 3 columns
print("Shape of 2nd:", array2.shape) # output is (1,) since it's a 1D array with 1 element
print("Shape of 3rd:", array3.shape) # output is (1, 3) since it's a 2D array with 1 row and 3 columns
print("Dimension of 1st:", array1.ndim) # output is 2, since it's a 2D array

# according to broadcasting rules, array2 can be broadcasted to the shape of array1. The single element in array2 will be added to each element of array1.
result = array1 + array2
print("Result of broadcasting addition:", result)

product = array1 * array3 # will raise an error since the shapes of array1 and array3 are not compatible for broadcasting. The shape of array1 is (2, 3) and the shape of array3 is (3, 3). The first dimension of array1 is 2, while the first dimension of array3 is 3. Since these dimensions are not equal and neither of them is 1, broadcasting cannot be applied.
print("Result of multiplication:", product)