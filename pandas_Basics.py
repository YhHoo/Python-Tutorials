import pandas as pd
import numpy as np

# initiating datasets
attendance = {'Day': [1, 2, 3, 4, 5, 6],
              'Absent': [0, 0, 1, 2, 3, 4],
              'Weather': [1, 1, 1, 0, 0, 0]}

# create DataFrame object 
df = pd.DataFrame(attendance)

# set the Day as index 
df.set_index('Day', inplace=True)
# print entire dataframe in table
print(df, "\n\n")
# convert the column of Weather to a list
print(df.Weather.tolist())





