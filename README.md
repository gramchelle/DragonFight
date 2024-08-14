# DragonFight Game
## Overview
The goal of this project is to create a DragonFight game, where players choose a dragon with specific power points and face off against a randomly selected opponent dragon. The project aims to enhance your Python programming skills, including the use of loops, conditional statements, and user input, while also encouraging creativity and adherence to coding standards such as PEP-8.
## Project Objectives
* Apply basic Python concepts such as loops, conditional statements, and user input.
* Develop logical thinking and adaptability.
* Incorporate creativity in game design.
## Project Outline
1. Game Introduction:
   * Create a welcome message including explanation of the rules of the game.
   * Inform the user how to play the game and how to exit.
   * The game is structured around multiple rounds where the player chooses a dragon to fight against a randomly selected opponent dragon. Each round can result in the player winning, the computer winning, or a draw.
2. Game Setup:
   * Define a dictionary of dragons with their respective power points.
   * Initialize counters for the total number of rounds, player points, and computer points.
3. Main Game Loop:
   * Use a while loop to manage the flow of the game.
   * Within this loop, reset the round and point counters for each new game.
4. Round Loop:
   * Use a loop to continue playing rounds until a specified number of rounds are completed (e.g., 5 rounds).
   * Prompt the player to choose a dragon from the list.
   * Generate a random opponent dragon using the random module.
   * Use logical operations or basic if-else statements to determine the winner of each round based on the dragon power points.
   * Update the point counters accordingly and print the results of each round.
5. Determine the Game Winner:
   * After all rounds are completed, determine the overall winner based on the final point totals.
   * Display the appropriate message announcing the winner.
6. Request to Continue:
   * Ask the player if they want to play another game.
   * Also, generate a random decision for the computer to determine if it wants to continue playing.
   * If both the player and the computer want to continue, restart the game; otherwise, end the game with a closing message.
