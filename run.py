import random
from hangman import LOGO, HANGMAN_PICS, ANIMAL_LIST

def print_introduction(attempts):
    """
    Prints welcome message and instructions of the game.

    Parameters:
        attempts (int): Remaining attempts
    """
    introduction = (
        "Welcome to Hangman!\n\n"
        "Hangman is a simple word guessing game. You are trying to guess the name of an ANIMAL.\n"
        f"You have {attempts} attempts to guess the animal correctly.\n"
        "Good luck.\n"
    )
    print(LOGO)
    print(introduction)

def valid_check(display, letters):
    """
    A prompt for the player to choose a letter and check if input is valid.

    Parameter: 
        display (list): Current display of the word
        letters (set): Already guessed letters

    Returns:
        player_choice (str): Valid choice
    """
    valid_input = False
    while not valid_input:
        player_choice = input("Choose a letter:").lower()
        if not player_choice.isalpha() or len(player_choice) != 1:
            print("Error, try again\n")
        elif player_choice in display or player_choice in letters:
            print(f"Invalid")
        else:
            valid_input = True
    letters.add(player_choice)
    return player_choice

def display_generator(animal):
    """
    Generate initial display for the chosen animal.

    Parameter:
        animal (str): Chosen animal

    Returns:
        display (list): Initial display for the chosen animal
    """

    display = []

    for char in animal:
        display += "_"

    print(display)
    return display

def update_display(animal, player_choice, display):
    """
    Update display based on player's choice.

    Parameters:
        animal (str): Chosen animal
        player_choice (str): Player's valid choice
        display (list): Current display for the chosen animal

    Returns:
        display (list): Updated display
    """
    for i in range(len(animal)):
        letter = animal[i]

        if letter == player_choice:
            display[i] = letter

    print(display)
    return display

def attempts_check(animal, player_choice, attempts, game_loser):
    """
    Check attempts and update game state.

    Parameters:
        animal (str): Chosen animal
        player_choice (str): Player's valid choice
        attempts (int): Remaining attempts
        game_loser (bool): Game state

    Returns:
        attempts, game_loser(tuple): Updated attempts and game state
    """
    if player_choice not in animal:
        attempts -= 1
        print(f"Incorrect, remaining attempts: {attempts}")
        if attempts == 0:
            print("Game Over.")
            game_loser = True
    return attempts, game_loser

def win_condition(display, game_winner):
    """
    Check if player has won the game

    Parameters:
        display (list): Current display for the chosen animal
        game_winner (bool): Game state
    
    Returns:
        game_winner(bool): Updated Game state
    """
    if "_" not in display:
        print("You win.")
        game_winner = True
    
    return game_winner

def main():
    """
    Main function to start the game.
    """
    attempts = 6
    letters = set()
    game_end = False
    
    print_introduction(attempts)
    animal = random.choice(ANIMAL_LIST).lower()
    display = display_generator(animal)
    print(animal)
    while not game_end:
        player_choice = valid_check(display, letters)
        display = update_display(animal, player_choice, display)
        attempts, game_end = attempts_check(animal, player_choice, attempts, game_end)
        print(HANGMAN_PICS[attempts])
        game_end = win_condition(display, game_end)

main()
