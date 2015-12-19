#
# Tentmakers: Lesson 6-final_project
# Topics covered: everything
#

#
# Project: create an interactive story game! The story should be interactive depending on user input.
# * For an example, see files/interactive_story.png
# * Story may be as indepth as you want it to be. However, story should have a minimum of seven possible tiles (events).
# * Tiles should be each written as functions. Event functions should call other event functions.
#

# Sample construction

#!/usr/bin/python
import random
import sys

# set story default values
name = raw_input("What is your name? ")
inventory = ["rope", "pistol", "map"]
money = 5
crew = []

# print story header
print "|||||||||||||||||||||||||||||||||||||||||||||"

def introduction():
    '''Sets the setting.'''
    # setting
    print "You are an adventurer in the American West. The year is 1863 and you are filled with hope."
    print "You have left your hometown in search of a better life."

    # break
    raw_input("Press enter to continue ")
    print ""

    # announcing character specific values
    print "Your name is %s." % name
    print "You have the following in your inventory: %s." % inventory
    print "You have %s dollars to your name." % str(money)

    if not crew:
        print "You are alone."
    else:
        print "This is your crew: %s." % crew

    # break
    raw_input("Press enter to continue ")
    print ""

    # solicit user input
    choice = None
    while choice not in ['explore', 'move', 'talk']:
        choice = raw_input("What would you like to do? 1) EXPLORE town 2) MOVE on 3) TALK to locals ")
        choice = choice.lower()

        # direct to other scenes
        if choice == 'explore':
            explore()
        elif choice == 'move':
            move()
        elif choice == 'talk':
            talk()
        else:
            print "We don't speak that kind of nonsense in these parts."

def explore():
    '''Initial exploration scene.'''
    print "You see some smoke in the distance. It looks like there was a fight."

    # solicit user input
    choice = None
    while choice not in ['see', 'move']:
        choice = raw_input("What would you like to do? 1) SEE what happened 2) MOVE on. ")
        choice == choice.lower()

        if choice == 'see':
            print 'It looks like a fight broke out. While looting the remains, you find: ammunition and gloves.'
            inventory.append('ammunition')
            inventory.append('gloves')
        elif choice == 'move':
            print 'You return to town.'
        else:
            print "We don't speak that kind of nonsense in these parts."
        print ""

        # return to town
        # initial_town()

def move():
    '''Initial progress West.'''
    print "You venture west until running into a river."

    # solicit user input
    choice = None
    while choice not in ['ford', 'wait']:
        choice = raw_input("What would you like to do? 1) attempt to FORD the river 2) WAIT for the current to dip. ")
        choice == choice.lower()

        if choice == 'ford':
            # generate a random number to determine the outcome.
            outcome = random.random()
            if outcome < .5:
                print "You make it safely across the river."
                # next_town()
            else:
                print "Your raft overturns. You are dead."
                raw_input("Press enter to continue. ")

                # exit the game
                sys.exit(0)
        elif choice == 'wait':
            print "The water levels have dropped. You safely cross."
        else:
            print "We don't speak that kind of nonsense in these parts."

        # invoke next scene
        # next_town()

def talk():
    '''Talking to the locals from the first town.'''
    pass

# invoke story
introduction()
