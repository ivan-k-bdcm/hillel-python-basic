'''
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}
'''

infinity = float("inf")


#graph = {"start": {"a": 6, "b": "2"}, "a": {"fin": 1}, "b": {"a": 3, "fin": 5}, "fin": {}}
#costs = {"a": 6, "b": 2, "fin": infinity}
#parents = {"a": "start", "b": "start", "fin": None}


graph = {
        "start": {"a": 5, "b": 2},
        "a": {"c": 4, "d": 2},
        "b": {"a": 8, "d": 7},
        "c": {"d": 6, "fin": 3},
        "d": {"fin": 1},
        "fin": {}
    }
costs = {
        "a": 5,
        "b": 2,
        "c": infinity,
        "d": infinity,
        "fin": infinity
}

parents = {
        "a": "start",
        "b": "start",
        "c": None,
        "d": None,
        "fin": None
}
proccessed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in proccessed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


def deikstra_alg(graph, costs, parents):
    global proccessed
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        proccessed.append(node)
        node = find_lowest_cost_node(costs)
    return costs["fin"]


print(f"Smallest-weight way cost: {deikstra_alg(graph, costs, parents)}")


def opti_way(parents, value):
    if value == "start":
        return ""
    elif value == "fin":
        value_fin = value
        value = parents[value]
        return opti_way(parents, value) + value + " -> " + value_fin
    else:
        value = parents[value]
        return opti_way(parents, value) + value + " -> "

print(opti_way(parents, "fin"))