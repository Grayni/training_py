import numpy as np
import pandas as pd

# quantile 75%

df = pd.DataFrame({'name' : ["Alex", "Bob", "Carmen", "Diaz", "Ella","Forman", "Glen"],
                   'age' : [20, 27, 35, 55, 18, 21, 35],
                   'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]})
print(df.describe().loc['count', 'age'])
print(df.describe().loc['75%', 'age'])
