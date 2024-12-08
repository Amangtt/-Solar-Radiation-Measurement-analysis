import pandas as pd
import math
import numpy as np

df= pd.read_csv('C:/Users/hello/Downloads/data/data/benin-malanville.csv')
number_column= df.drop(['Timestamp', 'Comments'], axis=1)
# Summary statistics
medians= number_column.median()
means=number_column.mean()
stds= number_column.std()

print(f' mean: {means}')
print(f' Median: {medians}')
print(f' Standard deviation: {stds}')

