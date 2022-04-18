def convert(num, to_base=10, from_base=10):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = str(num)[::-1]
    value_dec = 0

    # value from_base => decimal
    for i in range(len(num)):
        value_dec += from_base**i * alphabet.index(num[i])

    # value to_base
    value_to = ''

    while value_dec != 0:
        value_to += alphabet[value_dec % to_base]
        value_dec = value_dec // to_base
    return value_to[::-1]


numb = 'B05'
print(convert(42))
