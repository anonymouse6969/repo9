#8 puzzle

from queue import PriorityQueue

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def copy_state(state):
    new = []
    for row in state:
        new.append(row[:])
    return new

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def astar():
    pq = PriorityQueue()
    pq.put((heuristic(start), start))

    visited = set()

    while not pq.empty():

        cost, current = pq.get()

        if current == goal:
            print("Goal State Reached:")
            for row in current:
                print(row)
            return

        visited.add(state_to_tuple(current))

        x, y = find_zero(current)

        moves = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        for nx, ny in moves:

            if 0 <= nx < 3 and 0 <= ny < 3:

                new_state = copy_state(current)

                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                if state_to_tuple(new_state) not in visited:
                    h = heuristic(new_state)
                    pq.put((h, new_state))

astar()
