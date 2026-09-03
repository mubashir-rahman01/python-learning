# set is an unordered and unindexed collection of unique elements. It is mutable, but unordered and does not allow duplicate members. Sets are useful when you want to store a collection of unique items and perform operations like union, intersection, and difference.
# In Python, sets are written with curly brackets.

fruits = {"apple", "banana", "cherry", "date", "elderberry"}
print("Fruits: " + str(fruits));

# doesn't allow duplicate members, so if we try to add a duplicate member, it will be ignored.
fruits.add("fig");
fruits.add("apple"); # this will be ignored because "apple" is already in the set
print("Fruits after adding 'fig' and 'apple': " + str(fruits));

# to remove an element from a set, we can use the remove() or discard() method. The remove() method will raise a KeyError if the element is not found, while the discard() method will not raise an error.
if "banana" in fruits:
    fruits.remove("banana");
    print("Fruits after removing 'banana:  \n " + str(fruits));


# the discard() method will not raise an error if the element is not found.
fruits.discard("grape"); # this will not raise an error because "grape" is not in the set
print("Fruits after discarding 'grape': " + str(fruits));

# in set, True and 1 are considered the same, and False and 0 are considered the same. So if we try to add both True and 1 to a set, only one of them will be added.
this_set = {"apple", "banana", "cherry", True, 1, False, 0};
print("This set: " + str(this_set)); # this will only contain one of True and 1, and one of False and 0

# since set are unindexed, we cannot access items in a set by referring to an index or a key. However, we can loop through the set items using a for loop.
new_set = {"apple", "banana", "cherry", "date", "elderberry"};
#new_set[1] = "fig"; # this will raise an error because sets are unindexed and do not support item assignment.

# right way to loop through a set
for fruit in new_set:
    print(f"Fruit: {fruit}");
    
# frozenset is a built-in set type that is immutable, meaning that its elements cannot be changed after it is created. It is similar to a regular set, but it cannot be modified. 
# Frozensets are useful when you want to create a set that should not be changed, such as a set of constants or a set of unique values that should not be modified.
frozen_fruits = frozenset({"apple", "banana", "cherry", "grapes", "elderberry"});
print("Frozen fruits: " + str(frozen_fruits));