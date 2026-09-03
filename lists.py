# a list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# lists can contains different types of data and it allows duplicate members.

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"];
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
combined = [fruits, numbers];

# print("Fruits: " + str(fruits));
# print("Numbers: " + str(numbers));
# print("Combined: " + str(combined));

# lists can also be created using the list() constructor.
fruits_list = list(("apple", "banana", "cherry", "date"));
# print("Fruits list: " + str(fruits_list));


# list can be accessed using index, slicing, and negative indexing.
# print("First fruit: " + fruits[0]);
# print("First three fruits: " + str(fruits[0:3])); # element at 3 is not included in the slice.
# print("Last fruit: " + fruits[-1]);

# if no index is specified, the slice will go to the end of the list.
# print("Fruits from index 2 to 5: " + str(fruits[2:]));

# if any item exist in the list, it will return True, otherwise False.
# if "banana" in fruits:
    # print("Banana is in the list of fruits");
    
# another method to check if an item exist in the list is using the index() method, which returns the index of the first occurrence of the item in the list. If the item does not exist, it will raise a ValueError.
# print("Index of 'banana': " + str(fruits.index("banana")));
    
# these elements are accesable and mutable, so we can change the value of an element in the list.
fruits[1] = "blueberry";
# print("Fruits after changing the second element: \n" + str(fruits));

fruit1, fruit2, fruit3 = fruits[0:3]; # unpacking the list into variables
# print("Unpacked fruits: \n" + fruit1 + ", " + fruit2 + ", " + fruit3);

# insert, append and extend are used to add elements to a list. 
# Insert adds an element at a specific index, append adds an element at the end of the list, 
# and extend adds multiple elements to the end of the list.

fruits.insert(1, "coconut"); # insert "coconut" at index 1
fruits.append("dragonfruit"); # append "dragonfruit" at the end of the list
fruits.extend(["elderberry", "fig", "grape"]); # extend the list with multiple elements
print("Fruits after adding elements: \n" + str(fruits));

# pop, del, remove and clear are used to remove elements from a list.
fruits.pop(1); # remove the element at index 1
print("Fruits after removing element at index 1: \n" + str(fruits));

fruits.remove("fig"); # remove the first occurrence of "fig"
print("Fruits after removing 'fig': \n" + str(fruits));

del fruits[0]; # delete the element at index 0
print("Fruits after deleting element at index 0: \n" + str(fruits));

fruits.clear(); # remove all elements from the list
print("Fruits after clearing the list: \n" + str(fruits));