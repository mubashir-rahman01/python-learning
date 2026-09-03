# numbers in python are represented as objects of the int, float, and complex classes. The int class represents integers, the float class represents floating-point numbers, and the complex class represents complex numbers.
x = 10; # int
y = 3.14; # float
z = 2 + 3j; # complex

# boolean values are represented as objects of the bool class. The bool class has two values: True and False.
is_active = True; # bool
is_complete = False; # bool

# bool() used to evaluate the truth value of an expression.
print(bool(0)); # False
print(bool(1)); # True
print(bool("Hello")); # True
print(bool("")); # False

# Almost any value is evaluated to True if it has some sort of content.
print(bool("Python")); # True
print(bool([])); # False

# Some values are always False, such as None, False, 0, and empty sequences or collections (e.g., '', (), [], {}).
print(bool(False)); # False
print(bool(None)); # False
print(bool(0)); # False
print(bool("")); # False
print(bool(())); # False, it shows empty tuple
print(bool([])); # False, it shows empty list
print(bool({})); # False, it shows empty dictionary