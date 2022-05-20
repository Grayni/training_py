import numpy as np
import pandas as pd

# find pink XL sum

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

data = pd.read_csv('./csv/dataset_345422_8.csv', sep=';')

data = data.rename(columns={'IP_PROP30': 'color', 'IP_PROP32': 'size', 'CP_QUANTITY': 'quantity', 'CR_PRICE_1_USD': 'price'})

data = data.groupby(['color', 'size'])


for i in data:
    if i[0] == ('pink', 'XL'):
        print(sum(i[1]['price'] * i[1]['quantity']))
