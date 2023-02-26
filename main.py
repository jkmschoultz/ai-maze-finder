maze = []

# Returns maze loaded from file with 'filename' in mazes directory
def load_maze(filename):
    with open("mazes/" + filename) as f:
        global maze
        for line in f.readlines():
            if line.strip() != "":
                maze.append(line.strip().split())
    return maze

def dfs(maze, start, end):
    visited = []
    stack = [(start, [start])]
    while stack:
        (x, y), path = stack.pop()
        if (x, y) not in visited:
            visited.append((x, y))
            if x == end:
                return path, len(visited)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#' and (nx, ny) not in visited:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return None

if __name__ == "__main__":
    load_maze("maze-Large.txt")
    
    start = (0, maze[0].index('-'))
    end = len(maze)-1
    path, nodes_visited = dfs(maze, start, end)
    steps = 0

    if path:
        for x, y in path:
            maze[x][y] = '*'
            steps += 1
        for row in maze:
            print(' '.join(row))

        print('Steps taken: ' + str(steps))
        print('Nodes visited: ' + str(nodes_visited))

    else:
        print('No path found')
