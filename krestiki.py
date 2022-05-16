field = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_field(f):
    print("-------------")
    for i in range(3):
        print("|", f[0 + i * 3], "|", f[1 + i * 3], "|", f[2 + i * 3], "|")
        print("-------------")


def player_input(f, player_choice):
    correct_input = False
    while not correct_input:
        try:
            player_answer = int(input(f'Выберите куда поставить {player_choice} ? '))
        except ValueError:
            print("Вы вводите что-то не то :)), попробуйте еще раз ! ?")
            continue
        if 1 <= player_answer <= 9:
            if str(f[player_answer - 1]) not in "ox":
                f[player_answer - 1] = player_choice
                correct_input = True
            else:
                print("Эта клетка на поле уже занята")
        else:
            print(player_answer)
            print("Нужно ввести цифру от 1 до 9 чтобы походить")


def check_win(f):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if f[each[0]] == f[each[1]] == f[each[2]]:
            return f[each[0]]
    return False


count = 0
win = False
print('Игра крестики нолики ver 1.0')
while not win:
    draw_field(field)
    if count % 2 == 0:
        player_input(field, "x")
    else:
        player_input(field, "o")
    count += 1
    if count > 4:
        winner = check_win(field)
        if winner:
            print(winner, "выиграл!")
            break
    if count == 9:
        print("Ничья!")
        break
draw_field(field)
