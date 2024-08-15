# DragonFight Game

## Overview
The goal of this project is to create a DragonFight game, where players choose a dragon with specific power points and face off against a randomly selected opponent dragon. The project aims to enhance your Python programming skills, including the use of loops, conditional statements, and user input, while also encouraging creativity and adherence to coding standards such as PEP-8.

## Project Objectives
- Apply basic Python concepts such as loops, conditional statements, and user input.
- Develop logical thinking and adaptability.
- Incorporate creativity in game design.

## Project Outline

### Game Introduction
1. Create a welcome message including an explanation of the rules of the game.
2. Inform the user how to play the game and how to exit.
3. The game is structured around multiple rounds where the player chooses a dragon to fight against a randomly selected opponent dragon. Each round can result in the player winning, the computer winning, or a draw.

### Game Setup
1. Define a dictionary of dragons with their respective power points.
2. Initialize counters for the total number of rounds, player points, and computer points.

### Main Game Loop
1. Use a `while` loop to manage the flow of the game.
2. Within this loop, reset the round and point counters for each new game.

### Round Loop
1. Use a loop to continue playing rounds until a specified number of rounds are completed (e.g., 5 rounds).
2. Prompt the player to choose a dragon from the list.
3. Generate a random opponent dragon using the `random` module.
4. Use logical operations or basic `if-else` statements to determine the winner of each round based on the dragon power points.
5. Update the point counters accordingly and print the results of each round.

### Determine the Game Winner
1. After all rounds are completed, determine the overall winner based on the final point totals.
2. Display the appropriate message announcing the winner.

### Request to Continue
1. Ask the player if they want to play another game.
2. Also, generate a random decision for the computer to determine if it wants to continue playing.
3. If both the player and the computer want to continue, restart the game; otherwise, end the game with a closing message.

## Example Game Flow
- **Game Introduction**: Provide a detailed explanation of the rules.
- **Setup**: Display available dragons and initialize game variables.
- **Gameplay**:
  - **Round 1**: Player picks a dragon, computer picks a dragon, determine and display the winner, update points.
  - **Round 2**: Continue as above until the specified number of rounds is completed.
- **Game Result**: Announce the winner based on the points after all rounds.
- **Continue?**: Prompt player to play again, generate computer's decision, and either restart or end the game.
