import math
from collections import Counter
data = Counter(your_list_in_here)

def circumference(radius):
	circ = (radius**2)*math.pi
	return circ

def rectangle_area(side1,side2):
	area=side1*side2
	return area

def sqaure_area(side):
	area=side*side
	return area

def average(numbers):
	lengthof = numbers.length()
	sumof = sum(numbers)
	return sumof/lengthof

def median(numbers):
	lengthof = numbers.length()
	middle=lengthof/2
	if (middle%1 == 0):
		return numbers[(middle-1)]
	else:
		averagemid = (numbers[(middle-.5)]+numbers[(middle+.5)])/2
		return averagemid

def mode(numbers):


# Tier one: create the following functions:
# 1) Circumference of a circle
# 2) Area of a rectangle
# 3) Area of a square
# 4) Area of a trapezoid
# 5) A function that returns that average of a list of numbers
# 6) A function that returns the median of a list of numbers
# 7) A function that returns the mode of a list of numbers

# Challenge! Create the following functions:
# 1) A function that determines if a number is prime
# 2) A function that determines whether the sum of its individual digits exceeds their product
# For instance, the sum of the numbers in 87 is 15 and their product is 54
# 3) A function that determines if something will float. Acceptable params for this function: mass and volume.
# 4) A function that determines how much money you will have in n years given an initial deposit and an interest rate.
# For instance, depositing 100$ at 5% interest interest rate will give you 105$ in one year, 110.25$ in two years, etc.



