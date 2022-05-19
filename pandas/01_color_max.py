import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = pd.read_csv('./csv/torg.csv', sep=';')

val = data[['IP_PROP30', 'CP_QUANTITY']].groupby('IP_PROP30').sum()

print(val.sort_values('CP_QUANTITY').iloc[-1])
