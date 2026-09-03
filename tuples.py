# a tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
fruits = ("apple", "banana", "cherry", "date", "elderberry")

print("Fruits: " + str(fruits));

# tuple is indexed, meaning that each element in a tuple has a unique index that can be used to access it. The first element has an index of 0, the second element has an index of 1, and so on. We can also use negative indexing to access elements from the end of the tuple, where the last element has an index of -1, the second last element has an index of -2, and so on.
print("First fruit: " + fruits[0]);
print("Last fruit: " + fruits[-1]);

# type of a tuple is tuple if the tuple is empty, it will return an empty tuple.
empty_tuple = ();
print("Type of empty tuple: " + str(type(empty_tuple)));

print("Type of fruits tuple: " + str(type(fruits)));

# once initialized, the elements of a tuple cannot be changed, added, or removed. 
# However, if the tuple contains mutable objects like lists, those objects can be modified.

# fruits[0] = "blueberry"; # This will raise an error because tuples are immutable.

# the order of tuple also cannot be changed.
# fruits[0], fruits[1] = fruits[1], fruits[0]

# when a function returns multiple values, it actually returns a tuple containing those values. For example, the divmod() function takes two numbers and returns a tuple containing the quotient and remainder of their division.

result = divmod(10, 3);
print("Result of divmod(10, 3): " + str(result));

# tuples are mostly used to store related pieces of information, such as the coordinates of a point in 2D space (x, y), or the RGB values of a color (r, g, b).
coordinates = (10, 20)
print("Coordinates: " + str(coordinates));

GREEN = (0, 255, 0);
BLUE = (0, 0, 255);
RED = (255, 0, 0);
print("GREEN: " + str(GREEN));
print("BLUE: " + str(BLUE));
print("RED: " + str(RED));




