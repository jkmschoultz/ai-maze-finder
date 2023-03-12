import time

"""
Returns 2D array of maze loaded from file with 'filename' in mazes directory.
"""
def load_maze(filename):
    with open("mazes/" + filename) as f:
        maze = []
        for line in f.readlines():
            if line.strip() != "":
                maze.append(line.strip().split())
    return maze

"""
Perform depth first search of a given maze from a start position.
Returns tuple of style: (solution_path, total_nodes_visited)
(None, None) if no solution found
"""
def dfs(maze, start):
    # Use set to keep track of all visited nodes
    visited = set()
    # A tuple in the stack contains the current position and list of nodes in path to reach position
    stack = [(start, [start])]
    while stack != []:
        (x, y), path = stack.pop()
        # Visit node popped from stack if not yet visited
        if (x, y) not in visited:
            visited.add((x, y))
            if y == len(maze)-1:
                # Return path and number of nodes visited if end has been reached
                return path, len(visited)

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                # Add each possible path to stack
                if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]) \
                        and maze[new_y][new_x] != '#' and (new_x, new_y) not in visited:
                    stack.append(((new_x, new_y), path + [(new_x, new_y)]))
    return None, None

"""
Save the solution found to a maze to a file that can be viewed.
"""
def save_result(filename, maze):
    with open("solutions/"+ filename, 'w') as f:
        for row in maze:
            f.write(' '.join(row) + '\n')


if __name__ == "__main__":
    # Load maze
    start_load = time.time()
    maze = load_maze("maze-Small.txt")
    end_load = time.time()
    
    #Find start of maze
    start = (maze[0].index('-'), 0)
    steps = 0

    # Perform depth first search
    start_time = time.time()
    path, nodes_visited = dfs(maze, start)
    end_time = time.time()

    if path:
        # Save maze solution to file
        for x, y in path:
            maze[y][x] = '*'
            steps += 1
        save_result('solution-Small.txt', maze)

        # Print statistics
        print(path)
        print(str(len(maze[0])) + 'x' + str(len(maze)) + ' maze')
        print('Total nodes visited: ' + str(nodes_visited))
        print('Steps in path: ' + str(steps))
        print('Time to load: ' + str(end_load-start_load) + ' seconds')
        print('Search time: ' + str(end_time-start_time) + ' seconds')

    else:
        print('No path found')
