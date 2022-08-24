from random import choice


def monty_hall_problem(choice_door, agreement):
    doors = [1, 2, 3]
    win_door = choice(doors)

    # Choose list[0], even len(list) == 2. Because, important to choose any other door.
    other_door = list(filter(lambda x: x not in [choice_door, win_door], doors))[0]

    if agreement:
        other_door = list(filter(lambda x: x not in [choice_door, other_door], doors))[0]
        return other_door == win_door

    return choice_door == win_door


def Tester(is_agree, counter=0):
    for i in range(10000):
        if monty_hall_problem(2, is_agree):
            counter += 1

    print(f'{is_agree} coef: {counter / 10000}')


Tester(True)   # True coef: 0.6644
Tester(False)  # False coef: 0.3371
