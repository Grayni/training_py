infinity = float('inf')
graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'fin': 1
    },
    'b': {
        'a': 3,
        'fin': 5
    },
    'fin': {}
}

costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

processed = []


def lower_cost_node(cs):
    lower_cost = infinity
    lower_node = None
    for nd in cs:
        cst = cs[nd]
        if cst < lower_cost and nd not in processed:
            lower_cost = cst
            lower_node = nd
    return lower_node


node = lower_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = lower_cost_node(costs)

print(costs['fin'])
