course_name = "Python Programming"
print("Length of course name: " + str(len(course_name)));

print("First character: " + course_name[0]);
print("Last character: " + course_name[-1]);

# Escape sequences are used to introduce special characters or quotation marks in a string.
print("This is a line break\n \"This is a new line\"");

# String concatenation
first_name = "John" 
last_name = "Doe"
full_name = first_name + " " + last_name
# print("Full name: " + full_name);

# There is an another way to concatenate strings using the formatted strings.
print(f"Full name: {first_name} {last_name}");

# string formatting always create a new string and does not modify the original string.

upper = course_name.upper()
print("Uppercase: " + upper);

lower = course_name.lower();    
print("Lowercase: " + lower);

print("Original string: " + course_name);

# search a string 
print("Is 'Python' in course name? " + str("Python" in course_name));

# find the index of a substring in a string
index = course_name.find("Programming");
print("Index of 'Pro': " + str(index));

# slice the charatcres from a string
sliced = course_name[0:6]; # slice from index 0 to 5
print("Sliced string from index 0 to 5: " + sliced);

# if not specified, the slice will go to the end of the string
sliced = course_name[7:]; # slice from index 7 to the end
print("Sliced string from index 7 to the end: " + sliced);

# for negative indexing, the slice will go from the end to the beginning of the string
sliced = course_name[-11:-7]; # slice from index -11 to -8
print("Sliced string with negative indexing: " + sliced);