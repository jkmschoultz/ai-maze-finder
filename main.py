import time
import math
from queue import PriorityQueue

MAZE_TO_LOAD = "maze-Easy.txt"
SAVE_MAZE_TO = "solution-Easy.txt"

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

def a_star_search(maze, start, end):
    # Use set to keep track of all visited nodes
    visited = set()
    # An entry in the queue contains the priority, and a tuple of the current position and list of path taken
    priority_queue = PriorityQueue()
    priority = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    priority_queue.put((priority, (start, [start])))

    while not priority_queue.empty():
        # Get entry from queue with highest priority
        priority, ((x, y), path) = priority_queue.get()
        # Visit node if not yet visited
        if (x, y) not in visited:
            visited.add((x, y))
            if y == len(maze)-1:
                # Return path and number of nodes visited if end has been reached
                return path, len(visited)

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                # Calculate priority of each possible path to take and add to queue
                if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]) \
                        and maze[new_y][new_x] != '#' and (new_x, new_y) not in visited:
                    # Obtain goal node position
                    goal_x, goal_y = end
                    # Calculate node priority based on distance from goal node
                    priority = math.sqrt((goal_x - new_x)**2 + (goal_y - new_y)**2)
                    # Add to priority queue
                    data = ((new_x, new_y), path + [(new_x, new_y)])
                    priority_queue.put((priority, data))
    return None, None


if __name__ == "__main__":
    # Load maze
    start_load = time.time()
    maze = load_maze(MAZE_TO_LOAD)
    end_load = time.time()
    
    #Find start of maze
    start = (maze[0].index('-'), 0)
    steps = 0

    # Perform depth first search
    print(str(len(maze[0])) + 'x' + str(len(maze)) + ' maze')
    start_time = time.time()
    path, nodes_visited = dfs(maze, start)
    end_time = time.time()

    if path:
        # Save maze solution to file
        for x, y in path:
            maze[y][x] = '.'
            steps += 1
        save_result(SAVE_MAZE_TO, maze)

        # Print statistics
        print('Path found: '+ str(path))
        print('Total nodes visited: ' + str(nodes_visited))
        print('Steps in path: ' + str(steps))
        print('Time to load: ' + str(end_load-start_load) + ' seconds')
        print('Search time: ' + str(end_time-start_time) + ' seconds')

    else:
        print('No path found')

    print('\n\n\n')

    # Reset maze for a star search
    maze = load_maze(MAZE_TO_LOAD)
    steps = 0

    # Find end of maze
    length = len(maze)-1
    end = (length, maze[length].index('-'))

    # Perform A star search
    print(str(len(maze[0])) + 'x' + str(len(maze)) + ' maze')
    start_time = time.time()
    path, nodes_visited = a_star_search(maze, start, end)
    end_time = time.time()
    
    if path:
        # Save maze solution to file
        for x, y in path:
            maze[y][x] = '.'
            steps += 1
        save_result('a-star-'+SAVE_MAZE_TO, maze)

        # Print statistics
        print('Path found: ' + str(path))
        print('Total nodes visited: ' + str(nodes_visited))
        print('Steps in path: ' + str(steps))
        print('Time to load: ' + str(end_load-start_load) + ' seconds')
        print('Search time: ' + str(end_time-start_time) + ' seconds')

    else:
        print('No path found')
