import random
# declaring globals
global size
global speed
global languages

def main():
	#will do the creation here
	print("Hello, welcome to py-character, the python stat rolling simulator!")
	char_name = input("First, what is your character's name?\n")

	while True:
		species = input("Next, what is your character's race? \n Choose: Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half elf, Half orc, or Tiefling\n")
		# checking the user input
		# first, I want to make sure that if there is a dash in half-elf or half orc, it is removed
		species = species.replace('-',' ')
		# Next, making the inputs lowercase to simplify string matching
		species = species.lower()
		#finally, insuring that the users input a valid race
		valid_species = ["dwarf", "elf", "halfling", "human", "dragonborn", "gnome", "half elf", "half orc", "tiefling"]
		if species not in valid_species:
			print("Please choose a valid race")
		else:
			break

	# get subraces for each species with a subrace
	race = get_subrace(species)
    # get the bonuses for that race/subrace
	racial_characteristics(race)
	print("The bonuses that you get from being a %s are: " %(race))
	print(bonuses)
	# also printing any proficiencies the player gets from their race
	if len(proficiencies) > 0:
		print("The skill proficiencies that you get from being a %s are: "%(race))
		print(proficiencies)

	while True:
		the_class = input("Last question, what is your class? \n Choose Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, or Wizard\n")
		'''checking the validity of the input, first by making the input lowercase
		to simplify string comparison'''
		match_class = the_class.lower()
		# next, checking if it is in a list of valid classes
		valid_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
		if match_class not in valid_classes:
			print("you did not input a valid class, please try again")
		else:
			break

	stat_list = [stat_roll() for i in range(6)]
	print("Here are your rolls:")
	print(stat_list)

	# Having the player assign their rolls to their stats
	print("now it's time to assign your rolls to your stats")
	print("The stats that you can choose are strength, dexterity, constitution, intelligence, wisdom, and charisma")
	print("For each roll, you need to assign it to one of your stats \n choose str, dex, con, int, wis, or char")
	stat_assignment(race,stat_list)

	# getting the hit points for the character
	class_characteristics(the_class)
	print(proficiencies)

	# returning the player object
	print("And here is your finished character")
	character_info(char_name,race,the_class)


def get_subrace(race):
	#having the user specify subrace if any
	if race in "dwarf":
		size = "medium"
		speed = 25
		languages = ["common", "dwarvish"]
		subrace = input("is this a hill dwarf or a mountain dwarf?\n")
		race = subrace.lower()
	elif race in "elf":
		size = "medium"
		speed = 30
		languages = ["common", "elvish"]
		subrace = input("is this a high elf, a wood elf, or a dark elf?\n")
		race = subrace.lower()
	elif race in "halfing":
		size = "small"
		speed = 25
		languages = ["common", "halfling"]
		subrace = input("is this a stout halfing or a lightfoot halfling?\n")
		race = subrace.lower()
	elif race in "gnome":
		size = "small"
		speed = 25
		languages = ["common", "gnomish"]
		subrace = input("is this a forest gnome or a rock gnome?\n")
		race = subrace.lower()
	else:
		pass
	return race


def stat_roll():
	#simulating rolling a d6 4 times
	roll_list = []
	for j in range(4):
		roll_list.append(random.randint(1,6))

	#dropping the lowest number and getting the total
	roll_list.remove(min(roll_list))
	roll = sum(roll_list)
	return roll


def stat_assignment(race,rolls):
	# this is where I will make the stat assignments
	global char_stats
	# a dictionary of stats to be filled in by key by the user
	char_stats = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "char": 0}
	'''a list of strings of the already chosen keys to help the user keep track 
	of what they have assigned'''

	already_chosen = []
	count = 1
	for roll in rolls:
		print("roll %d is %d" %(count, roll))
		if len(already_chosen) > 0:
			print("you have already assigned %s" %(already_chosen))

		# making sure that the user choice is valid and non-repeating
		while True:
			player_choice = input("where do you want to assign this?\n")
			if player_choice not in char_stats.keys():
				# making sure the input is valid
				print("that was not a valid input. Please chose str, dex, con, int, wis, or char")
				continue
			if player_choice in already_chosen:
				# making sure the input isn't repeating a choice
				print("You have already chosen your %s stat, please choose a different one"%(player_choice))
				continue
			else:
				# the player has entered a valid non-repeating stat
				# we can exit the loop
				break

		# implementing the user's choice
		that_bonus = bonuses.get(player_choice)
		total = roll + that_bonus
		char_stats[player_choice] = total
		already_chosen.append(player_choice)
		print("your %s is %d"%(player_choice,total))
		count +=1
		
	
