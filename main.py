import time

maze = []

# Returns maze loaded from file with 'filename' in mazes directory
def load_maze(filename):
    with open("mazes/" + filename) as f:
        global maze
        for line in f.readlines():
            if line.strip() != "":
                maze.append(line.strip().split())
    return maze

# Perform depth first search of maze from a start position
def dfs(maze, start):
    # List to track all visited nodes
    visited = []
    # A tuple in the stack represents the current position and list of nodes in path to this position
    stack = [(start, [start])]
    while stack != []:
        (x, y), path = stack.pop()
        # Visit node in stack if not yet visited
        if (x, y) not in visited:
            visited.append((x, y))
            if x == len(maze)-1:
                # Return if end has been reached
                return path, len(visited)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                # Add each possible path to stack
                if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) \
                        and maze[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                    stack.append(((new_x, new_y), path + [(new_x, new_y)]))
    return None

if __name__ == "__main__":
    start_load = time.time()
    load_maze("maze-VLarge.txt")
    end_load = time.time()
    
    start = (0, maze[0].index('-'))
    steps = 0

    start_time = time.time()
    path, nodes_visited = dfs(maze, start)
    end_time = time.time()

    if path:
        for x, y in path:
            maze[x][y] = '*'
            steps += 1
        for row in maze:
            print(' '.join(row))

        print(str(len(maze[0])) + 'x' + str(len(maze)) + ' maze')
        print('Steps taken: ' + str(steps))
        print('Nodes visited: ' + str(nodes_visited))
        print('Time to load: ' + str(end_load-start_load) + ' seconds')
        print('Execution time: ' + str(end_time-start_time) + ' seconds')

    else:
        print('No path found')
