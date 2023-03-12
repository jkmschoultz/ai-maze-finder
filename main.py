import time

maze = []

# Returns 2D array of maze loaded from file with 'filename' in mazes directory
def load_maze(filename):
    with open("mazes/" + filename) as f:
        maze = []
        for line in f.readlines():
            if line.strip() != "":
                maze.append(line.strip().split())
    return maze

# Perform depth first search of a given maze from a start position
def dfs(maze, start):
    # Use set to keep track of all visited nodes
    visited = set()
    # A tuple in the stack contains the current position and list of nodes in path to reach position
    stack = [(start, [start])]
    while stack != []:
        (x, y), path = stack.pop()
        # Visit popped node from stack if not yet visited
        if (x, y) not in visited:
            visited.add((x, y))
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

# Save the solution found to a maze to a file that can be viewed 
def save_result(filename, maze):
    with open("solutions/"+ filename, 'w') as f:
        for row in maze:
            f.write(' '.join(row) + '\n')

if __name__ == "__main__":
    # Load maze
    start_load = time.time()
    maze = load_maze("maze-VLarge.txt")
    end_load = time.time()
    
    #Find start of maze
    start = (0, maze[0].index('-'))
    steps = 0

    # Perform depth first search
    start_time = time.time()
    path, nodes_visited = dfs(maze, start)
    end_time = time.time()

    if path:
        # Save maze solution to file
        for x, y in path:
            maze[x][y] = '*'
            steps += 1
        save_result('solution-VLarge.txt', maze)

        # Print statistics
        print(path)
        print(str(len(maze[0])) + 'x' + str(len(maze)) + ' maze')
        print('Steps in path: ' + str(steps))
        print('Nodes visited: ' + str(nodes_visited))
        print('Time to load: ' + str(end_load-start_load) + ' seconds')
        print('Execution time: ' + str(end_time-start_time) + ' seconds')

    else:
        print('No path found')
