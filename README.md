# AI Maze Solver

This is a program for finding paths through a maze by the use of search algorithms. This program uses both a depth-first search algorithm and an A* search algorithm for solving mazes.

## How it works

The program loads in a maze from a text file located in the `mazes/` directory, and provides the path it finds through this maze in the `solutions/` directory. The solution path is represented by `.` (dots) leading through the maze, and can be more easily viewed by searching the file for all occurrences of a full-stop.

The file from which to load a maze is specified in the `MAZE_TO_LOAD` variable, and the file to save the solution to is specified by the `SAVE_MAZE_TO` variable. These can be changed between runs of the program to trial it across mazes of various sizes and layouts.

The program will create two solution files from a run: one specifying the solution found by the depth first search algorithm, and the other specifying the solution found by the A* search algorithm.

If no path is found that leads through the maze, the program will simply output 'No path found'.

## How to run

The program can be simply run from a terminal opened in the root folder with the command:

    python3 main.py

Upon being launched, the program first performs a depth-first search of the mazes, and will output a list containing the path through the maze that it found, as well as other statistics. Each entry in the list corresponds to an (x, y) coordinate in the maze.

After the depth first search is completed, it continues to do an A* search, similarly outputting the path found by this search and other statistics.

Upon completing each search of the maze, the program will output statistics regarding the search. These include:

- the total number of nodes that it visited in the maze (if the maze is considered as a graph-like structure)
- the total number of steps in the resulting path
- the total time it took to load the maze
- the time to search the maze

For larger mazes, the user may need to scroll up in the terminal to see the resulting statistics for the depth-first search.
