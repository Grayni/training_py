def wisdom_multiplication(x, y, length_check=True):
    val_X = 100 - x
    val_Y = 100 - y

    sub = 100 - (val_X + val_Y)
    mul = val_X * val_Y

    if length_check:
        return int(f'{sub}{"0" if mul < 10 else ""}{mul}')
    else:
        return int(f'{sub}{mul}')


print(wisdom_multiplication(99, 99))