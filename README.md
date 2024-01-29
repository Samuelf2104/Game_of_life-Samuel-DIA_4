# TD_1_game_of_life

# Game of Life Simulator

## Overview
This Python script simulates Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The game represents an ever-evolving grid of cells that follow a simple set of rules to either live, die, or multiply based on their neighbors.

## Features
- Randomized board generation.
- Configurable board dimensions and generations.
- Visualization of each generation's state.
- Automatic clearing and updating of the console for dynamic display.

## How to Run
To start the simulation, execute the script with Python. By default, it runs a 50-generation simulation on a 20x20 board.

## Customization
You can customize the board size and the number of generations by changing the parameters in the `game_of_life` function call at the end of the script.

## Rules
1. Any live cell with two or three live neighbors survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Dependencies
- Python Standard Library: `random`, `time`, `os`

## Example
game_of_life(20, 20, 50) # Runs a 50-generation simulation on a 20x20 board with random initialization.