import random

def dice_roll():

	try:
		num_dice = int(input("How many dice?"))
		for i in range(num_dice):
		    yield random.randint(1,6)

	except ValueError:
		print("Error! Please enter a number, not a word!")

for roll in dice_roll():
	print("you rolled %d" %(roll))