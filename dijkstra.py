#dijkstra

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

dist = {}
visited = []

for node in graph:
    dist[node] = 999

dist['A'] = 0

while len(visited) < len(graph):

    min_node = None

    for node in graph:
        if node not in visited:

            if min_node is None or dist[node] < dist[min_node]:
                min_node = node

    visited.append(min_node)

    for neighbour in graph[min_node]:

        new_dist = dist[min_node] + graph[min_node][neighbour]

        if new_dist < dist[neighbour]:
            dist[neighbour] = new_dist

print("Shortest Distances:")
print(dist)