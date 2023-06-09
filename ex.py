import pandas as pd
import time
import numpy as np

# Ch4
from pandas import Series

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
first = pd.Series([1, 5, 10, 12], dtype='int8')
print(f'Adding the series to itself \n{first + first}')
print(f'Using the add method on the series to add to itself \n{first.add(first)}')
print(f'Show the series unadulterated: \n{first}')

# Ch7
another = pd.Series([1, 5, 10, 12, 5, None])
print(f'count of non null entries: {another.count()}')
print(f'total count of items (including Nones) {another.size}')
print(f'total unique count of items (excludes Nones): {another.nunique()}')
print(f'find the mean of the series: {another.mean()}')
print(f'find the max of the series: {another.max()}')
print(f'use agg method to find all of the above: \n{another.agg(["mean", "max"])}')

# Ch8
ch8 = pd.Series([1, 5, 10, 12, 5], dtype="Int64")
print(f'memory size of ch8: {ch8.nbytes}')
convert = ch8.astype("uint8")
print(f'memory size of convert: {convert.nbytes}')

print(f'converting uint8: \n{convert}')
print(f'printing out int64 \n{np.iinfo("int64")}')
print(f'printing out uint8 \n{np.iinfo("uint8")}')
print(f'printing out float16 \n{np.finfo("float16")}')
print(f'printing out float64 \n{np.finfo("float64")}')

ch8_string = pd.Series(
    ["one string", "two string", "red string", "blue string", "one string", "two string", "red string", "blue string",
     "one string", "two string", "red string", "blue string"])
print(f'memory size of ch8_string: {ch8_string.nbytes}')
print(f'memory size of ch8_string_convert: {ch8_string.astype("category").nbytes}')

city_type = pd.CategoricalDtype(categories=pd.Series(sorted(set(ch8_string))), ordered=True)
print(f'memory size of ch8_string_convert with order: {ch8_string.astype(city_type).nbytes}')

# Ch9
# Create series from numeric column that has the value of 'high' if it is equal
# to or above the mean and 'low' if it is below the mean using .apply()
the_series = pd.Series(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, None, None])


def displayHigh(val):
    if (val >= the_series.mean()):
        return 'High'
    return 'Low'


start_time = time.time()
print(
    f'Display High if val is gte mean, display Low if val is lt mean, using apply \n{the_series.apply(displayHigh)}')
print("--- %s seconds ---" % (time.time() - start_time))

start_time2 = time.time()
high = the_series.where(lambda x: x >= the_series.mean())
low = the_series.where(lambda x: x < the_series.mean())
print(
    f'Display High if val is gte mean, display Low if val is lt mean, using select/where \n{np.select([the_series.isin(high), the_series.isin(low)], ["High", "Low"], "Other")}')
print("--- %s seconds ---" % (time.time() - start_time2))

print(f'fill in the missing values with the mean: \n{the_series.fillna(the_series.mean())}')
print(
    f'Clip from the 10th quantile to the 90th quantile: \n{the_series.clip(the_series.quantile(.1), the_series.clip(the_series.quantile(.9)))}')

top_5 = the_series.value_counts().index[:5]
print(f'Show the top 5 in the series {top_5}')
print(f'Show series, but replace anything that is not in the top 5 {the_series.where(the_series.isin(top_5), "Other")}')

top_10 = the_series.value_counts().index[:10]
print(f'Show the top 10 in the series {top_10}')
print(
    f'Show series, but replace anything that is not in the top 10 {the_series.where(the_series.isin(top_10), "Other")}')


def top_n(a_series: Series, top: int) -> Series:
    return a_series.value_counts().index[:top]


print(f'print top n {top_n(the_series, 12)}')

print(f'print bins of equal width {pd.cut(the_series, 5)}')
print(f'print bins of equal quantity sizes {pd.cut(the_series, 5)}')


# ch10
print(f'inspect {the_series}')
print(f'change the index labels from dict {the_series.rename(the_series.to_dict())}')
print(f'set index to monotonic increasing {the_series.reset_index()}')
# print(f'change the index labels from dict {the_series.rename(the_series.to_dict()).rename()}')
