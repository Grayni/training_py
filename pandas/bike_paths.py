import pandas as pd
from datetime import datetime

# find the day of the week with max middle attendance

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')
data_bike = pd.read_csv('./csv/dataset_345422_14.csv', sep=',', parse_dates=['Date'], date_parser=dateparse)
data_bike['Date'] = data_bike['Date'].dt.dayofweek

data_bike = data_bike.replace({'Date': {
    0: days[0],
    1: days[1],
    2: days[2],
    3: days[3],
    4: days[4],
    5: days[5],
    6: days[6]
}})
days_week = data_bike.groupby('Date').mean().mean(axis=1)
print(days_week[days_week == days_week.max()])
