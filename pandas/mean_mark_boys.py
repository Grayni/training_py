import pandas as pd

# find males with education as education parents of females with max mean score

data_students = pd.read_csv('csv/students_performance.csv', sep=',')
data_mean = data_students.groupby(['gender', 'parental level of education']).mean().mean(axis=1)
education = data_mean[data_mean == data_mean.filter(like='female').max()].index[0][1]
print(data_mean.filter(like=education)['male'].values[0].round(1))