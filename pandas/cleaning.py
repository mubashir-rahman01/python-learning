# Most of the time when we read data from files, it can be wrong, null or N/A
# To avoid this we have to correct the data

import pandas as pd;

df = pd.read_csv("pokemon_list.csv")

# set a particular column value
# df.loc[7, 'hp'] = 90

# drop a column
df = df.drop(["id"], axis=1)

# Drop all rows with type2="N/A"
#df = df.dropna(subset=["type_2"]) # returns all rows without n/a

# Fill all rows with n/a to none
# df = df.fillna({"type_2": "none"}, inplace=True)

# Remove all duplicate value from the data
# df = df.drop_duplicates(inplace=True)

print(df)