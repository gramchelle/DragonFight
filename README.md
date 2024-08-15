# DragonTaso Game

## Overview

The DragonFight game pits players against a computer-controlled opponent in a series of battles featuring dragons with specific power points. The game aims to enhance Python programming skills and provide an engaging experience with basic game mechanics, including loops, conditionals, and user input.

This project was developed as a capstone project for the Global AI Hub's Aygaz Python Bootcamp. It serves as an opportunity to apply foundational Python concepts and develop creative problem-solving skills while engaging in a fun and interactive game.


## Project Objectives

- Apply basic Python concepts such as loops, conditional statements, and user input.
- Develop logical thinking and adaptability.
- Incorporate creativity in game design.

## Project Outline

### Game Introduction

- Create a welcome message explaining the rules of the game.
- Inform the user how to play and how to exit.
- The game consists of multiple rounds where players choose a dragon to fight against a randomly selected opponent dragon. Each round results in a win, loss, or draw.

### Game Setup

- Define a dictionary of dragons with their respective power points.
- Initialize counters for total rounds, player points, and computer points.

### Main Game Loop

- Use a `while` loop to manage the flow of the game.
- Reset the round and point counters for each new game.

### Round Loop

- Use a loop to continue playing rounds until a specified number of rounds are completed (e.g., 5 rounds).
- Prompt the player to choose a dragon from the list.
- Generate a random opponent dragon using the `random` module.
- Determine the winner of each round based on the dragon power points using if-else statements.
- Update the point counters and print the results of each round.

### Determine the Game Winner

- After all rounds are completed, determine the overall winner based on the final point totals.
- Display the appropriate message announcing the winner.

### Request to Continue

- Ask the player if they want to play another game.
- Generate a random decision for the computer to determine if it wants to continue playing.
- If both the player and the computer want to continue, restart the game; otherwise, end the game with a closing message.

## Installation

To run the game, ensure you have Python installed. You can download Python from the [official website](https://www.python.org/downloads/).

1. Clone the repository or download the source code.
2. Navigate to the directory containing the `DragonTaso.py` file.

   ```sh
   cd path_to_directory ```
3. Run the game using Python:
``` python DragonTaso.py ```
## Usage

1. **Starting the Game:**
   - Run the game script by executing the following command in your terminal:

     ```sh
     python DragonTaso.py
     ```

2. **Choosing a Dragon:**
   - At the beginning of each round, you will be prompted to choose a dragon from the list of available dragons.
   - Enter the name of the dragon you want to fight with, e.g., `trex`.

3. **Round Outcomes:**
   - After you make your choice, the computer will randomly select a dragon.
   - The game will display the power points of both dragons and announce the result of the round:
     - **Win:** If your dragon's power points are higher than the computer's dragon.
     - **Draw:** If both dragons have the same power points.
     - **Loss:** If your dragon's power points are lower than the computer's dragon.

4. **Scoring:**
   - Winning a round adds 20 points to your score and deducts 40 points from the computer's score.
   - Drawing a round results in a deduction of 20 points from both scores.
   - Losing a round results in a deduction of 40 points from your score and adds 20 points to the computer's score.

5. **Game Rounds:**
   - The game continues for a predefined number of rounds (e.g., 5 rounds).
   - After every two rounds, you will have the option to continue playing or exit.

6. **Winning the Game:**
   - If either you or the computer wins two rounds in a row, the respective player will be declared the overall winner.
   - The game ends when either player runs out of points or the rounds are completed.

7. **Playing Again:**
   - At the end of each series of rounds, you will be asked if you want to play another game.
   - Type 'y' to play again or any other key to exit.

## Contact
For any questions or feedback, feel free to reach out:

* Email: ozlemnduman34@hotmail.com
* Linkedin: (https://www.linkedin.com/in/ozlemnurduman/)


Footnote: I wanted to make something different, so i used the rock paper scissors format and the requirements in the instructions given. Everything is in the same format and method with rock paper scissors game, but instead of objects we have dragon heroes in this game. By increasing the number of options, chances of winning and losing decreases at the same time. Which motivates the player to be careful when deciding what to use. Wish you enjoy this game. 
