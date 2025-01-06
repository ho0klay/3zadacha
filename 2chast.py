import random

class Warrior:

	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 20

	def attack(self, enemy):
		if enemy.health > 0:
			enemy.health -= self.damage
			print(f'{self.name} аттакует {enemy.name} и наносит {self.damage} урона! у {enemy.name} осталось {enemy.health} здоровья')
		else:
			print(f'{enemy.name} уже мертв!')

def battle(unit1, unit2):
	while unit1.health > 0 and unit2.health > 0:
		attacker = random.choice([unit1, unit2])
		if attacker == unit1:
			unit1.attack(unit2)
		else:
			unit2.attack(unit1)	

	if unit1.health <= 0 and unit2.health <= 0:
		print('Ничья!')

	elif unit1.health <= 0:
		print(f'{unit2.name} победил!')

	else:
		print(f'{unit1.name} победил!')	

unit1 = Warrior('1')
unit2 = Warrior('2')
battle(unit1, unit2)
			
   		