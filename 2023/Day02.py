import math

# Fetch input data
with open('2023/input.txt', 'r') as input: input = [x.strip() for x in input.readlines()]

class Game:

	def __init__(self, id, rounds) -> None:
		self.id = id
		self.rounds = rounds
	
	def round_max(self) -> dict:
		round_max = {'red': 0, 'blue': 0, 'green': 0}
		
		for round in self.rounds:
			for draw in round.split(','):
				quanity, colour = draw.split()
				if int(quanity) > round_max[colour]:
					round_max[colour] = int(quanity)

		return round_max
	
	def p1(self):
		max = self.round_max()
		return not(max['red'] > 12 or max['green'] > 13 or max['blue'] > 14)
	
	def p2(self):
		max = self.round_max()
		return math.prod(max.values())


valid_IDs_toal = 0
powers= 0

for line in input:
	id, game = line.split(':')
	game = Game(id=int(id[5:]), rounds=game.split(';'))

	if game.p1():
		valid_IDs_toal += game.id

	powers += game.p2()

# Part 1 Answer
print(valid_IDs_toal)

# Part 2 Answer
print(powers)
