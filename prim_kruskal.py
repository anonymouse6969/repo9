def kruskal(n, edges):
    parent = []
    for i in range(n):
        parent.append(i)

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(a, b):
        pa = find(a)
        pb = find(b)
        parent[pa] = pb

    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            if edges[i][2] > edges[j][2]:
                temp = edges[i]
                edges[i] = edges[j]
                edges[j] = temp

    mst = []
    total = 0

    for edge in edges:
        u = edge[0]
        v = edge[1]
        w = edge[2]

        if find(u) != find(v):
            union(u, v)
            mst.append(edge)
            total = total + w

    return mst, total


def prim(n, graph):
    visited = []
    for i in range(n):
        visited.append(False)

    visited[0] = True
    mst = []
    total = 0

    for i in range(n - 1):
        min_w = 9999
        u = -1
        v = -1

        for j in range(n):
            if visited[j]:
                for k in graph[j]:
                    node = k[0]
                    weight = k[1]

                    if not visited[node] and weight < min_w:
                        min_w = weight
                        u = j
                        v = node

        visited[v] = True
        mst.append((u, v, min_w))
        total = total + min_w

    return mst, total


n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

edges = []
graph = []

for i in range(n):
    graph.append([])

print("Enter edges (u v w):")
for i in range(e):
    u = int(input("u: ")) 
    v = int(input("v: ")) 
    w = int(input("weight: "))

    edges.append((u, v, w))
    graph[u].append((v, w))
    graph[v].append((u, w))


mst1, cost1 = kruskal(n, edges)
mst2, cost2 = prim(n, graph)

print("\nKruskal MST:", mst1)
print("Total Cost:", cost1)

print("\nPrim MST:", mst2)
print("Total Cost:", cost2)
