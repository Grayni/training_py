
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf', 'Muhtar'],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
)

filter_names = ["animal", "age"]
filter_values = ["cat", 3]

print(df.loc[df[filter_names[0]] == filter_values[0]].loc[df[filter_names[1]] < filter_values[1]])


# variant 2

names = df[filter_names[0]] == filter_values[0]
values = df[filter_names[1]] < filter_values[1]
print(df[names & values])
