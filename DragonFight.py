import random

monsters = {
    "Dragon": 1900,
    "Griffin": 1500,
    "Phoenix": 1700,
    "Kraken": 2000,
    "Manticore": 1600,
    "Basilisk": 1700,
    "Hydra": 1850,
    "Chimera": 1550,
    "Werewolf": 1450,
    "Cyclops": 1800
}

print("Welcome to the DragonFight game! " +
      "\nThere are some dragons and each of them has some amount of power points." +
      "\nSo you need to pick your hero carefully.\n")

print("These are the dragons: \n", ', '.join(monsters.keys()), ".\n\nDo not forget you cannot pick the same type of dragon as your opponent.\n\n")

user_points = 200
computer_points = 200

def generate_random_monster():
    global random_monster_key, random_monster_value
    random.seed(42)  # Correctly seed the random number generator
    random_monster_key = random.choice(list(monsters.keys()))
    random_monster_value = monsters[random_monster_key]

def is_hero_in_list(hero):
    if hero not in monsters:
        print("Please enter a valid hero name.")
        return False
    return True

def are_the_heros_same(user_hero, computer_hero):
    if user_hero == computer_hero:
        print("You cannot use the same hero as your component!")
        return False
    else:
        return True

def wanna_play_again():
    print("Do you want to play once more? If yes, enter 'y':")
    decision = input()
    if decision.lower() == "y":
        print("You have a good level of confidence!\n")
        play()
    else:
        print("It was nice to play with you. Hope to see you next time!")

def play():
    global user_points, computer_points, random_monster_key

    for i in range(5):
        generate_random_monster()

        print("Your opponent is", random_monster_key, ". Pick your fighter!\n")
        hero = input().capitalize()

        if not is_hero_in_list(hero):
            continue

        if not are_the_heros_same(hero, random_monster_key):
            continue

        print("Your dragon:", hero, "and has", monsters[hero], "power points!\n" +
              "Your opponent has", random_monster_value, "\n")

        if monsters[hero] > random_monster_value:
            print("You won! +40p\n")
            user_points += 40
            computer_points -= 40

        elif monsters[hero] == random_monster_value:
            print("Draw. -20p each\n")
            user_points -= 20
            computer_points -= 20

        else:
            print("You lost. -40p\n")
            user_points -= 40
            computer_points += 40

        print("Overall situation:\nComputer Points:", computer_points, "\nUser Points:", user_points)
        print("\nEnd of tour", i + 1, "!\n")

    print("Finish! Let's see who won.\n" +
          "You:", user_points, "\nComputer:", computer_points)

    if user_points > computer_points:
        print("Congratulations! You won!\n")
        wanna_play_again()

    elif user_points == computer_points:
        print("It's a draw. You have to play once more to break this.")
        play()

    else:
        print("Unfortunately, you are defeated by the computer.")
        wanna_play_again()

play()
