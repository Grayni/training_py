def permutations(elements):
    if len(elements) <= 1:
        yield elements
        return

    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
           yield perm[:i] + elements[0:1] + perm[i:]


def brackets_round(arr):
    return list(map(lambda element: '(' + element + ')', arr))


def brackets_in(n):
    return (n-1) * ['(', ')']


n = 3
arr = set([''.join(element) for element in permutations(brackets_in(n))])

print(sorted(brackets_round(arr)))
