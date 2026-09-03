# Python dictionaries are ordered collections of key-value pairs. Each key in a dictionary is unique and maps to a specific value. 
# Dictionaries are mutable, meaning you can change their contents after creation.

# A dictionary is similar to javascript object, where keys are strings and values can be any data type.

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
}

print("Car: " + str(car));

# over-writing a value for an existing key will update the value associated with that key.
car["year"] = 2021;

print("Updated Car: " + str(car));

# if there are multiple keys with the same name, the last one will be used.
new_car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2021,
    "model": "Corolla"
};
print("New Car: " + str(new_car));

# collection is unindexed, so we cannot access items in a dictionary by referring to an index or a key. However, we can loop through the dictionary items using a for loop.

#print("Car model: " + car[2]); # this will raise an error because dictionaries are unindexed and do not support item assignment.
print("Car model: " + car["model"]); # this will print the value associated with the key "model".

# As of Python 3.7, dictionaries maintain the order of items as they were added. This means that when you iterate over a dictionary, the items will be returned in the order they were inserted.

for key, value in car.items():
    print(f"{key}: {value}");

# We can also create dictionaries using the dict() constructor, which takes a list of tuples as an argument. Each tuple should contain a key-value pair.
person = dict(name = "Alice", age = 30, city = "New York");
print("Person: " + str(person));

# keys() method returns a view object that displays a list of all the keys in the dictionary.
# values() method returns a view object that displays a list of all the values in the dictionary.
print("Keys: " + str(person.keys()));
print("Values: " + str(person.values()));

# If you want to check if a specific key exists in the dictionary, you can use the in keyword.
if "name" in person:
    print("Name is in the person dictionary");
    
    
# item values can be updated using the direct assignment method, or using the update() method. The update() method can also be used to add new key-value pairs to the dictionary.
person["age"] = 31; # direct assignment method
person.update({"city": "Los Angeles"}); # update() method
print("Updated Person: " + str(person));

#update method can also be used to add new key-value pairs to the dictionary.
person.update({"country": "USA"}); # adding new key-value pair

# pop() method removes the item with the specified key and returns its value. If the key does not exist, it raises a KeyError.
removed_value = person.pop("city");

# popitem() method removes the last inserted key-value pair from the dictionary and returns it as a tuple. If the dictionary is empty, it raises a KeyError.
last_item = person.popitem();   

print("Removed value: " + str(removed_value));
print("Last item removed: " + str(last_item));
print("Person after removals: " + str(person));

# values in dictionary can be copied using copy() method or using the dict() constructor. The copy() method creates a shallow copy of the dictionary, while the dict() constructor creates a new dictionary with the same key-value pairs.
person_copy = person.copy();
print("Person copy: " + str(person_copy));

constructed_person = dict(person);
print("Constructed person: " + str(constructed_person));