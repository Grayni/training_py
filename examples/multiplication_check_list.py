def multiplication_check_list(start=10, stop=99):
    value = 0
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            value += 1

    return value


print(multiplication_check_list(96, 97))
