# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint


def get_players_1():
    """
    Функция запрашивает у пользователя два имени и возвращает список, содержащий эти имена.

    :return: A list with two elements:
    """
    players = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    return players


def get_loting(players):
    """
    Функция случайным образом выбирает очерёдность хода игроков. Она принимает список игроков
    в качестве аргумента и возвращает список игроков в порядке очерёдности.

    :param players: Store the names of the players
    :return: A list of players
    """
    print('Жеребьёвка!')
    index = randint(0, 1)
    if index == 1:
        players.reverse()
    return players


def manual_game(players):
    """
    Функция позволяет пользователям играть с компьютером в игру «деление конфет».
    Функция принимает список игроков и спрашивает каждого игрока по очереди,
    сколько конфет он хотел бы взять. Проверяет остаток и объявляет победителя, если конфет нет.

    :param players: Store the names of all players
    :return: None
    """
    loting_list = get_loting(players)
    candies = 2021
    index = 0
    while (True):
        print(f'Ходит {loting_list[index]}')
        num = int(input('Заберите не более 28 конфет: '))
        candies -= num
        if candies == 0:
            print(f'Победил {loting_list[index]}')
            break
        if index == len(loting_list) - 1:
            index -= 1
        else:
            index += 1


print('Игра с партнёром: 1\nИгра с компьютером: 2\nClever bot: 3')
choice = int(input('Ваш вабор: '))

if choice == 1:
    plrs_list = get_players_1()
    manual_game(plrs_list)
elif choice == 2:
    pass
elif choice == 3:
    pass
