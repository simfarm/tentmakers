print "Welcome to Joe's Star Wars trivia game!"

name = raw_input ("Please enter your name: ")
print "Welcome %s!" %name

play_again = "Y"
# "play_again" variable allows you to play multiple games.

while play_again == "Y":
	

	continue_toggle = False
	# "continue_toggle" variable is to ensure proper input.
	
	point = 0
	#point counter for the trivia game.

	while continue_toggle != True:

		print \
		"""
		Question 1:

		According to a recent fan theory, who was originally supposed to be the true "Phantom Menance" in Star Wars Episode I?
		(A) Annakin Skywalker
		(B) Jango Fett
		(C) Jar Jar Binks
		(D) Obi-wan Kenobi
		"""
		# the answer is "C"

		answer=raw_input ("Please enter your answer: ")
		answer=answer.upper()

		if answer == "C":
			print "Correct!"
			point += 1
			continue_toggle = True

		elif answer == "A":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "B":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "D":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		else:
			print "Invalid entry - try again"

	continue_toggle = False

	while continue_toggle != True:

		print \
		"""
		Question 2:

		What thing did Luke target with his Skyhopper back on Tatooine? 
		(A) Cacti 
		(B) Ootini
		(C) Droids
		(D) Womp rats
		"""

		#the answer is "D"

		answer=raw_input ("Please enter your answer: ")
		answer=answer.upper()

		if answer == "D":
			print "Correct!"
			point += 1
			continue_toggle = True

		elif answer == "A":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "B":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "C":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		else:
			print "Invalid entry - try again"

	continue_toggle = False

	while continue_toggle != True:

		print \
		"""
		Question 3:

		What rebel spaceship was fast/agile but had very little armor? 
		(A) Y-Wing 
		(B) X-Wing
		(C) A-Wing
		(D) Z-Wing
		"""

		#the answer is "C"

		answer=raw_input ("Please enter your answer: ")
		answer=answer.upper()

		if answer == "C":
			print "Correct!"
			point += 1
			continue_toggle = True

		elif answer == "A":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "B":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "D":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		else:
			print "Invalid entry - try again"

	continue_toggle = False

	while continue_toggle != True:

		print \
		"""
		Question 4:

		What creature was originally meant to inhabit Endor? 
		(A) Eewoks 
		(B) Jawas
		(C) Wookies
		(D) Clones
		"""

		#the answer is "C"

		answer=raw_input ("Please enter your answer: ")
		answer=answer.upper()

		if answer == "C":
			print "Correct!"
			point += 1
			continue_toggle = True

		elif answer == "A":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "B":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "D":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		else:
			print "Invalid entry - try again"

	continue_toggle = False

	while continue_toggle != True:

		print \
		"""
		Question 5:

		The actor who played Wedge Antilles is the uncle of which Star Wars character's actor/actress?
		(A) Qui-Gon 
		(B) Young Obi-wan
		(C) R2-D2
		(D) C-3PO
		"""

		#the answer is "B"

		answer=raw_input ("Please enter your answer: ")
		answer=answer.upper()

		if answer == "B":
			print "Correct!"
			point += 1
			continue_toggle = True

		elif answer == "A":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "C":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		elif answer == "D":
			print "That's wrong - sorry dude!"
			continue_toggle = True

		else:
			print "Invalid entry - try again"

	print "You scored %d out of 5 points" % point

	if point==5:
		print "Indeed you are powerful as Obi-wan forsaw"

	elif point==4:
		print "The force is strong with you...but you are not a Jedi yet..."

	elif point==3:
			print "You are too old...too old to become a Jedi"

	elif point==2:
		print "Better stick to a blaster"

	else:
		print "Aren't you a little short for a storm trooper?"

	play_again = raw_input ("Do you want to play again (Y/N): ")
	play_again = play_again.upper()

print "Thanks for playing!"
