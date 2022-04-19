def multiplication_check_list(start=10, stop=99, length_check=True):
    m, n = [0, 0]
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            val_X = 100 - x
            val_Y = 100 - y
            sub = 100 - (val_X + val_Y)
            mul = val_X * val_Y

            if length_check:
                if mul < 10:
                    if int(f'{sub}0{mul}') == x * y:
                        n += 1
                    else:
                        m += 1
                else:
                    if int(f'{sub}{mul}') == x * y:
                        n += 1
                    else:
                        m += 1
            else:
                if int(f'{sub}{mul}') == x * y:
                    n += 1
                else:
                    m += 1

    print('Правильных результатов:', n)
    print('Неправильных результатов:', m)


print(multiplication_check_list())
