cities = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = [False] * 4

current = 0
visited[current] = True

path = [current]
cost = 0

for i in range(3):

    minimum = 999
    next_city = -1

    for j in range(4):

        if not visited[j] and cities[current][j] < minimum:
            minimum = cities[current][j]
            next_city = j

    visited[next_city] = True
    path.append(next_city)
    cost += minimum

    current = next_city

cost += cities[current][0]
path.append(0)

print("Path:", path)
print("Total Cost:", cost)