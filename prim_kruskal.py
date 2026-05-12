#prim and kruskal

def kruskal(n, edges):

    # CREATE PARENT ARRAY
    # Initially every node is its own parent
    # Example: [0,1,2,3]

    parent = []

    for i in range(n):
        parent.append(i)



    # FIND FUNCTION
    # Finds root parent of a node
    # Used to check whether two nodes belong to same group

    def find(x):

        while parent[x] != x:
            x = parent[x]

        return x



    # UNION FUNCTION
    # Connects two groups together

    def union(a, b):

        pa = find(a)
        pb = find(b)

        parent[pa] = pb



    # SORT EDGES ACCORDING TO WEIGHT
    # Smaller weight edges come first

    for i in range(len(edges)):

        for j in range(i + 1, len(edges)):

            if edges[i][2] > edges[j][2]:

                temp = edges[i]
                edges[i] = edges[j]
                edges[j] = temp



    # MST STORAGE
    # mst stores selected edges
    # total stores total minimum cost

    mst = []
    total = 0



    # MAIN KRUSKAL LOGIC

    for edge in edges:

        # EXTRACT EDGE VALUES

        u = edge[0]
        v = edge[1]
        w = edge[2]



        # CHECK FOR CYCLE
        # If parents are different,
        # adding edge is safe

        if find(u) != find(v):


            # CONNECT GROUPS

            union(u, v)


            # ADD EDGE TO MST

            mst.append(edge)


            # ADD EDGE WEIGHT TO TOTAL COST

            total = total + w



    # RETURN FINAL MST AND TOTAL COST

    return mst, total


def prim(n, graph):

    # CREATE VISITED ARRAY
    # Initially no node is visited

    visited = []

    for i in range(n):
        visited.append(False)



    # START FROM NODE 0

    visited[0] = True



    # mst stores selected edges
    # total stores total minimum cost

    mst = []
    total = 0



    # MAIN LOOP
    # MST always has n-1 edges

    for i in range(n - 1):


        # VARIABLES TO STORE MINIMUM EDGE

        min_w = 9999
        u = -1
        v = -1



        # CHECK ALL NODES

        for j in range(n):


            # ONLY CHECK VISITED NODES

            if visited[j]:


                # CHECK ALL NEIGHBOURS OF NODE j

                for k in graph[j]:


                    # EXTRACT NODE AND WEIGHT

                    node = k[0]
                    weight = k[1]



                    # FIND SMALLEST EDGE
                    # Edge should connect:
                    # visited node -> unvisited node

                    if not visited[node] and weight < min_w:

                        min_w = weight

                        u = j
                        v = node



        # MARK NEW NODE AS VISITED

        visited[v] = True



        # ADD EDGE TO MST

        mst.append((u, v, min_w))



        # ADD WEIGHT TO TOTAL COST

        total = total + min_w



    # RETURN MST AND TOTAL COST

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
