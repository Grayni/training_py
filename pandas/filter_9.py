
import numpy as np
import pandas as pd

# mean ages

df = pd.DataFrame({
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7],
    'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf'],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no']},
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
)

group_by = "animal"

gr = df[group_by].value_counts()
print(gr)

