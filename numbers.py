
import math;
print(round(2.9));
print(abs(-5));
print(int(math.sqrt(16)));


# Type conversion
x = input("Enter a number: ");
# y = x + 5;

# print("Value of y: " + str(y)); #gives an error because x is a string and cannot be added to an integer. To fix this, we need to convert x to an integer before adding 5.
y = int(x) + 5;
print("Value of y: " + str(y));