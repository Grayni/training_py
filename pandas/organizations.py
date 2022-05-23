import pandas as pd
# find value organizations where project sum FileSize > mean FileSize all projects
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data_org = pd.read_csv('./csv/dataset_file_storage.csv', sep=';')

# file size of projects
project_sum = data_org[['ProjectID', 'FileSize']].groupby(['ProjectID']).sum()

# mean value (global)
mean_value = project_sum.mean()
mean_company_project = pd.DataFrame(data_org[['CompanyID', 'ProjectID', 'FileSize']].groupby(['CompanyID', 'ProjectID']).sum())
m = mean_company_project[mean_company_project > mean_value]
m = m[m['FileSize'].notna()]

print(m.groupby(level=0).head(1).shape[0])



