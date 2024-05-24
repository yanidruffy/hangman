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

def player_check(animal):
    """
    A prompt for the player to choose a letter and check if input is valid.
    """
    player_choice = input("Choose a letter:").lower()
    if not player_choice.isalpha() or len(player_choice) != 1:
        print("Error, try again\n")
        player_check(animal)
    else:
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

def main():
    """
    Main function to start the game.
    """
    print("Welcome Message")
    animal = animal_generator()
    display = display_generator(animal)
    print(animal)
    player_choice = player_check(animal)
    update_display(animal, player_choice, display)
main()
