import random

def main():
	#getting the user inputs and creating the counter for the dice total
    dice_num = int(input("How many dice? "))
    dice_type = input("What kind of dice? d20,d12,d10,d8,d6,d4 ")
    total = 0

    #figuring out what type of dice
    sides = int(''.join(filter(str.isdigit, dice_type)))

    #calling the dice roll generator and printing the results
    for roll in roll_dice(dice_num,sides):
     	print("You rolled %d!" %roll)
     	total = total + roll
    print("Your total is %d!" %total)


def roll_dice(num,sides):
	for i in range(num):
		yield random.randint(1,sides)

main()