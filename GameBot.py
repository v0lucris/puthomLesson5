# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint as ri

total_sweet = 2021
take_sweet = 0
player_sweet = 0
bot_sweet = 0
second_player_sweet = 0
choose = None
def choose_game():
    choose = int (input("Put 1 if you want play with person, put 2 if you want play with bot: "))
    if choose == 1:
        star_game_person()
    else:
        star_game_bot()

def star_game_person():
    print("На столе лежит 2021 конфета.\nИграют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой")
    who_is_first_person()        

def star_game_bot():
    print("На столе лежит 2021 конфета.\nИграют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой")
    who_is_first_bot()

def who_is_first_person():
    random_number = ri(1, 2)
    if random_number == 1:
        player_turn()
    else:
        second_player_turn()

def who_is_first_bot():
    random_number = ri(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()


def player_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    global choose
    print(f"You move, This are {total_sweet} sweets")
    take_sweet = int(input("How much sweets are first person want take?: "))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
        take_sweet = int(input("This are a lot of sweets, try again: "))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        if choose == 2:
            bot_turn()
        else:
            second_player_turn()
    else:
        print("You are win")

def second_player_turn():
    global total_sweet
    global take_sweet
    global second_player_sweet
    print(f"You move, This are {total_sweet} sweets")
    take_sweet = int(input("How much sweets are second pesron want take?: "))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
        take_sweet = int(input("This are a lot of sweets, try again: "))
    total_sweet -= take_sweet
    second_player_sweet += take_sweet
    if total_sweet > 0:
        player_turn()
    else:
        print("You are win")        

def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1,28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f"bot take {take_sweet} sweets.There are {total_sweet} sweets on the table ")
    if total_sweet > 0:
        player_turn()
    else:
        print("You are win")
    