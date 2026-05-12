graph = {"A":["B", "C"],
         "B":["A", "D"],
         "C":["A", "D"],
         "D":["C", "B"]}

def bfs_recursive(queue, visited_bfs):

    if not queue:
        return

    node = queue.pop(0)

    print(node, end=" ")

    for neighbour in graph[node]:

        if neighbour not in visited_bfs:

            visited_bfs.add(neighbour)

            queue.append(neighbour)

    bfs_recursive(queue, visited_bfs)


visited_bfs = set()

start = 'A'

visited_bfs.add(start)

queue = [start]

bfs_recursive(queue, visited_bfs)

