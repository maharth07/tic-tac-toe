# Tic-Tac-Toe AI Game

A simple command-line Tic-Tac-Toe game where you can play against an unbeatable AI opponent. The AI uses the Minimax algorithm with Alpha-Beta pruning to make optimal moves.

## Features

- Human vs AI gameplay
- Unbeatable AI opponent (always plays optimally)
- Command-line interface
- Clear board display
- Input validation

## How to Play

Tic-Tac-Toe is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

In this version:
- You are X (Human)
- AI is O
- Positions are numbered 0-8, starting from top-left (0) to bottom-right (8)

## Requirements

- Python 3.x

## Installation

No installation required. Just ensure you have Python installed on your system.

## Running the Game

1. Open a terminal/command prompt
2. Navigate to the directory containing `qqqq.py`
3. Run the command: `python qqqq.py`
4. Follow the on-screen instructions to make your moves

## Game Rules

- Players take turns placing their marks (X or O) on the board
- The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
- If all 9 squares are filled without a winner, it's a tie
- You go first as X, AI responds as O

## AI Strategy

The AI uses the Minimax algorithm to evaluate all possible game states and choose the best move. Alpha-Beta pruning optimizes the search to make it efficient even for a small game like Tic-Tac-Toe.

## Contributing

Feel free to modify the code or add features like:
- GUI interface
- Different difficulty levels
- Two-player mode
- Score tracking

## License

This project is open source. Feel free to use and modify as needed.
