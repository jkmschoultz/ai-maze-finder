import networkx as nx

maze = []
visited = []
steps = 0
done = False

# Returns maze loaded from file with 'filename' in mazes directory
def load_maze(filename):
    G = nx.Graph()
    with open("mazes/" + filename) as f:
        global maze
        for line in f.readlines():
            if line.strip() != "":
                maze.append(line.strip().split())
    #return maze
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '-':
                G.add_node((x, y))
                if maze[y-1][x] == '-':
                    G.add_edge((x,y), (x,y-1))
                if maze[y][x-1] == '-':
                    G.add_edge((x,y), (x-1,y))
    return G

# Find the path through the maze
def find_start(maze):
    return (maze[0].index('-'), 0)

# Check if can move in a given direction from the current position
def can_move(maze, xpos, ypos, dir):
    newx, newy = xpos, ypos
    if dir == 'left':
        newx -= 1
    elif dir == 'right':
        newx += 1
    elif dir == 'down':
        newy += 1
    elif dir == 'up':
        newy -= 1
    
    if (newx, newy) not in visited and maze[newx][newy] == '-':
        return True
    return False
        

# Depth first search
def dfs(maze, current_pos):
    while current_pos[1] != len(maze)-1:
        (x, y) = current_pos
        if can_move(maze, x, y, 'right'):
            current_pos[0] += 1
        elif can_move(maze, x, y, 'down'):
            current_pos[1] += 1
        elif can_move(maze, x, y, 'left'):
            current_pos[0] -= 1
        elif can_move(maze, x, y, 'up'):
            current_pos[1] -= 1
        global visited
        visited += current_pos
        print(current_pos)

def search(graph, node):
    global done
    if node[1] == len(maze)-1:
        visited.append(node)
        done = True

    if node not in visited and not done:
        visited.append(node)
        global steps
        steps += 1
        print(node)
        for adjacent in list(graph.neighbors(node)):
            search(graph, adjacent)

if __name__ == "__main__":
    small_maze = load_maze("maze-Medium.txt")
    search(small_maze, find_start(maze))
    print(visited)
    """for line in small_maze:
        print(line)
    find_path(small_maze)
    print(visited)"""
