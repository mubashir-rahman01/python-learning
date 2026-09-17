# We have studies aggregate functions, and we have studied how to use them on arrays. They used to summarize the data in an array. 

# Universal functions (ufuncs) are a set of functions that operate on ndarrays in an element-by-element fashion, supporting array broadcasting, type casting, and several other standard features.
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
c = np.array([1, 4, 9, 16, 25])

print("Addition: ", np.add(a, b))  # Output: [ 7  9 11 13 15]
print("Subtraction: ", np.subtract(a, b))  # Output: [-5 -5 -5 -5 -5]
print("Multiplication: ", np.multiply(a, b))  # Output: [ 6 14 24 36 50]
print("Division: ", np.divide(a, b))  # Output: [0.16666667 0.28571429 0.375 0.44444444 0.5]
print("Power: ", np.power(a, 2))  # Output: [ 1  4  9 16 25]
print("Modulus: ", np.mod(b, a))  # Output: [0 1 2 1 0]
print("Square root: ", np.sqrt(c))  # Output: [1. 2. 3. 4. 5.]

# Similarly, we can use other universal functions like np.sin(), np.cos(), np.tan(), np.exp(), np.log(), etc. to perform element-wise operations on arrays.