import pandas as pd
# max median value of 'reading score' / 'gender' and 'race/ethnicity'
data_students = pd.read_csv('csv/students_performance.csv', sep=',')
data_students = data_students.groupby(['race/ethnicity', 'gender']).median().max()['reading score']

print(data_students)


