# Returns maze loaded from file with 'filename' in mazes directory
def loadMaze(filename):
    with open("mazes/" + filename) as f:
        maze = []
        for line in f.readlines():
            if line.strip() != "":
                maze.append(line.strip().split())
        return maze

if __name__ == "__main__":
    small_maze = loadMaze("maze-Small.txt")
    for line in small_maze:
        print(line)
    print(len(small_maze))
