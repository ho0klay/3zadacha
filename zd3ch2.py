import random 

class Warrior:
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.armor = 100
		self.stamina = 100


	def attack(self):
		if self.stamina > 0:
			self.stamina -=10
			return True
		else:
			return False	

	def defend(self, damage):
		if self.armor > 0:
			self.health -= random.randint(0, 20)
			self.armor -= random.randint(0, 10)
		else:
			self.health -= random.randint(10, 30)	
		
def battle(unit1, unit2):
	while unit1.health > 10 and unit2.health > 10 :

		action1 = random.choice(['attack', 'defend'])		
		action2 = random.choice(['attack', 'defend'])

		if action1 == 'attack' and action2 == 'attack':
			damage1 = random.randint(10, 30)
			damage2 = random.randint(10, 30)
			unit1.health -= damage2
			unit2.health -= damage1
		elif action1 == 'attack' and action2 == 'defend':
			damage = random.randint(10, 20)
			unit2.defend(damage)
		elif action1 == 'defend' and action2 == 'attack':
			damage = random.randint(10, 20)
			unit1.defend(damage)
		print(f'{unit1.name}: HP = {unit1.health}, Armor = {unit1.armor}, Stamina = {unit1.stamina}')
		print(f'{unit1.name}: HP = {unit2.health}, Armor = {unit2.armor}, Stamina = {unit2.stamina}')
	winner = unit1 if unit1.health > unit2.health else unit2
	print(f'{winner.name} Wins!')	

unit1 = Warrior('Voin 1')
unit2 = Warrior('Voin2')
battle(unit1, unit2)		

		
