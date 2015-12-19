#
# Tentmakers: Lesson 5-rock_paper_scissors
# Topics covered: imports, functions, dictionaries
#

# Project: Create a rock-paper-scissors game!
# The game should be able to take a person's choice, a computer's choice, decide who wins, and keep track of stats.

# The following functions need to be written:
# * get_computer_choice()
# * determine_winner(person_choice, computer_choice)
# * update_statistics(winner):
# * see_stats()

# For added challenge:
# * At the beginning of the game ask the person how many games the person wants
#   to play (best of 5 or best of 9, etc.) and end the game when the person or
#   the computer has won that many times.
# * Create a function to start a new game at any point in the current game
# * Allow a person to choose a username that is used throughout the game

# A simple (and incomplete) construction:

#!/usr/bin/python

# We need the Python random library to run this game, so we import it here
import random

# Statistics dictionary: how many games won
statistics_dictionary = {
    'person': 0,
    'computer': 0
}


# The main program function
def context_menu():
    print "Welcome to CTTT - the Clam Tic Tac Toe Game!"

    # The person's choice of what to do
    play_game = None
    while play_game != 'quit':
        play_game = raw_input("Type 'start' to start game vs. Clam Computer\n")
        if play_game == "start":
            run_game()

# Run the tic tac toe game
def run_game():
    choice = None
    while choice != 'quit':
        choice = raw_input("Type 'n' for next round, or 'stats' to see the statistics.\n")
        if choice == "n":
            next_round()
        elif choice == "stats":
            see_stats()
        else:
            print "What? I didn't understand that"

def next_round():
    """The next round of the game"""
    print "---------------The next round vs...Clam Computer!!!---------------"
    # Get person's choice
    person_choice = 'No choice'
    while person_choice.lower() not in ['rock', 'paper', 'scissors']:
        person_choice = raw_input("What do you want to throw? Type 'rock', 'paper', or 'scissors'\n")
        if person_choice not in ['rock', 'paper', 'scissors']:
            print "Choice not understood"

    # Get the computer's choice
    computer_choice = get_computer_choice()

    # Determine the winner
    winner = determine_winner(person_choice, computer_choice)

    # Update the statistics based on who won the round
    update_statistics(winner)

def see_stats():
    """Prints out current statistics of how many games have been won"""
    # Write logic here

def get_computer_choice():
    # A random integer between 1 and 3
    random_int = random.randint(1,3)

    # Write logic here. Use the random_int to make a choice for the computer.
    # Make sure to return the computer's choice

def determine_winner(person_choice, computer_choice):
    """Determines winner based on the person's choice and computer's choice"""
    # Write logic here. Make sure to return the winner - person or computer

def update_statistics(winner):
    """Update the statistics_dictionary based on who won the game"""
    # Write logic here

# Run the program
context_menu()
