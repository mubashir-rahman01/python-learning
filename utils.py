# Here we will discuss some utility functions that can be used across the project. 
# These functions are designed to simplify common tasks and improve code reusability.

# A lambda function is a small anonymous function that can take any number of arguments, but can return only have one expression. It is often used for short, throwaway functions that are not reused elsewhere in the code.
# The syntax for a lambda function is: lambda arguments: expression

def square(x):
    return x * x

# write this function as a lambda function
square_lambda = lambda x: x * x
print(square_lambda(5))  # Output: 25

items = [
    ("Product1", 10),
    ("Product2", 9),    
    ("Product3", 12),
]

# if we want to sort this functions, we can use the sort method or a lambda function as the key argument to sort the list based on the second element of each tuple (the price).
# using the sort method

def sort_items(item):
    return item[1];

sorted = items.sort(key=sort_items);
# print("Sorted items using sort method: " + str(items));

# same can be written using a lambda function as the key argument to sort the list based on the second element of each tuple (the price).
sorted_values = items.sort(key=lambda item: item[1]);
# print("Sorted items using lambda function: " + str(items));

# a simple lambda function to print age
student ={
    "name": "John",
    "age": 20,
    "grade": "A"
}

print_age = lambda student: student["age"]
print("Student age: " + str(print_age(student)))



students = [{
    "name": "John",
    "age": 20,
    "grade": "A"
},{
    "name": "Jane",
    "age": 22,
    "grade": "B"
},{
    "name": "Jim",
    "age": 21,
    "grade": "C"    
}];

# here we will use lambda function to print the names of students who have grade A or B.
result = lambda student: student["name"] if student["grade"] in ["A", "B"] else None

# print("Students with grade A or B: " + str([result(student) for student in students]))


# map function is used to apply a function to all the items in an iterable (list, tuple etc.) and return a map object (an iterator) of the results. The syntax for the map function is: map(function, iterable)

numbers = [1, 2, 3, 4, 5];
map_obj = map(lambda number: number *2 , numbers); # map object returns an iterator
# an iterable is an object that contains a coutable number of values. Iterator gives you mechanism to iterate through all the values when an object is returned

# for num in map_obj:
#     print("Product:", num);

# filter method works same as map but it only returns the filtered iterator. 
filtered_it = filter(lambda number: number % 2 == 0, numbers)

# for num in filtered_it:
#     print("Even: ", num);

# filter out the product items equal or greator than 10 price
x = filter(lambda item: item[1] >= 10, items);
# for item in x:
#     print("Greator prices:", item);

# we can easily convert iterator to a list, tuple, or a set using constructors
products = list(x);
#print("Product:", products);

# we can show these iteratable values using list comprehension method
# [expression for x in iterables]
# [expression for x in iterables if condition statement else statement]
numbers_ = [x * 2 for x in numbers];
# print("list comp:", numbers_);

# now if we want to print even 
even = [x for x in numbers if x % 2 == 0];
print("Even:", even);

# in else case we slightly adjust the syntax
# [x if condition else y for x in numbers]

# Unpacking operators are similar to spread operator in python. Using unpacking operator, we can combine all the values in a single variable or a list, tuple etc.
def add(a,b,c, d):
    return a + b + c + d; # when a postional parameter is missing, it will give error

# print(add(3,4,5));

def add2(*params):
    return sum(params)

values = [1,2,3]
print("Unpacked:", add2(*values));

# Similarly we can use this for tuples
tuple1 = (1,2,3)
tuple2 = (3,4)

combined = (*tuple1, *tuple2)
print("Combined", combined);

# Similarly dict can also be unpacked
dict1 = {"x": 10}
dict2 = {"y": 12, "z": 12}

combined = {**dict1, "j": 12, **dict2, "z": 15}

print("Combined dict", combined);

