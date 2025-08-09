# secret-numbers
A classic "Guess the Number" game built with Python. The script generates a secret number from 1 to 10, and the player must guess it while the program counts the number of attempts.

# Secret Number Guessing Game

This is a simple yet fun terminal-based game written in Python. The program uses the `random` library to generate a secret integer between 1 and 10. The player is then prompted to guess the number. The game provides feedback after each wrong guess and continues until the player guesses correctly, at which point it reveals the number of attempts taken.

## Features

-   Generates a random secret number for each new game.
-   Interactive command-line interface for user input.
-   Counts the total number of guesses.
-   Displays a congratulatory message with the total tries upon winning.

## How to Run

1.  Make sure you have [Python 3](https://www.python.org/downloads/) installed on your system.
2.  Save the code as a Python file (e.g., `secret_number.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command:
    ```bash
    python secret_number.py
    ```

## Usage Example

The program will repeatedly ask for a number until you guess the correct one.

```
Try to guess a number between 1 and 10:
5
Try again!
Try to guess a number between 1 and 10:
8
Try again!
Try to guess a number between 1 and 10:
7
Congratulations you guessed the number 7, it took 3 tries!
```
