import pandas as pd
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%d.%m.%Y %H:%M:%S')
source_data = pd.read_csv('./csv/export.csv', sep=';')
print('Source_data:\n', source_data.head(), '\n')

source_data = pd.read_csv('./csv/export.csv', sep=';', parse_dates=['IP_PROP5562'], date_parser=dateparse)
print('With date_parse:\n', source_data.head(), '\n')

print(source_data['IP_PROP5562'][4].month, '\n')
print(source_data['IP_PROP5562'][4].date(), '\n')
print(source_data['IP_PROP5562'][4].hour, '\n')
source_data['date'] = source_data['IP_PROP5562'].map(lambda x: x.date())
print(source_data, '\n')

#matplotlib
print(source_data[['IE_ID', 'date']].groupby('date').count().plot(kind='bar', figsize=(13, 8)))


