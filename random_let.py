import random
import string
import word
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
print(*user_letters)
if len(user_letters) < 7:
    letters_add()
# word = input(f"Введите слово из букв {let} ")
# print(word)
def letters_control(word):
    count = 0
    for i in word:
        if i in user_letters:
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
    points = sum(map(fun, word))
    return points

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
    if word.word_in_dict_control(word) == True:
        points = pointsCount(word)
        print(f'Grats your word is {points} points')
    else:
        print(f"Sorry, you word is not found")


def row_column_check(column, row):
    location = []
    if (column == "" or row == "") or (column not in [str(x) for x in range(15)]) or (row not in [str(x) for x in range(15)]):
        location = [-1,-1]
    else:
        location = [int(row), int(column)]
    return location