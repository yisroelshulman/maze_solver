# **_Maze Solver_**

## Description
My spin on the Boot.dev Maze Solver Project.\
Generates a random maze and then solves it.

### About
The maze is generated as a grid of square cells based on the rows and columns variables from the user input. After the grid is complete a start (green) and end (blue) cell are randomly selected using the initial seed (default or user selected) for the RNG.

> **_NOTE:_** The max number of cells the maze can have is capped at 1,000. This is because the solver uses a recursive depth first traversal algorithm in both the path generation and the solving, and by default the max recursion stack in python is capped at 1,000.


> **_NOTE:_** The min size for a cell is 10 X 10 if the window size is not sufficient the solver will error and exit.


The path is generated using a depth first traversal approach knocking down the walls between cells as they are visited, ensuring that there is a valid solution to the maze.

The solution is derived through a depth first search for the end cell, drawing a red line to the path and errasing it when back tracking. The RNG is reseeded so the attempt to solve can look different every time.

![](https://github.com/yisroelshulman/assets/blob/main/maze_solver/maze.gif)

> **_NOTE:_** The seed determines what the maze will look like, the same seed number will always generate the same maze.

## Quick Start
### Requirements
- python (3.10 or greater)
- tkinter

In a terminal run
```
python -m tkinter
```
If your system has the proper installations, you should see a small pop-up window with some buttons. You can close it and you're good to download the files.

#### _Dependency Issues_
Make sure that you have the correct python installation by checking
```
python --version
```
Uninstall the python environment, install tkinter, and reinstall the python environment.

Check out [Installing Tk][] for more help. If that is not sufficient, try searching the web with the error message to find a solution.

[Installing Tk]: https://tkdocs.com/tutorial/install.html

### Download
To get started download the repository (can also be done as a zipball and unzip).
```
wget https://github.com/yisroelshulman/maze_solver/tarball/master -O maze_solver.tar
```
And unpack
```
tar xvf maze_solver.tar
```

## Usage
In the terminal type
```
python mian.py
```
Follow the prompts for the window's height and width, the maze's rows and columns, and seed for the random number generator.

Sit back and watch the solver generate and solve the maze.