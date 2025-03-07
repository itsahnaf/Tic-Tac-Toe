
# Tic-Tac-Toe Game

A simple, graphical two-player Tic-Tac-Toe game built with Python and Tkinter. The game features an easy-to-use interface with colourful elements to distinguish between players and provide feedback on game progress, such as detecting winners and ties.

## Features

- **Two-player gameplay**: Players alternate between marking "X" and "O".
- **Interactive UI**: Uses Tkinter to create a user-friendly graphical interface.
- **Winner Detection**: Automatically checks for a winner after every move.
- **Tie Detection**: Detects when all the squares are filled without a winner.
- **Colourful Design**: Utilises colours for a more visually appealing experience.
- **Game Reset**: Automatically resets the game after a win or a tie.

## Requirements

- **Python 3.x**: The game requires Python 3.x or higher.
- **Tkinter**: Tkinter is included in most Python installations by default. If not, it can be installed as follows:
  - On Debian/Ubuntu-based systems:
    ```bash
    sudo apt-get install python3-tk
    ```

## Installation

1. Ensure that Python 3.x is installed on your machine.
   - To check Python version:
     ```bash
     python --version
     ```
   
2. Clone this repository or download the `tic_tac_toe.py` file:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   ```

3. Install Tkinter if it's not already installed:
   - On Windows and macOS, Tkinter usually comes pre-installed with Python.
   - On Linux, you can install it with the package manager:
     ```bash
     sudo apt-get install python3-tk
     ```

## How to Play

1. Run the game by executing the script:
   ```bash
   python tic_tac_toe.py
   ```
   The game window will open, displaying a 3x3 grid.
   
2. **Player 1 (X)**: Click on an empty square to place "X".
3. **Player 2 (O)**: Click on an empty square to place "O".
4. The game will automatically detect when one player wins or if the game ends in a tie.
5. Once the game ends, a pop-up message will appear with the result, and the board will reset for a new game.

## How It Works

1. **Game Board**: The game board consists of a 3x3 grid, represented as a list of 9 elements.
2. **Game Logic**: The game alternates between two players, "X" and "O". After each move, the program checks for a winner by evaluating the defined winning combinations.
3. **Winner Detection**: A player wins if they manage to align three of their marks either horizontally, vertically, or diagonally. If no player wins and the board is full, the game declares a tie.
4. **Game Reset**: After a win or tie, the game automatically resets for a new round.

## Code Structure

- `TicTacToe` Class: Contains the main game logic and UI.
  - `__init__`: Sets up the game and UI.
  - `create_board`: Generates the 3x3 grid of buttons.
  - `make_move`: Handles the player's move and updates the board.
  - `check_winner`: Checks the game state for a winner.
  - `reset_board`: Resets the game board for a new round.
  
- Tkinter buttons are used to interact with the game board. The game detects clicks on the buttons to place marks and checks for winning conditions after each move.

## Screenshot

![Tic-Tac-Toe](screenshot.png)  
*The Tic-Tac-Toe game interface displaying a 3x3 grid.*

## Contribution

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your changes and open a pull request.

## Licence

This project is open-source and available under the MIT Licence. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- The Tkinter library is used for building the GUI.
- This project was inspired by the classic Tic-Tac-Toe game.
