#
# Tentmakers: Lesson 4-grocery_store 
# Topics covered: lists, dictionaries, loops, for 
#

# Create a virtual grocery store! Grocery store should be able to:
# * Add items to cart
# * Remove items from cart
# * See items in your cart 
# * Check out your order

# For added challenge:
# * Add in the ability to apply a universal discout (20% off--for instance) to your entire order
# * Add in the ability to apply item-specific discounts (20% off milk, for instance)
# * To see the current value of all items in your cart
# * To write the entire program using functions
# * To write a really expansive grocery-store inventory
# * To make your grocery store pleasing aesthetically 

import pdb

cart = {}

class Total(object):
	def __init__(self, total_amount):
		self.total_amount = total_amount
	def add_to_total(self, addition):
		self.total_amount += addition
	def subtract_from_total(self,subtraction):
		self.total_amount -= subtraction

stock = {
'banana' : 1,
'apple' : 10,
'Star Wars DVD' : 4
}

prices = {
'banana' : 1,
'apple' : 2,
'Star Wars DVD' : 8
}

def remove_from_cart():
	remove_item_input= raw_input ("What item would you like to remove? (1 per instance) ")
	print
	if remove_item_input in cart.keys():
		for key in cart:
			if key == remove_item_input:
				if cart[key] > 0:
					total.subtract_from_total(prices[key])
					stock[key] += 1
					cart[key] -= 1
					print "We've removed one %s from your cart."%(key)
					if cart[key] == 0:
						del cart[key]
					print
					see_cart()

				elif cart[key] == 0:
					print "You don't have any %ss in your cart to remove!" %(key)
					print
					see_cart()
	else:
		print "You don't have any %ss in your cart to remove!" %(remove_item_input)
		see_cart()

def see_cart():
	if bool(cart) == False:
		print "You don't have anything in your cart."
		print
	else:
	    print "Your cart contains:"
	    for key in cart:
	    	if cart[key] > 1:
	    		print "%d %ss" %(cart[key], key)
	    	elif cart[key] == 1:
	    		print "%d %s" %(cart[key], key)
	    print
	continue_toggle = False
	while continue_toggle == False:
		remove_from_cart_toggle = raw_input ("Do you want to remove anything from your cart? (Y/N): ")
		remove_from_cart_toggle = remove_from_cart_toggle.upper()
		if remove_from_cart_toggle.upper() == "Y":
			print
			continue_toggle = True
			remove_from_cart()
		elif remove_from_cart_toggle.upper() == "N":
			print
			continue_toggle = True
			shopping()
		else:
			print "Invalid entry"
			print

def check_out():
	if bool(cart) == False:
		print "You didn't buy anything! Oh well."
	else:
	    print "Your cart contains:"
	    for key in cart:
	    	if cart[key] > 1:
	    		print "%d %ss" %(cart[key], key)
	    	elif cart[key] == 1:
	    		print "%d %s" %(cart[key], key)
	    print
	    print "Your order total is $%d" %(total.total_amount)
	    print "Thanks for shopping with us!"

def main_menu():
	print
	main_menu_input = raw_input ("Type 'inventory' to see what is in stock,'prices' to see what everything costs, 'shop' to begin adding items to your cart, or 'end' to check-out: ")
	print
	if main_menu_input=='inventory':
		for key in stock:
			print "We have %d %ss left" % (stock[key], key)
		main_menu()
	elif main_menu_input == 'prices':
		for key in prices:
			print "Each %s costs $%d" % (key, prices[key])
		main_menu()
	elif main_menu_input == 'shop':
		shopping()
	elif main_menu_input == 'end':
		check_out()
	else:
		print "invalid entry"
		main_menu()

def shopping():
	shopping_input = raw_input ("What do you what do buy? Type in your entry now (type 'main menu' to go back, 'cart' to see your cart, or 'end' to check-out): ")
	print
	if shopping_input == 'main menu':
		main_menu()
	elif shopping_input == 'end':
		check_out()
	elif shopping_input == 'cart':
		see_cart()
	else:
		if shopping_input in stock.keys():
			for key in stock:
				if key == shopping_input:
					if stock[key] > 0:
						if key in cart:
							cart[key] += 1
						else:
							cart[key] = 1
						stock[key] -= 1
						total.add_to_total(prices[key])
						print "You just added a %s to your cart! Nice!!" %(key)

					else:
						print "We are out of %s's. Sorry!" %(key)
		else:
			print "You chose something we don't stock! Try Wal-Mart"

		print
		shopping()

print "Welcome to Joe's Mini Mart!"
total = Total(0)
main_menu()

