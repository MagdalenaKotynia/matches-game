# Klasa GameTree umożliwia utworzenie drzewa gry "Zapałki" dla zadanej liczby zapałek oraz głębokości drzewa.

import math


class GameTree(object):
	def __init__(self, depth, is_human_player, matches_list, value=0):
		self.depth = depth
		self.is_human_player = is_human_player
		self.matches_list = list(eval(matches_list))
		self.value = value
		self.children = []
		self.create_children()

	def create_children(self):
		if self.depth < 0:
			return
		for j in range(0, len(self.matches_list)):
			if self.matches_list[j] > 2:
				new_matches_list = self.matches_list[0:j] + self.matches_list[j + 1:]
				new_matches_list.extend([0, 0])
				for i in range(1, math.ceil(self.matches_list[j] / 2)):
					new_matches_list[-2] = i
					new_matches_list[-1] = self.matches_list[j] - i
					self.children.append(GameTree(self.depth - 1, -self.is_human_player, str(new_matches_list),
					                              self.compute_val(new_matches_list)))

	def compute_val(self, val):
		if all(v == 1 or v == 2 for v in val):
			return self.is_human_player
		else:
			return -self.is_human_player
