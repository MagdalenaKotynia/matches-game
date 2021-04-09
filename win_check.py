# funkcja win_check sprawdza aktualny stan gry

def win_check(matches, is_human_player):
	if all(v == 1 or v == 2 for v in matches):
		print("\n", "* " * 30)
		if is_human_player > 0:
			print(f"\t Twoje zwycięstwo!")
		else:
			print(f"\t Nie możesz już podzielić zapałek, komputer wygrał :(")
		print("* " * 30)
		return 0
	return 1
