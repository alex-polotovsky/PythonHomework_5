# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint


def number_check(MAX_NUM):
    """
    Функция number_check — это вспомогательная функция, которая проверяет,
    является ли ввод пользователя целым числом и находится ли он в пределах определенного диапазона.
    Она возвращает число, если оно допустимо, в противном случае печатает сообщение об ошибке.

    :param MAX_NUM: Limit the number of candies that can be taken
    :return: The number entered by the user
    """
    while True:
        try:
            number = int(input(f'Заберите не более {MAX_NUM} конфет: '))
        except ValueError:
            print('Bad value')
        else:
            if 0 < number <= MAX_NUM:
                return number
            print('Число вне диапазона')


def get_players(ch):
    """
    Функция принимает единственный аргумент ch, который является целым числом.
    Если ch == 1, то функция возвращает список двух игроков.
    Если ch == 2, то возвращается список  из игрока и just_bot.
    Если ch == 3, то возвращается список  из игрока и clever_bot.

    :param ch: Specifies the variant of the game
    :return: A list of two players' names
    """
    if ch == 1:
        return [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    elif ch == 2:
        return [input('Введите имя игрока: '), 'just_bot']
    elif ch == 3:
        return [input('Введите имя игрока: '), 'clever_bot']


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


def get_just_bot(remainder, MAX_NUM):
    """
    Функция принимает два аргумента:
            остаток - количество оставшихся конфет.
            MAX_NUM — максимальное количество конфет, которое можно взять за ход.

    :param remainder: Calculate the number of candies that will be left after the bot takes its share
    :param MAX_NUM: Limit the number of candies that can be taken
    :return: The number of candies that the bot takes
    :doc-author: Trelent
    """
    if remainder < MAX_NUM:
        number = randint(1, remainder)
    else:
        number = randint(1, MAX_NUM)
    print(f'Взял {number} конфет')
    return number


def get_clever_bot(reminder, MAX_NUM):
    """
    Функция принимает остаток конфет и возвращает остаток от деления
    оставшихся конфет на (MAX_NUM + 1).

    :param reminder: Determine the remainder of the reminder
    :param MAX_NUM: Limit the number of candies that can be taken
    :return: The reminder of the division between the input and (max_num + 1)
    """
    number = reminder % (MAX_NUM + 1)
    print(f'Взял {number} конфет')
    return number


def lets_game(loting_list, candies, MAX_NUM):
    """
    Функция принимает список игроков, общее количество конфет и количество конфет,
    которое можно взять за ход.
    Функция возвращает имя победителя.

    :param loting_list: Store the names of players
    :param candies: Store the number of candies
    :param MAX_NUM: Set the maximum number of candies that can be taken
    :return: :
    """
    print('Количество конфет: ', candies)
    index = 0
    while True:
        print(f'Ходит {loting_list[index]}')

        if loting_list[index] == 'just_bot':
            num = get_just_bot(candies, MAX_NUM)
        elif loting_list[index] == 'clever_bot':
            num = get_clever_bot(candies, MAX_NUM)
        else:
            while True:
                num = number_check(MAX_NUM)
                if num <= candies:
                    break
                print('Нельзя взять больше остатка.')

        candies -= num
        print('Остаток конфет: ', candies)

        if candies == 0:
            print(f'УРА!!! Победил {loting_list[index]}')
            break
        if index == len(loting_list) - 1:
            index -= 1
        else:
            index += 1


print('Игра с партнёром: 1\nИгра с компьютером: 2\nClever bot: 3')
choice = int(input('Ваш вабор: '))
candies = int(input('Общее количество конфет: '))
MAX_NUMBER = int(input('Максимальное количество конфет, которое можно забрать: '))

loting_plrs_list = get_loting(get_players(choice))
print(loting_plrs_list)
lets_game(loting_plrs_list, candies, MAX_NUMBER)
