# Tic-Tac-Toe Game Project

## Part 1: Project Introduction

In this project, you will build a Tic-Tac-Toe game in the command line interface. Two players, X and O, will take turns picking their next move by entering numbers in the command line.

### Project Breakdown

The project is divided into two parts:

- **Part 1**: Build all the utility functions for the game, including:
  - `markBoard`
  - `printBoard`
  - `validateMove`
  - `checkWin`
  - `checkFull`
  - A constant variable storing all the winning combinations (`winCombinations`)

- **Part 2**: Complete the gameplay using the utility functions built in Part 1.


# Tic-Tac-Toe Utility Functions

This document outlines the utility functions required for a Tic-Tac-Toe game. Each function has specific requirements and responsibilities.

## Functions

### `markBoard(position, mark)`
- **Inputs:**
  - `position`: A number representing the box number.
  - `mark`: The player's mark (X or O).
- **Description:** This function fills the specified box with the player's mark (X or O).

### `printBoard()`
- **Description:** Prints the current state of the game board. If a box is unoccupied, it prints the number of that box.
- **Example Output:**

  | X | O | 3 |
  |---|---|---|
  | X | X | 6 |
  | O | 8 | O |


### `validateMove(position)`
- **Inputs:**
- `position`: The position that the player picked.
- **Description:** Validates the player's move and returns `true` or `false`.
- **Checks for:**
  - Wrong Input (invalid position, not entering a position).
  - Out of bound position (smaller than 1 or larger than 9).
  - The position is already occupied.
- **Returns:** `true` if the input is correct, otherwise `false`.

### `checkWin()`
- **Description:** Checks if the current player has won the game.
- **Returns:** `true` if the player has won, otherwise `false`.

## Usage

To use these functions, ensure you have a basic understanding of the game rules and the structure of the game board. Each function plays a crucial role in managing the game state and ensuring a smooth gameplay experience.

