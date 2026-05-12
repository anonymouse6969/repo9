#maze

from queue import PriorityQueue

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar():

    pq = PriorityQueue()
    pq.put((0, start))

    visited = set()

    while not pq.empty():

        cost, current = pq.get()

        if current == goal:
            print("Goal reached:", current)
            return

        visited.add(current)

        x, y = current

        neighbours = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        for nx, ny in neighbours:

            if 0 <= nx < 3 and 0 <= ny < 3:

                if grid[nx][ny] == 0 and (nx, ny) not in visited:

                    h = heuristic((nx, ny), goal)

                    pq.put((h, (nx, ny)))

    print("No path found")

astar()