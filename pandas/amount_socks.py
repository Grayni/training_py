import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

products = pd.read_csv('./csv/products.csv', sep=';')
orders = pd.read_csv('./csv/orders.csv', sep=';')

# print(products)
# print(orders)

table = pd.merge(products, orders, how='inner', left_on=('Product_ID'), right_on=('ID товара'))
table_socks = table[table['Name'].str.contains('Носки')]
table_socks_paid = table_socks[table_socks['Статус'].str.contains('Оплачен')]
table_socks_paid['Sum'] = table_socks_paid['Price'] * table_socks_paid['Количество']
print(table_socks_paid['Sum'].sum())
