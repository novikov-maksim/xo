def draw_field(f):
    print()
    print("    | 0 | 1 | 2 | ")
    print("  ---------------")
    for i, row in enumerate(f):
        print(f"  {i} | {' | '.join(row)} |")
        print("  ---------------")
    print()


def player_input(f, p):
    while True:
        place = input(f"Ходит игрок {p}. Введите две координаты через пробел: ").split()
        if len(place) != 2 or len(place[0]) != 1 or len(place[1]) != 1:
            print('Неверный ввод. Нужно ввести две координаты через пробел')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Вы вводите что-то не похожее на цифры :)), попробуйте еще раз ! ')
            continue
        x, y = map(int, place)
        if not(0 <= x <= 2 and 0 <= y <= 2):
            print('Координаты должны быть в диапазоне от 0 до 2 ')
            continue
        if f[x][y] != ' ':
            print('Эта клетка на поле уже занята')
            continue
        break
    return x, y


def check_win(f):
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)))
    for card in win:
        symbols = []
        for c in card:
            symbols.append(f[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            return True
        if symbols == ["0", "0", "0"]:
            return True
    return False


field = [[" "] * 3 for i in range(3)]
count = 0
print('Игра крестики нолики ver 1.0')
while True:
    draw_field(field)
    print('Первая координата по строке, вторая по столбцу - пример: 1 2')
    if count % 2 == 0:
        player = 'X'
    else:
        player = '0'
    if count < 9:
        x, y = player_input(field, player)
        field[x][y] = player
    elif count == 9:
        draw_field(field)
        print('Вы сыграли вничью !')
        break
    if check_win(field):
        draw_field(field)
        print(f"Выиграл игрок {player} поздравляем !")
        break
    count += 1
print('Игра закончилась')
