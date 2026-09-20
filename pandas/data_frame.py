# A data-frame is a two-dimensional labeled data structure with columns of potentially different types. 
# It can be thought of as a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.


import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"]);

# print(df);

# Locate a row by label using loc
# print(df.loc["Employee 2"])

# Add a new column in the table
reg_no = [1211, 1234, 1254, 1267];
df["Reg No"] = reg_no

# Add a new row in the data-frame
new_row = pd.DataFrame([{
    'Name': 'James',
    'Age': 25,
    'City': 'Jamaica',
    "Reg No": 1654
}], index=["Employee 5"])
pd.concat([df, new_row])


# Reading JSON and CSV data from files

df = pd.read_csv("pokemon_list.csv", index_col="name")
# print(df) 
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

# Reading data from columns
# print(df["type"])

# Reading data from rows
print("\n")

# try:
#     print(df.loc["Charizard", ["type"]]) # passing a python list of all the columns will print those only
# except:
#     print("Value not found! ")

# Print every second row
# print(df.iloc[0:10:2]) # every second row from zero to ten

# print(df)

# Filtering in dataframe is same as numpy
# print(df[df["type"] == "Fire"])
# print(df[(df["id"] > 10) & (df["id"] <= 15)])

# Data aggregation in pandas is same as numpy
