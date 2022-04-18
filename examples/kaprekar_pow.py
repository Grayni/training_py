def kaprekar(n):
    num = str(n**2)

    for i in range(1, len(num)//2 + 1):
        if int(num[0:i]) + int(num[i:]) == n:
            return True

    return False


numb = 1000

print(kaprekar(numb))

