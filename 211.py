def game_21():
    print("Игроки по очереди называют 1-3 числа.\nКто произнесёт 21 — проиграл, остальные кричат 'Ура!'")
    current = 0
    player = 1
    while current < 21:
        print(f"\nТекущий счёт: {current}. Ход игрока {player}.")
        try:
            take = int(input("Сколько чисел называете (1-3)? "))
        except ValueError:
            print("Введите 1, 2 или 3.")
            continue
        if take not in (1, 2, 3):
            print("Можно назвать только 1, 2 или 3 числа.")
            continue
        for i in range(take):
            current += 1
            print(current, end=" ")
            if current >= 21:
                break
        print()
        if current >= 21:
            print(f"\nИгрок {player} произнёс 21 — он проиграл. Ура!!!")
            break
        player = 2 if player == 1 else 1

if name == "main":
    game_21()