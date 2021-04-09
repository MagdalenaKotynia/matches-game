# program uruchamiający Grę w Zapałki

from win_check import win_check
from best_move import best_move


print("\n* * * GRA W ZAPAŁKI * * *")
while True:
	try:
		matches_num = int(input("\nUstal początkową liczbę zapałek: "))
		break
	except ValueError:
		print(
			"\n* * * Podana wartość jest niepoprawna. Spróbuj jeszcze raz! * * *")
		continue

i_depth = matches_num - 1
matches_num = [matches_num]
while True:
	try:
		is_human_player = int(input("\nKto ma rozpocząć grę? Ty: wpisz '1', Komputer: wpisz '-1', : "))
		break
	except ValueError:
		print(
			"\n* * * Podana wartość jest niepoprawna. Spróbuj jeszcze raz! * * *")
		continue

while not all(v == 1 or v == 2 for v in matches_num):

	if win_check(matches_num, is_human_player):

		best_choice = best_move(i_depth, is_human_player, matches_num)
		if is_human_player == 1:
			print("\nTwój ruch: Najlepszy ruch w tym wypadku to podział grupy zapałek o liczności ",
			      best_choice[-2] + best_choice[-1],
			      "na podgrupy o licznościach ", best_choice[-2:])
			while True:
				try:
					group_choice = int(input("\nKtórą grupę chciałbyś rozdzielić?: "))
				except ValueError:
					print(
						"\n* * * Podana wartość jest niepoprawna. Spróbuj jeszcze raz! * * *")
					continue
				if not (group_choice in matches_num):
					print(
						"\n* * * Wybrana grupa nie istnieje w zbiorze grup zapałek. Spróbuj jeszcze raz! * * *")
					continue
				else:
					break

			matches_num.remove(group_choice)

			while True:
				try:
					division_choice = list(
						map(int,
						    input(
							    "\nNa jakie podgrupy chcesz podzielić wybraną grupę zapałek?: ").strip().split()))[
					                  :]
				except ValueError:
					print(
						"\n* * *Podana wartość jest niepoprawna. Wpisz dwie liczby oddzielone spacją. Spróbuj jeszcze raz! * * *")
					continue

				if len(division_choice) != 2:
					print(
						"\n* * *Podzieliłeś grupę inaczej niż na dwie podgrupy. Spróbuj jeszcze raz! * * *")
					continue
				elif division_choice[0] + division_choice[1] != group_choice:
					print(
						"\n* * * Suma liczności podgrup nie zgadza się z licznością grupy. Spróbuj jeszcze raz! * * *")
					continue
				elif division_choice[0] == division_choice[1]:
					print(
						"\n* * * Nie możesz dzielić grupy zapałek na dwie takie same podgrupy. Spróbuj jeszcze raz! * * *")
					continue
				else:
					break
			matches_num.append(division_choice[0])
			matches_num.append(division_choice[1])
			print("\n", matches_num, " - Tak wygląda aktualne pogrupowanie zapałek. ")
			win_check(matches_num, is_human_player)
			is_human_player *= -1
		else:
			print("\nRuch komputera: Komputer dzieli grupę", best_choice[-1] + best_choice[-2],
			      "zapałek na podgrupy ", best_choice[-2:], " zapałek.")
			matches_num = best_choice
			print("\n", matches_num, " - Tak wygląda aktualne pogrupowanie zapałek. ")
			win_check(matches_num, is_human_player)
			is_human_player *= -1