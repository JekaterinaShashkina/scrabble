import random
import bags
from tkinter import *
from tkinter import ttk

def bag_choice(lang):
    if lang == "Estonian":
        bag = bags.est_bag
    elif lang == "Russian":
        bag = bags.ru_bag
    else:
        bag = bags.en_bag
    return bag

user_letters = []
en_vowels = "euioa"
ru_vowels = "уеаоыэюя"
est_vowels = "euioaüõäö"
# выдаем буквы пользователю
def letters_add(lang):
    if lang == "Estonian":
        vowels = est_vowels
    elif lang == "Russian":
        vowels = ru_vowels
    else:
        vowels = en_vowels
    bag = bag_choice(lang)
    while len(user_letters) < 7:
        l = random.choice(bag.tiles)
        user_letters.append(l)
        bag.remove_from_bag(l)
    count = 0 
    for i in user_letters:
        if i in vowels:
            count += 1
    if count == 0:
        user_letters.pop()
        bag.return_to_bag(i)
        r_choice = random.choice(vowels)
        user_letters.append(r_choice)
        bag.remove_from_bag(r_choice)
    let = ' '.join(user_letters)
    
    return let

# добавляем буквы после использования для слова
def user_letters_update(word, letters, lang):
    bag = bag_choice(lang)
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
        l = random.choice(bag.tiles)
        l_letters.append(l)
        bag.remove_from_bag(l)
    let = ' '.join(l_letters)
    used_letters = " ".join(used_l)
    # print(used_letters)
    return let, used_letters

# проверка введенного слова, соответствует ли слово буквам имеющимся у пользователя
def letters_control(word, letters, user_let):
    count = 0
    for i in word:
        if i in letters or i in user_let:
            count += 1
    if count == len(word):
        print('Отлично')
        return True
    else:
        print('неправильные буквы')
        return False

# размещение слова на поле и сохранение бонусов в отодельный массив
premium_spots = []
def word_place(word, direct, row, column, buttons):
    boldStyle = ttk.Style ()
    boldStyle.configure ("Bold.TButton", width=2, font='Helvetica 10 bold')
    global premium_spots
    if direct == "Down":

        for i in word:
            if buttons[row][column]['text'] != " ":
                premium_spots.append((i, buttons[row][column]['text']))
            buttons[row][column]['text'] = i.upper()
            buttons[row][column]['style'] = "Bold.TButton"
            row += 1
    if direct == "Right":
            for i in word:
                if buttons[row][column]['text'] != " ":
                    premium_spots.append((i, buttons[row][column]['text']))
                buttons[row][column]['text'] = i.upper()
                buttons[row][column]['style'] = "Bold.TButton"

                column += 1

def fun(x):
    dct = {
    'aeioulnstrавеинорст' : 1, 'dgдклмпуõ' : 2, 'bcmpбгёьяäöü' : 3,
    'fhvwyйыšž' : 4, 'kжзхцч' : 5, 'jxшэю' : 8, 'qzщъф' :10
    }
    for key in dct:
        if x in key:
            return dct.get(key) # метод get ищет значение по ключу, если находит ключ возвращает значение

# Суммируем очки за слово 
def pointsCount(word):
    global premium_spots
    word_score = 0
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
            
def row_column_check(column, row):
    location = []
    if (column == "" or row == "") or (column not in [str(x) for x in range(16)]) or (row not in [str(x) for x in range(16)]):
        return False
    else:
        location = [int(row), int(column)]
    return True, location

# создание массива букв и еслть что то на том месте
def control_buttons(direct, column, row, buttons, word):
    space_letters_list = list()
    for _ in word:
        if buttons[row][column]['text'] == " " or buttons[row][column]['text'] == "" or buttons[row][column]['text'] == "TWS" or buttons[row][column]['text'] == "TLS" or buttons[row][column]['text'] == "DWS" or buttons[row][column]['text'] == "DLS" or buttons[row][column]['text'] == "...":
            space_letters_list.append("-")
        else:
            space_letters_list.append(buttons[row][column]['text'])
        if direct == "Right":
            column += 1
        elif direct == "Down":
            row += 1
    
    return space_letters_list
# контроль соответствия букв и массива поля
def word_and_field_control(direct, column, row, buttons, word, message):
    spl = control_buttons(direct, column, row, buttons, word)
    word_l = list(word)
    for i in range(len(spl)):
        if spl[i] != "-":
            if word_l[i].upper() == spl[i]:
                return True
            else:
                print("you need other word place")
                message["text"] = "You need other word place"
                return False



