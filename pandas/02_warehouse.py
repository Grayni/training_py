# sort on sizes by stock of warehouse

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = pd.read_csv('./csv/torg.csv', sep=';').rename(columns={'IP_PROP32': 'size', 'CP_QUANTITY': 'quantity'})

val = data[['size', 'quantity']].groupby('size').sum().sort_values('quantity')
print(val)
