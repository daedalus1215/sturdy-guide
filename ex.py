import pandas as pd
import numpy as np

# Ch4
temps = pd.Series([145, 142, 38, 13, 12, 15, 52])
# Filter out anything below the mean
print(temps[temps > np.mean(temps)])
# Not sorted category
colors = pd.Series(["green", "red", "blue", "purple"], dtype='category')
print(colors.cat.ordered)

# Ch5
# Sorted category
size_type = pd.api.types.CategoricalDtype(categories=["green", "red", "blue", "purple"], ordered=True)
s3 = colors.astype(size_type)
print(s3)
print(s3.cat.ordered)

# Ch6
# Add a numeric series to itself
first= pd.Series([1, 5, 10, 12], dtype='int8')
print(f'Adding the series to itself \n{first + first}')
print(f'Using the add method on the series to add to itself \n{first.add(first)}')
print(f'Show the series unadulterated: \n{first}')

# Ch7
another = pd.Series([1, 5, 10, 12,5, None])
print(f'count of non null entries: {another.count()}')
print(f'total count of items (including Nones) {another.size}')
print(f'total unique count of items (excludes Nones): {another.nunique()}')
print(f'find the mean of the series: {another.mean()}')
print(f'find the max of the series: {another.max()}')
print(f'use agg method to find all of the above: \n{another.agg(["mean", "max"])}')

# Ch8