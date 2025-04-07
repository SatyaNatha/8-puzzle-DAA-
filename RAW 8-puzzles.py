from collections import deque

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Convert list of lists to tuple (hashable)
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Find the position of 0 (blank)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Move generator
def get_neighbors(state):
    x, y = find_zero(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# BFS algorithm
def bfs(start):
    visited = set()
    queue = deque([(start, [])])
    
    while queue:
        state, path = queue.popleft()
        state_tuple = to_tuple(state)
        
        if state == goal_state:
            return path + [state]
        
        if state_tuple in visited:
            continue
        
        visited.add(state_tuple)

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))
    
    return None

# DFS algorithm
def dfs(start, depth_limit=50):
    visited = set()
    stack = [(start, [])]

    while stack:
        state, path = stack.pop()
        state_tuple = to_tuple(state)

        if state == goal_state:
            return path + [state]
        
        if state_tuple in visited or len(path) >= depth_limit:
            continue
        
        visited.add(state_tuple)

        for neighbor in get_neighbors(state):
            stack.append((neighbor, path + [state]))
    
    return None

# Helper to print the puzzle
def print_path(path):
    for step in path:
        for row in step:
            print(row)
        print("------")

# Example usage
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

print("Solving with BFS...")
path_bfs = bfs(start_state)
print_path(path_bfs)

print("Solving with DFS...")
path_dfs = dfs(start_state)
print_path(path_dfs)
