# matrix operations are an important part of linear algebra and are widely used in various fields such as computer graphics, physics simulations, and machine learning. 
# Numpy provides a convenient way to perform matrix operations using its built-in functions and methods.

# Dot product of a matrix

import numpy as np
a = np.array([1, 2])
b = np.array([3,4])
result = np.dot(a, b) # 1* 3 + 2 * 4 = 11
print("Dot product of 1D matrix:", result)

# 2D matrix dot product is similar to the 1D matrix dot product, but it involves multiplying the rows of the first matrix by the columns of the second matrix. 
array1 = np.array([[1, 2], 
                   [3, 4]
                ])
array2 = np.array([[5, 6], 
                   [7, 8]
                ])
result = array1 @ array2 # 1*5 + 2*7 = 19, 1*6 + 2*8 = 22, 3*5 + 4*7 = 43, 3*6 + 4*8 = 50
print("Dot product of 2D matrix:", result) # output: [[19 22], 
                                           #          [43 50]]

# Transpose of a matrix is achieve by changing the rows of the matrix to columns and the columns to rows.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]
                ])
transposed_matrix = matrix.transpose()
print("Original matrix:\n", matrix)
print("Transposed matrix:\n", transposed_matrix)

# Array and matrix multiplication is different. In array multiplication, the corresponding elements of the two arrays are multiplied together, 
# while in matrix multiplication, the rows of the first matrix are multiplied by the columns of the second matrix.

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Array multiply:", a * b) # output: [4 10 18]
print("Matrix multiply:", a @ b) # output: 32
                                            