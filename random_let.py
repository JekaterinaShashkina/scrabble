import random
from functools import reduce
from operator import add
# import string
# import word
bag = [] # создаем массив сумка букв
def add_to_bag(tile, quantity): # добавляем буквы и количество букв в сумку 
    for _ in range(quantity):
        bag.append(tile)

add_to_bag('a', 9)
add_to_bag('b', 2)
add_to_bag('c', 2)
add_to_bag('d', 4)
add_to_bag('e', 12)
add_to_bag('f', 2)
add_to_bag('j', 3)
add_to_bag('h', 2)
add_to_bag('i', 9)
add_to_bag('j', 9)
add_to_bag('k', 1)
add_to_bag('l', 4)
add_to_bag('m', 2)
add_to_bag('n', 6)
add_to_bag('o', 8)
add_to_bag('p', 2)
add_to_bag('q', 1)
add_to_bag('r', 6)
add_to_bag('s', 4)
add_to_bag('t', 6)
add_to_bag('u', 4)
add_to_bag('v', 2)
add_to_bag('w', 2)
add_to_bag('x', 1)
add_to_bag('y', 2)
add_to_bag('z', 1)
#add_to_bag('#', 2)
random.shuffle(bag) # перемешиваем буквы

def return_to_bag(tile):
    bag.append(tile)

def remove_from_bag(tile):
    bag.pop(tile)
# alpha = string.ascii_lowercase
user_letters = []
vowels = "euioa"

def letters_add():
    while len(user_letters) < 7:
        l = random.choice(bag)
        user_letters.append(l)
        bag.remove(l)
    count = 0 
    for i in user_letters:
        if i in vowels:
            count += 1
    if count == 0:
        user_letters.pop()
        return_to_bag(i)
        r_choice = random.choice(vowels)
        user_letters.append(r_choice)
        remove_from_bag(r_choice)
    let = ' '.join(user_letters)
    
    return let

def user_letters_update(word, letters):
    l_letters = list(letters)
    used_l = list()
    for i in l_letters:
        if i == " ":
            l_letters.remove(i)
    for i in word:
        if i in letters:
            l_letters.remove(i)
            used_l.append(i)
    while len(l_letters) < 7:
        l = random.choice(bag)
        l_letters.append(l)
        bag.remove(l)
    let = ' '.join(l_letters)
    used_letters = " ".join(used_l)
    # print(used_letters)
    return let, used_letters

def letters_control(word, letters, user_let):
    count = 0
    for i in word:
        if i in letters or i in user_let:
            count += 1
    if count == len(word):
        print('Отлично')
        return True
    else:
        print('не так')
        return False

# en_dict = '/dictionaries/english_noun.txt'
# ee_dict = '/dictionaries/estonian_nouns.txt'
# ru_dict = '/dictionaries/russian_nouns.txt'
premium_spots = []
def word_place(word, direct, row, column, buttons):
    global premium_spots
    if direct == "Down":

        for i in word:
            if buttons[row-1][column-1]['text'] != " ":
                premium_spots.append((i, buttons[row-1][column-1]['text']))
            buttons[row-1][column-1]['text'] = i.upper()
            row += 1
            # print(i)
    if direct == "Right":
            for i in word:
                if buttons[row-1][column-1]['text'] != " ":
                    premium_spots.append((i, buttons[row-1][column-1]['text']))
                buttons[row-1][column-1]['text'] = i.upper()
                column += 1
                # print(i)

def fun(x):
    dct = {
    'aeioulnstr' : 1, 'dg' : 2, 'bcmp' : 3,
    'fhvwy' : 4, 'k' : 5, 'jx' : 8, 'qz' :10
    }
    for key in dct:
        if x in key:
            return dct.get(key) # метод get ищет значение по ключу, если находит ключ возвращает значение
# Суммируем очки за слово 
def pointsCount(word):
    global premium_spots
    # points = list(map(fun, word))
    # print(points)
    # return points
    word_score = 0
    # p = 0
    for letter in word:
        for spot in premium_spots:
            if letter == spot[0]:
                if spot[1] == "TLS":
                    word_score += fun(letter) * 2
                elif spot[1] == 'DLS':
                    word_score += fun(letter)
        word_score += fun(letter)
    for spot in premium_spots:
        if spot[1] == "TWS":
            word_score *= 3
        elif spot[1] == "DWS":
            word_score *= 2

    return word_score
# print(pointsCount("hi"))
# # Проверка в словаре 
# def word_in_dict_control(word):
#     with open('./dictionaries/english_noun.txt', 'r') as en_dict: # открываем файл на чтение
#         words = en_dict.readlines()    # читаем файл построчно и делаем массив строк
#     # w = 0
#     for line in words:
#         if line.strip('\n') == word: # проверяем есть ли слово в словаре, удаляем из слов в словаре перенос строки
#             print(f'Grats')
#             return True
#         else:
#             print(f"Sorry")
#             return False
            
# начисление пунктов за слово
def word_points(word):
    # if word.word_in_dict_control(word) == True:
    points = pointsCount(word)
    print(f'Grats your word is {points} points')
    # else:
    #     print(f"Sorry, you word is not found")


def row_column_check(column, row):
    location = []
    if (column == "" or row == "") or (column not in [str(x) for x in range(15)]) or (row not in [str(x) for x in range(15)]):
        return "Location is not valid"
    else:
        location = [int(row), int(column)]
    return location



def control_buttons(direct, column, row, buttons, word):
    space_letters_list = list()
    for i in word:
        if buttons[row - 1][column - 1]['text'] == " " or buttons[column - 1][row - 1]['text'] == "TWS" or buttons[column - 1][row - 1]['text'] == "TLS" or buttons[column - 1][row - 1]['text'] == "DWS" or buttons[column - 1][row - 1]['text'] == "DLS" or buttons[column - 1][row - 1]['text'] == "...":
            print(buttons[row-1][column-1])
            space_letters_list.append(" ")
        else:
            space_letters_list.append(buttons[row - 1][column - 1]['text'])
        if direct == "Down":
            column += 1
        else:
            row += 1
    
    print("spl: ", space_letters_list)
    return space_letters_list

def word_and_field_control(direct, column, row, buttons, word):
    spl = control_buttons(direct, column, row, buttons, word)
    word_l = list(word)
    for i in range(len(spl)):
        if spl[i] != " ":
            if word_l[i].upper() == spl[i]:
                return True
            else:
                print("you need other word place")
                return False


# word_and_field_control('hello', ['h', ' ', ' ', 'l', 'o'])

def word_location_control(user_all_words, column, row, direct, buttons, word):
    if len(user_all_words) == 0:
        if column == 8 and row == 8:
            return True
        else:
            print("Please begin from ***")
            return False
    else:
        word_and_field_control(direct, column, row, buttons, word)

