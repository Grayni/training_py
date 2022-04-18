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


def kaprekar(n, base=10):
    num_save = int(convert(n, 10, base)) if base != 10 else n

    num = str(num_save**2)
    num = convert(num, base, 10) if base != 10 else num

    for i in range(1, len(num)//2 + 1):
        if base != 10:
            if int(convert(num[0:i], 10, base)) + int(convert(num[i:], 10, base)) == num_save:
                return True
        else:
            if int(num[0:i]) + int(num[i:]) == n:
                return True
    return False


print(kaprekar('5B', 16))
