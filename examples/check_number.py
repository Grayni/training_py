values = ['5', '3.4', '3.4.1', '1a', 'a3', '-123', '-5.321']

for value in values:
    try:
        float(value)
        print('Correct')
    except ValueError:
        print('Wrong')
