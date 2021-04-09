#funkcja bst_move zwraca optymalny ruch dla danej fazy gry

from GameTree import GameTree
from minimax import minimax


def best_move(depth, is_human_player, matches):
	game_tree = GameTree(depth, is_human_player, str(matches))
	best_choice = None
	best_value = -is_human_player
	for i in range(len(game_tree.children)):
		child = game_tree.children[i]
		value = minimax(child, depth, -is_human_player)
		if abs(is_human_player * 1 - value) <= abs(is_human_player * 1 - best_value):
			best_value = value
			best_choice = child.matches_list
	return best_choice