def racial_characteristics(race):
	# This is where I will make and fill the dictionary of racial bonuses
	global bonuses
	global proficiencies
	proficiencies = []
	bonuses = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "char": 0}
	if "hill dwarf" in race:
		bonuses.update({"con" : 2, "wis" : 1})
	if "mountain dwarf" in race:
		bonuses.update({"con" : 2, "str" : 2})
	if "high elf" in race:
		bonuses.update({"dex" : 2, "int" : 1})
		proficiencies.append("perception")
	if "wood elf" in race:
		bonuses.update({"dex" : 2, "wis" : 1})
		proficiencies.append("perception")
	if "dark elf" in race:
		bonuses.update({"dex" : 2, "char" : 1})
		proficiencies.append("perception")
	if "lightfoot halfling" in race:
		bonuses.update({"dex" : 2, "char" : 1})
	if "stout halfling" in race:
		bonuses.update({"dex" : 2, "con" : 1})
	if "human" in race:
		bonuses.update({"str" : 1, "dex" : 1, "con" : 1, "int" : 1, "wis" : 1, "char" : 1})
		size = "medium"
		speed = 30
		languages = ["common"]
	if "dragonborn" in race:
		bonuses.update({"str" : 2, "char" : 1})
		size = "medium"
		speed = 30
		languages = ["common", "draconic"]
	if "forest gnome" in race:
		bonuses.update({"int" : 2, "dex" : 1})
	if "rock gnome" in race:
		bonuses.update({"int": 2, "con" : 1})
	if "half elf" in race:
		bonuses["char"] = 2
		#having the users choose the two other bonuses they get
		print("half elves get to choose two other ablity scores to increase by one point each")
		ability_choices = input("choose two of str, dex, int, con, wis\n")
		#splitting the single string into a list of two strings (the two diff ability scores)
		if "," in ability_choices:
			choice_list = ability_choices.split(",")
		else:
			choice_list = ability_choices.split(" ")
		#going through list and checking that the option is valid and not char again
		valid_abilities = ["str", "dex", "con", "int", "wis"]
		while True:
			for choice in choice_list:
				if choice not in valid_abilities:
					print("%s is not a valid choice" %(choice))
					new_choice = input("please choose one of str, dex, con, int wis\n")
					choice_list.remove(choice)
					choice_list.append(new_choice)
			break
		#using choice_list to update the bonuses dictionary
		for choice in choice_list:
			bonuses[choice] = 1
		#having the users choose two extra proficiencies
		print("Half-elves also get proficiency in two skills of their choice")
		skill_choices = input("choose two of: Acrobatics, Animal Handling, Arcana,\nAthletics, Deception, History,\nInsight, Intimidation, Medicine,\nNature, Perception, Performance,\nReligion, Sleight of Hand, Stealth, or Survival\n")
		#formatting into a list of easily comparable strings
		skill_choices.lower()
		if "," in skill_choices:
			skill_list = skill_choices.split(",")
		else:
			skill_list = skill_choices.split(" ")
		#checking that the user choices are valid:
		valid_skills = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "medicine", "nature", "perception", "performance", "religion", "sleight of hand", "stealth", "survival"]
		while True:
			for choice in skill_list:
				if choice not in valid_skills:
					print("%s is not a valid skill" %(choice))
					new_choice = input("please choice a skill from the list above\n")
					skill_list.remove(choice)
					skill_list.append(new_choice)
			break
		#using skill_list to update the list of proficiencies
		proficiencies.extend(skill_list)
		size = "medium"
		speed = 30
		languages = ["common", "elvish"]
	if "half orc" in race:
		bonuses.update({"str" : 2, "con" : 1})
		size  = "medium"
		speed = 30
		languages = ["common", "orc"]
		proficiencies.append("Intimidation")
	if "tiefling" in race:
		bonuses.update({"int" : 1, "char" : 2})
		size = "medium"
		languages = ["common", "infernal"]


def character_info(name,race,job):
	# a function to creare a object containing all the player info
	class DnD_Character(object):
		"""creating a class to hold basic info and stats for a DnD Character. Name, 
		race, and class have been passed in, the stats come from the char_stats
		dictionary, which is a global variable"""
		def __init__(self, name, race, playerclass, hit_points, strength, dexterity, constitution, intelligence, wisdom, charisma, proficiencies):
			#super(DnD_Character, self).__init__(name,race, playerclass, strength, dexterity, constitution, intelligence, wisdom, charisma)
		    self.name = name
		    self.race = race
		    self.playerclass = job
		    self.hit_points = hit_points
		    self.strength = strength
		    self.dexterity = dexterity
		    self.constitution = constitution
		    self.intelligence = intelligence
		    self.wisdom = wisdom
		    self.charisma = charisma
		    self.proficiencies = proficiencies

		def __str__(self):
			return "name: %s\nrace: %s\nclass: %s\nhit points: %s\nstrength: %s\ndexterity: %s\nconstitution: %s\nintelligence: %s\nwisdom: %s\ncharisma: %s\nproficiencies: %s\n" %(self.name,self.race,self.playerclass,self.hit_points,self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma,self.proficiencies)

	# using the information given to create an object of class DnD character
	playercharacter = DnD_Character(name,race,job,hit_points,char_stats["str"],char_stats["dex"],char_stats["con"],char_stats["int"],char_stats["wis"],char_stats["char"],proficiencies)
	print(playercharacter)


