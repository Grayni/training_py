from collections import deque

#  ~/pictures/graphs_numbers.jpg
graph = {
    0: [1, 2, 3, 4, 5, 6],
    1: [7, 8],
    2: [9, 10, 11],
    3: [12, 13],
    4: [14, 15, 16, 3],
    5: [16, 17, 18],
    6: [19],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [21],
    18: [],
    19: [20],
    20: [],
    21: []
}


def find_x2(value):
    search_number = deque()
    search_number += graph[0]
    former = []
    while search_number:
        number = search_number.popleft()
        if number in former:
            continue

        if check_number(number, value):
            return f'Number {number} found!'
        else:
            former.append(number)
            search_number += graph[number]
    return f'{value}x2 not found!'


def check_number(num, val):
    return val * 2 == num


print(find_x2(2))
print(find_x2(14))

