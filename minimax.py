def minimax(game_tree, depth, is_max_player):
	if depth == 0:
		return game_tree.value
	if is_max_player == 1:
		best_value = -1

		for child in game_tree.children:
			value = minimax(child, depth - 1, -is_max_player)
			best_value = max(best_value, value)

		return best_value
	else:
		best_value = 1
		for child in game_tree.children:
			value = minimax(child, depth - 1, -is_max_player)
			best_value = min(best_value, value)

		return best_value
