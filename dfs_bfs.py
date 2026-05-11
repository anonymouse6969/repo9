graph = {"A":["B", "C"],
         "B":["A", "D"],
         "C":["A", "D"],
         "D":["C", "B"]}

#dfs
#recursion is used here in dfs instead of stack
visited_dfs = set()
def dfs(node):
    if node not in visited_dfs:
        print(node, end=" ")
        visited_dfs.add(node)

        for neighbour in graph[node]:
            dfs(neighbour)


#bfs
def bfs(start):
    visited_bfs = set()
    queue = []

    visited_bfs.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node , end = " ")

        for neighbour in graph[node]:
            if neighbour not in visited_bfs:
                visited_bfs.add(neighbour)
                queue.append(neighbour)

print("DFS:")
dfs("A")
print("\nBFS:")
bfs("A")


# Q1. Difference between DFS and BFS?
# Answer:
# DFS visits nodes deeply first using recursion or stack.
# BFS visits nodes level by level using queue.

# Q2. Which data structure is used in BFS?
# Answer:
# Queue.

# Q3. Which data structure is used in DFS?
# Answer:
# Stack or recursion.

# Q4. Why visited set is needed?
# Answer:
# To avoid revisiting nodes and infinite loops.

# Q5. Which traversal gives shortest path?
# Answer:
# BFS.