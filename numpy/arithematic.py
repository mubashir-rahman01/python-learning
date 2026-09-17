## Numpy is simple for scalar operations, but it can be a bit tricky when it comes to multi-dimensional arrays. 
## Scalar is an operation perform between an array and a single value. For example, adding a number 5 to an array will add that number to each element of the array.
## While the vector is an operation between two arrays of the same shape. For example, adding two arrays of the same shape will add the corresponding elements of the arrays together.

import numpy as np
array = np.array([1, 2, 3, 4, 5])  # Create a 1D array
second_array = np.array([4, 5, 6]) 
third_array = np.array([7, 8, 9])
scores = np.array([90, 100, 85, 66, 32])  # Create a 2D array

sum = array + 10
diff = array - 2
product = array * 3
quotient = array / 2
power = array ** 2

print("Original array:", array)
print("Sum with 10:", sum)
print("Difference with 2:", diff)
print("Product with 3:", product)
print("Quotient with 2:", quotient)
print("Array with power of 2:", power)

# Now the vector operations will be applied to the second_array and third_array. The two arrays must have the same shape for the operations to be valid.
vector_sum = second_array + third_array
vector_diff = second_array - third_array
vector_product = second_array * third_array
vector_quotient = second_array / third_array

print("Vector sum:", vector_sum)
print("Vector difference:", vector_diff)
print("Vector product:", vector_product)
print("Vector quotient:", vector_quotient)


# Comparison operations can also be performed on arrays. These operations will return a boolean array indicating whether each element of the first array is greater than, less than, or equal to the corresponding element of the second array.
# Comparison operations can be scalar and vector operations. For example, comparing an array with a scalar will return a boolean array indicating whether each element of the array is greater than, less than, or equal to the scalar value. 
# Similarly, comparing two arrays of the same shape will return a boolean array indicating whether each element of the first array is greater than, less than, or equal to the corresponding element of the second array.

# Let's check whetther the scores are greater than 50 or not.
passing_students = scores > 50
print("Students passed the exam:", passing_students)


# Filtering is a powerful feature of numpy that allows you to select elements from an array based on certain conditions. 
# For example, you can filter an array to get only the elements that are greater than a certain value, or only the elements that are even numbers.

ages = np.array([[18, 22, 25, 30, 35], 
                 [40, 45, 50, 55, 60], 
                 [65, 70, 75, 80, 99]
                ]);

teenagers = ages[(ages >= 13) & (ages <= 19)];
adults = ages[(ages >= 20) & (ages <= 64)];
# seniors = ages[(ages >= 65)];

print("Teenagers:", teenagers)
print("Adults:", adults)


# If we want to preserve the original shape of the array while filtering, we can use the np.where() function. This function returns the indices of the elements that satisfy the condition, and we can use these indices to create a new array with the same shape as the original array.
# Syntax: np.where(condition, x, y) - This function returns an array with elements from x where the condition is True, and elements from y where the condition is False.
seniors = np.where(ages >= 65, ages, -1)  # Replace elements that do not satisfy the condition with 0
print("Seniors:", seniors)