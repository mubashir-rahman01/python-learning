# An array is similar to list but it is more efficient and contain only elements of the speicifed data type.
from array import array
numbers = array("i", [1,2,3,4,5])

# if we try to assign another data type value in this array, it will give an error
numbers[2] = 5.6

print("numbers", numbers)