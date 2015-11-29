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

cart = {
'banana' : 0,
'apple' : 0,
'Star Wars DVD' : 0
}

class Total(object):
	def __init__(self, total_amount):
		self.total_amount = total_amount
	def add_to_total(self, addition):
		self.total_amount += addition

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

def remove_from_cart(removed_item):
    cart.remove(removed_item)

def see_cart():
    print "Your cart contains:"
    for key in cart:
    	if cart[key] > 1:
    		print "%d %ss" %(cart[key], key)
    	elif cart[key] == 1:
    		print "%d %s" %(cart[key], key)
    print
    shopping(total)

def check_out(total):
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
		shopping(total)
	elif main_menu_input == 'end':
		check_out(total)
	else:
		print "invalid entry"
		main_menu()

def shopping(total):
	shopping_input = raw_input ("What do you what do buy? Type in your entry now (type 'main menu' to go back, 'cart' to see your cart, or 'end' to check-out): ")
	print
	if shopping_input == 'main menu':
		main_menu()
	elif shopping_input == 'end':
		check_out(total)
	elif shopping_input == 'cart':
		see_cart()
	else:
		if shopping_input in stock.keys():
			for key in stock:
				if key == shopping_input:
					if stock[key] > 0:
						cart[key] += 1
						stock[key] -= 1
						total.add_to_total(prices[key])
						print "You just added a %s to your cart! Nice!!" %(key)

					else:
						print "We are out of %s's. Sorry!" %(key)
						print
		else:
			print "You chose something we don't stock! Try Wal-Mart"

		print
		shopping(total)

print "Welcome to Joe's Mini Mart!"
total = Total(0)
main_menu()

