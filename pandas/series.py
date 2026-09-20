# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
# It is used for data cleaning, transformation, and analysis. Pandas provides data structures like Series and DataFrame that make it easy to work with structured data.

# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
# It can be thought of as a column in a spreadsheet or a SQL table.

import pandas as pd

column = pd.Series([2,4,6,8,10], index=['a', 'b', 'c', 'd', 'e'])
print(column)
print("\n")

# If we pass a dictionary to the Series constructor, it will create a Series with the keys as the index and the values as the data.
calories = pd.Series({'apple': 52, 'banana': 89, 'orange': 47})
calories["banana"] = 90  # Update the value for 'banana'

print(calories)
print("\n")
print("Calory of apple:", calories.loc['apple'])  # Accessing the value for 'apple'
print("Calory of 2nd:", calories.iloc[1])  # Accessing the first element using iloc

# Calories can be filtered out as well
print("\n")
high_calories = calories[calories > 50]
print("High calorie fruits:\n", high_calories)