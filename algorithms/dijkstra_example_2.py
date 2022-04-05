infinity = float('inf')
graph = {
    'start': {
        'a': 5,
        'b': 2
    },
    'a': {
        'c': 4,
        'd': 2
    },
    'b': {
        'a': 8,
        'd': 7
    },
    'c': {
        'fin': 3,
        'd': 6
    },
    'd': {
        'fin': 1
    },
    'fin': {}
}

costs = {
    'a': 5,
    'b': 2,
    'd': infinity,
    'c': infinity,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'c': None,
    'd': None,
    'fin': None
}

processed = []


def min_cost_node(cs):
    lower_cost = infinity
    lower_node = None
    for node in cs:
        cost = cs[node]
        if cost < lower_cost and node not in processed:
            lower_cost = cost
            lower_node = node
    return lower_node


node = min_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = min_cost_node(costs)


print(costs['fin'])
