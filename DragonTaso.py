import random

def tas_kagit_makas_OZLEM_NUR_DUMAN():
    print("Welcome to the Dragon Taso game.\n" +
          "In this game you are opponents with your computer.\n\n" +
          "This game basically includes 5 dragons and they all have some Power Points, so if the dragon you pick is weaker than your opponent's pick you lose.\n" +
          "If both players select the same, it will be a draw.\n" +
          "And lastly, if your dragon is stronger than your opponent's dragon, you will win!\n")

    print("Each player starts with 200 player points.\n" +
          "In each lose, players lose 40 points; each draw puts a -20p and each win will provide players a +20p.\n" +
          "If one player wins twice in a row at the beginning, they will win. However, regardless the win scores, whoever runs out of their 200 points will lose, yet with a honured win scores.\n\n" +
          "There will be given an opportunity to leave at the end of each 2 tour.\n\n" +
          "Now you are ready to get it done. Let's play!\n")

    dragons = {
        "trex": 16000,
        "pterodactyl": 16500,
        "velociraptor": 15650,
        "stegosaurus": 14000,
        "triceratops": 15500
    }

    print("### These are the dinosaurs: ### \n", ', '.join(dragons.keys()), "\n")

    user_points = 200
    computer_points = 200

    user_win_scores = 0
    computer_win_scores = 0

    continuity = "y"
    tour_count = 0

    def generate_random_dragon():
        global random_dragon_key, random_dragon_value
        # random.seed(42)
        random_dragon_key = random.choice(list(dragons.keys()))
        random_dragon_value = dragons[random_dragon_key]

    def hero_object():
        return input("Pick your dragon: ").lower()

    def is_hero_in_list(hero):
        if hero not in dragons:
            print("Please enter a valid hero name.")
            return False
        return True

    def wanna_play_again():
        nonlocal continuity
        print("\n\nDo you want to play once more? If yes, enter 'y':")
        decision = input()
        if decision.lower() == 'y':
            print("You both have a good level of confidence!\n")
            play()
        else:
            continuity = False
            print("It was nice to play with you both. Hope to see you next time!")

    def win(winner_points, loser_points, win_score):
        winner_points += 20
        loser_points -= 40
        win_score += 1
        return winner_points, loser_points, win_score

    def check_winner():
        nonlocal user_points, computer_points
        if user_points <= 0:
            print("You have lost all your points. Computer wins the game!")
            return True
        elif computer_points <= 0:
            print("Computer has lost all its points. You win the game!")
            return True
        return False

    def play():
        nonlocal user_points, computer_points, user_win_scores, computer_win_scores, continuity, tour_count

        while continuity == "y":
            generate_random_dragon()

            print("Your opponent has picked. Pick your fighter!")
            hero = input().lower()

            while not is_hero_in_list(hero):
                hero = hero_object()

            difference = dragons[hero] - random_dragon_value

            print("\nYour dragon:", hero, "and has", dragons[hero], "power points!\n" +
                  "Your opponent has", random_dragon_key, "with ", random_dragon_value, "power!\n" +
                  "You have ", difference, "difference.\n")

            if dragons[hero] > random_dragon_value:
                print("You won! +20p\n")
                user_points, computer_points, user_win_scores = win(user_points, computer_points, user_win_scores)

            elif dragons[hero] == random_dragon_value:
                print("Draw. -20p each\n")
                user_points -= 20
                computer_points -= 20

            else:
                print("You lost. -40p\n")
                computer_points, user_points, computer_win_scores = win(computer_points, user_points, computer_win_scores)

            tour_count += 1

            print("Overall situation:\nComputer Points:", computer_points, "\nUser Points:", user_points)
            print("\nEnd of tour", tour_count,"!\n")

            if check_winner():
                wanna_play_again()
                return

            if tour_count % 2 == 0:
                if user_win_scores == 2:
                    print("Congratulations! You won twice in a row, now you are the winner!\n" +
                        "Total scores: ", user_win_scores,", and total point is: ", user_points)

                elif computer_win_scores == 2:
                    print("Computer is the winnder now, since won twice in a row! Congratulations computer!\n" +
                          "Total scores: ", computer_win_scores, ", and total point is: ", computer_points)

                wanna_play_again()

    play()

tas_kagit_makas_OZLEM_NUR_DUMAN()