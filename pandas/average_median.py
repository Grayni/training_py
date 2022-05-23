import pandas as pd
# find every club where mean wage == median wage

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data_football = pd.read_csv('./csv/football_players.csv', sep=',')
median_wage = data_football.groupby('Club').median()['Wage']
mean_wage = data_football.groupby('Club').mean()['Wage']

print(mean_wage[median_wage == mean_wage].shape[0])
