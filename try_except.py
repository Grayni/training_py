try:
    res = 1 / 0
    f = open('somefile.txt')
except (FileNotFoundError, ZeroDivisionError):
    print('Error')
# except ZeroDivisionError:
#     print('Division zero - error')
# except:
#     print('Error')

print('end program')

