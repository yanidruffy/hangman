import random

animal_list = [
    "Alligator",
    "Cheetah",
    "Chimpanzee",
    "Crocodile",
    "Dolphin",
    "Elephant",
    "Flamingo",
    "Giraffe",
    "Hedgehog",
    "Kangaroo",
    "Leopard",
    "Octopus",
    "Orangutan",
    "Ostrich",
    "Penguin",
    "Platypus",
    "Rhinoceros",
    "Seahorse",
    "Starfish",
    "Tortoise"
]

def animal_generator():
    """
    Return random animal from the list.
    """
    return random.choice(animal_list).lower()

def valid_check(display):
    """
    A prompt for the player to choose a letter and check if input is valid.
    """
    valid_input = False
    while not valid_input:
        player_choice = input("Choose a letter:").lower()
        if not player_choice.isalpha() or len(player_choice) != 1:
            print("Error, try again\n")
        elif player_choice in display:
            print(f"Invalid")
        else:
            valid_input = True
    return player_choice

def display_generator(animal):
    display = []

    for char in animal:
        display += "_"

    print(display)
    return display

def update_display(animal, player_choice, display):    
    for i in range(len(animal)):
        letter = animal[i]

        if letter == player_choice:
            display[i] = letter

    print(display)
    return display

def attempts_check(animal, player_choice, attempts, game_loser):
    if player_choice not in animal:
        attempts -= 1
        print(f"Incorrect, remaining attempts: {attempts}")
        if attempts == 0:
            print("Game Over.")
            game_loser = True
    return attempts, game_loser

def win_condition(display, game_winner):
    if "_" not in display:
        print("You win.")
        game_won = True
    
    return game_winner

def main():
    """
    Main function to start the game.
    """
    print("Welcome Message")
    animal = animal_generator()
    display = display_generator(animal)
    attempts = 7
    game_end = False
    print(animal)

    while not game_end:
        player_choice = valid_check(display)
        display = update_display(animal, player_choice, display)
        attempts, game_end = attempts_check(animal, player_choice, attempts, game_end)
        game_end = win_condition(display, game_end)
    
main()
