#!/usr/bin/python

name = raw_input("What is your name? ")
inventory = ['shield', 'breastplate', 'sword', 'scabbard'] 
land = 0

def introduction():
    # introducing setting
    print "|||||||||||||||||||||||||||||||||||"
    print "You are an intrepid knight of the name %s." % name
    print "He is loyal, brave, and sacrificial."
    print "There is a tyrant king named Josephius Flavius who threatens to take over the land."
    print "We want to prepare to fight back."
    # solicit user choice
    choice = None
    while choice not in ['prepare', 'warn']:
        choice = raw_input("What would you like to do? 1) PREPARE yourself 2) WARN the townspeople. ")
        choice = choice.lower()

        # direct to other scenes
        if choice == 'prepare':
            meditate()
        elif choice == 'warn':
            warn1()
        else:
            print "We don't speak that kind of nonsense in these part."

def meditate():
    print "I've set my face like flint towards the prize."
    print "It's now time to warn the people."
    warn1()

def warn1():
    print "The people are freaking out but are willing to take our side."
    print "The kids are crying their tears out and their parents are worrying."

    # solicit user input
    choice = None
    while choice not in ['others', 'home']:
        choice = raw_input("What would you like to do? 1) tell them to go HOME 2) tell them to tell OTHERS. ")
        choice = choice.lower()

        # direct to other scenes
        if choice == 'others':
            warn2()
        elif choice == 'home':
            go_home()
        else:
            print "We don't speak that kind of nonsense in these parts."

def go_home():
    print "The king has been alerted to your rebellion."
    print "Since you have dismissed your troops, you are easily squashed by the kings men."
    print "You lose. Try again."

def warn2():
    print "We finally increased the number of people in our group."
    print "Courage steels our hearts."

    # solicit user input
    choice = None
    while choice not in ['equip', 'tell']:
        choice = raw_input("What would you like to do? 1) tell them to TELL others 2) EQUIP the people.")
        choice = choice.lower()

        # direct to other scenes
        if choice == 'equip':
            equip()
        elif choice == 'tell':
            warn3()
        else:
            print "We don't speak that kind of nonsense in these parts."

def warn3():
    print "It wasn't the best day for us because the king discovered us and crushed our rebellion."
    print "You lose try again."

def equip():
    print "Our army is prepared."
    print "Our army is mighty and strong."
    print "We are ready to defeat the the king."

    # solicit user input
    choice = None
    while choice not in ['attack', 'towns']:
        choice = raw_input("What would you like to do? 1) to ATTACK the king 2) to take some TOWNS.")
        choice = choice.lower()

        # direct to other scenes
        if choice == 'attack':
            victory()
        elif choice == 'towns':
            towns()
        else:
            print "We don't speak that kind of nonsense in these parts."

def towns():
	print "The king's army showed up and we died."
	print "Sorry you lose try again."

def victory():
    print "Finally the king's army takes our side."
    print "Yay we finally won."

introduction()