def class_characteristics(char_class):
	global hit_points
	if "barbarian" in char_class:
		class_points = 12
		#getting barbarian proficiencies
		barbarian_skills = input("choose two of the following skills to become proficient in:\nAnimal handling, Athletics, Intimidation, Nature, Perception, or Survival\n")
		#parsing the string into a list of choices
		barbarian_skills.lower()
		if "," in barbarian_skills:
			barbarian_choices = barbarian_skills.split(",")
		else:
			barbarian_choices = barbarian_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		barbarian_valid = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"]
		while True:
			for choice in barbarian_choices:
				if choice not in barbarian_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					barbarian_choices.remove(choice)
					barbarian_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					barbarian_choices.remove(choice)
					barbarian_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(barbarian_choices)
	if "bard" in char_class:
		class_points = 8
		#getting bard proficiencies
		bard_skills = input("choose three of the following skills to become proficient in:\nAcrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Medicine, Nature, Perception, Performance, Religion, Sleight of Hand, Stealth, or Survival\n")
		#parsing the string into a list of choices
		bard_skills.lower()
		if "," in bard_skills:
			bard_choices = bard_skills.split(",")
		else:
			bard_choices = bard_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		bard_valid = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "medicine", "nature", "perception", "performance", "religion", "sleight of hand", "stealth", "survival"]
		while True:
			for choice in bard_choices:
				if choice not in bard_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					bard_choices.remove(choice)
					bard_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					bard_choices.remove(choice)
					bard_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(bard_choices)
	if "cleric" in char_class:
		class_points = 8
		cleric_skills = input("choose two of the following skills to become proficient in:\nHistory, Insight, Medicine, Persuasion, Religion\n")
		#parsing the string into a list of choices
		cleric_skills.lower()
		if "," in cleric_skills:
			cleric_choices = cleric_skills.split(",")
		else:
			cleric_choices = cleric_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		cleric_valid = ["history", "insight", "medicine", "persuasion", "religion"]
		while True:
			for choice in cleric_choices:
				if choice not in cleric_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					cleric_choices.remove(choice)
					cleric_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					cleric_choices.remove(choice)
					cleric_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(cleric_choices)
	if "druid" in char_class:
		class_points = 8
		druid_skills = input("choose two of the following skills to become proficient in:\nArcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival\n")
		#parsing the string into a list of choices
		druid_skills.lower()
		if "," in druid_skills:
			druid_choices = druid_skills.split(",")
		else:
			druid_choices = druid_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		druid_valid = ["arcana", "animal handling", "insight", "medicine", "nature", "perception", "religion", "survival"]
		while True:
			for choice in druid_choices:
				if choice not in druid_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					druid_choices.remove(choice)
					druid_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					druid_choices.remove(choice)
					druid_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(druid_choices)
	if "fighter" in char_class:
		class_points = 10
		fighter_skills = input("choose two of the following skills to become proficient in:\nAcrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, Survival\n")
		#parsing the string into a list of choices
		fighter_skills.lower()
		if "," in fighter_skills:
			fighter_choices = fighter_skills.split(",")
		else:
			fighter_choices = fighter_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		fighter_valid = ["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"]
		while True:
			for choice in fighter_choices:
				if choice not in fighter_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					fighter_choices.remove(choice)
					fighter_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					fighter_choices.remove(choice)
					fighter_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(fighter_choices)
	if "monk" in char_class:
		class_points = 8
		monk_skills = input("choose two of the following skills to become proficient in:\nAcrobatics, Athletics, History, Insight, Religion, Stealth\n")
		#parsing the string into a list of choices
		monk_skills.lower()
		if "," in monk_skills:
			monk_choices = monk_skills.split(",")
		else:
			monk_choices = monk_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		monk_valid = ["acrobatics", "athletics", "history", "insight", "religion", "stealth"]
		while True:
			for choice in monk_choices:
				if choice not in monk_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					monk_choices.remove(choice)
					monk_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					monk_choices.remove(choice)
					monk_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(monk_choices)
	if "paladin" in char_class:
		class_points = 10
		paladin_skills = input("choose two of the following skills to become proficient in:\nAthletics, Insight, Intimidation, Medicine, Persuasion, Religion\n")
		#parsing the string into a list of choices
		paladin_skills.lower()
		if "," in paladin_skills:
			paladin_choices = paladin_skills.split(",")
		else:
			paladin_choices = paladin_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		paladin_valid = ["athletics", "insight", "intimidation", "medicine", "persuasion", "religion"]
		while True:
			for choice in paladin_choices:
				if choice not in paladin_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					paladin_choices.remove(choice)
					paladin_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					paladin_choices.remove(choice)
					paladin_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(paladin_choices)
	if "ranger" in char_class:
		class_points = 10
		ranger_skills = input("choose three of the following skills to become proficient in:\nAnimal Handling, Athletics, Insight, Investigation, Nature, Stealth, Survival\n")
		#parsing the string into a list of choices
		ranger_skills.lower()
		if "," in ranger_skills:
			ranger_choices = ranger_skills.split(",")
		else:
			ranger_choices = ranger_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		ranger_valid = ["animal handling", "athletics", "insight", "ivestigation", "nature", "perception", "stealth", "survival"]
		while True:
			for choice in ranger_choices:
				if choice not in ranger_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					ranger_choices.remove(choice)
					ranger_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					ranger_choices.remove(choice)
					ranger_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(ranger_choices)
	if "rogue" in char_class:
		class_points = 8
		rogue_skills = input("choose four of the following skills to become proficient in:\nAcrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, Stealth\n")
		#parsing the string into a list of choices
		rogue_skills.lower()
		if "," in rogue_skills:
			rogue_choices = rogue_skills.split(",")
		else:
			rogue_choices = rogue_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		rogue_valid = ["acrobatics", "athletics", "deception", "insight", "intimidation", "ivestigation", "perception", "performance", "persuasion", "sleight of hand", "stealth"]
		while True:
			for choice in rogue_choices:
				if choice not in rogue_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					rogue_choices.remove(choice)
					rogue_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					rogue_choices.remove(choice)
					rogue_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(rogue_choices)
	if "sorcerer" in char_class:
		class_points = 6
		sorcerer_skills = input("choose two of the following skills to become proficient in:\nArcana, Deception, Insight, Intimidation, Persuasion, Religion\n")
		#parsing the string into a list of choices
		sorcerer_skills.lower()
		if "," in sorcerer_skills:
			sorcerer_choices = sorcerer_skills.split(",")
		else:
			sorcerer_choices = sorcerer_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		sorcerer_valid = ["arcana", "deception", "insight", "intimidation", "persuasion", "religion"]
		while True:
			for choice in sorcerer_choices:
				if choice not in sorcerer_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					sorcerer_choices.remove(choice)
					sorcerer_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					sorcerer_choices.remove(choice)
					sorcerer_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(sorcerer_choices)
	if "warlock" in char_class:
		class_points = 8
		warlock_skills = input("choose two of the following skills to become proficient in:\nArcana, Deception, History, Intimidation, Investigation, Nature, Religion\n")
		#parsing the string into a list of choices
		warlock_skills.lower()
		if "," in warlock_skills:
			warlock_choices = warlock_skills.split(",")
		else:
			warlock_choices = warlock_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		warlock_valid = ["arcana", "deception", "history", "intimidation", "invstigation", "nature", "religion"]
		while True:
			for choice in warlock_choices:
				if choice not in warlock_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					warlock_choices.remove(choice)
					warlock_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					warlock_choices.remove(choice)
					warlock_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(warlock_choices)
	if "wizard" in char_class:
		class_points = 6
		wizard_skills = input("choose two of the following skills to become proficient in:\nArcana, History, Insight, Investigation, Medicine, Religion\n")
		#parsing the string into a list of choices
		wizard_skills.lower()
		if "," in wizard_skills:
			wizard_choices = wizard_skills.split(",")
		else:
			wizard_choices = wizard_skills.split(" ")
		#checking if the user makes valid, not repetitive choices
		wizard_valid = ["arcana", "history", "insight", "invstigation", "medicine", "religion"]
		while True:
			for choice in wizard_choices:
				if choice not in wizard_valid:
					new_choice = input("%s is not a valid choice, please choice another from the above list\n"%(choice))
					wizard_choices.remove(choice)
					wizard_choices.append(new_choice)
				if choice in proficiencies:
					new_choice = input("You are already proficient in %s, please choice another from the above list\n"%(choice))
					wizard_choices.remove(choice)
					wizard_choices.append(new_choice)
			break
		#adding the user choices to the proficiencies list
		proficiencies.extend(wizard_choices)

	hit_points = class_points + char_stats["con"]

main()