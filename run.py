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

def tries_check(animal, player_choice, tries):
    if player_choice not in animal:
        tries -= 1
        print(f"Incorrect, remaining tries: {tries}")
        if tries == 0:
            print("Game Over.")
    return tries

def main():
    """
    Main function to start the game.
    """
    print("Welcome Message")
    animal = animal_generator()
    display = display_generator(animal)
    tries = 7
    print(animal)

    while tries > 0:
        player_choice = valid_check(display)
        display = update_display(animal, player_choice, display)
        tries = tries_check(animal, player_choice, tries)
main()
