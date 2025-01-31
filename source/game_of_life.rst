The Game of Life
==================

This file contains the implementation of Conway's Game of Life.

The Game of Life is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

Rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.

2. Any live cell with two or three live neighbours lives on to the next generation.

3. Any live cell with more than three live neighbours dies, as if by overpopulation.

4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The game is played on a grid of cells, where each cell can be in one of two states: alive or dead. The state of the grid evolves in discrete time steps, with the state of each cell at the next time step being determined by the current states of its eight neighbours.

 