#!/usr/bin/env python
import numpy as np
import pandas as pd


# Create a list of lists
a = [['10', '1.2', '4.2'], ['15', '70', '0.03'], ['8', '5', '0']]
# Make a dataframe from our list of list with column names
df = pd.DataFrame(a, columns=['one', 'two', 'three'])
print(df)

# Which rows in column one are greater than or equal to column two
print(np.where(df['one'] >= df['two']))
# Which rows are column one & two equal
print(np.where(df['one'] == df['two']))
# Which rows are not equal in columns one & two 
print(np.where(df['one'] != df['two']))
