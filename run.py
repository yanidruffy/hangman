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
    A prompt for the player to choose a letter and see if it is entailed within the searched word.
    """
    player_choice = input("Choose a letter:").lower()
    if not player_choice.isalpha():
        print("Error, try again\n")
        player_check(animal)
    else:
        for letter in animal:
            if letter == player_choice:
                print("Correct")
            else:
                print("Incorrect, try again.")


def main():
    """
    Main function to start the game.
    """
    print("Welcome Message")
    animal = animal_generator()
    print(animal)
    player_check(animal)
main()
