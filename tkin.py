from tkinter import *
from tkinter import ttk
import random_let
import word
import os
import time


def finish():
    rootWindow.destroy()
    print("Закрытие окна")

rootWindow = Tk() # создаем новый обьект - окно
rootWindow.title("SCRABBLE for everyone!!!") # устанавливаем заголовок окна
rootWindow.iconbitmap(default="img/scrabble.ico")
rootWindow.geometry("700x800+400+0") # устанавливаем размеры окна
# rootWindow.attributes("-alpha", 0.2) # установка прозрачности
# rootWindow.attributes("-toolwindow", True) # отключение верхней панели окна

# rootWindow.resizable(False, False) # Неизменяемые размеры окна
gameName = Label(text="SCRABBLE") # создаем текстовую метку
gameName.pack() # размещаем метку в окне
# rootWindow.protocol("WM_DELETE_WINDOW", finish) # хрень какая то перехватываем закрытие окна 

#получаем набор 7 букв добавляем его на поле
l = random_let.letters_add()
us_let = ttk.Label(text=l)
us_let.pack()
# рамка с вводом слова кнопкой сейва и листом со словами
frame = ttk.Frame(borderwidth=1, relief=SOLID, height=100, width=700) # Создаем новое окно в корневом окне
frame['padding'] = (100, 10)

# выводим слово которое пользователь придумал
user_word_label = ttk.Label(frame, justify=LEFT, text="Your word ")
user_word_label.grid(column=0, row=0, sticky=W)  

# список слов польззователя
user_words_list = ttk.Label(frame, text=f"List of your words: ")
user_words_list.grid(column=2, row=0)
entered_text = ttk.Entry(frame)
entered_text.grid(column=1, row=0, sticky=W, padx=25, pady=5)

# выбираем ряд в который устанавливаем слово
row_label = ttk.Label(frame, text="Enter row number") 
row_label.grid(column=0, row=1, sticky=W)
row_entry = ttk.Entry(frame, width=3)
row_entry.grid(column=1, row=1, sticky=W, padx=25, pady=5)

# выбираем колонку с которой слово начинается
column_label = ttk.Label(frame, text="Enter column number")
column_label.grid(column=0, row=2, sticky=W)
column_entry = ttk.Entry(frame, width=3)
column_entry.grid(column=1, row=2, sticky=W, padx=25, pady=5)

# выбираем направление в котором устанавливаем слово
position = {"sticky":W} 
direct = ["Right", "Down"]
selected_direct = StringVar()
header = ttk.Label(frame, text="Choose direction")
header.grid(column=0, row=3, sticky=W)

def select():
    header.config(text=f"Your choice {selected_direct.get()}")

 # Радиокнопки 
direct_btn = ttk.Radiobutton(frame, text=direct[0], value=direct[0], variable=selected_direct, command=select)
direct_btn.grid(**position, column=1, row=3, padx=25)
direct_btn = ttk.Radiobutton(frame, text=direct[1], value=direct[1], variable=selected_direct, command=select)
direct_btn.grid(**position, column=1, row=4, padx=25, pady=5)

# устанавливаем рамку
frame.pack(anchor=N, padx=5, pady=5) 


user_all_words = [] # список всех слов
user_used_letters = []
user_word = ""
user_row = 0
user_column = 0
user_direct = ""
all_score = 0
listbox_words = Listbox() # листбокс куда помещаются все слова

# Создаем поле для игры 
game_field = Canvas(bg="#ccc", width=600, height=600, borderwidth=0)
game_field.pack(anchor=CENTER, expand=1)

# column_label = ttk.Label(game_field, text="1    2   3   4   5   6   7   8   9   ")
# column_label.grid(column=0, row=0)

# стили для бонусных полей
btn_style =ttk.Style()
btn_style.configure("SL.TButton", background="#FBFBDD")
btn_style.configure("TWS.TLabel", background="#B2DFDB")
btn_style.configure("TLS.TLabel", background="#B7F590")
btn_style.configure("DWS.TLabel", background="#F9A8C9")
btn_style.configure("DLS.TLabel", background="#E8AEF9")
btn_style.configure("POINT.TLabel", background="#A53EFB")

# создаем поле для игры с бонусными полями
ROW = 15
COLUMNS = 15
TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))  # поля с утраиванием слова 
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10)) # поля с удваиванием слова
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9)) # поля с утраиванием буквы
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11)) # поля с удваиванием буквы
buttons =[]
for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn = ttk.Button(game_field, width=5, padding=2, style="SL.TButton") #, style="SL.TLabel")
        temp.append(btn)
    buttons.append(temp)

for coord in TRIPLE_WORD_SCORE: # присваивание полям текста об удваивании или утраивании
    buttons[coord[0]][coord[1]]['text'] = "TWS"
    buttons[coord[0]][coord[1]]["style"] = "TWS.TLabel" 
for coord in DOUBLE_WORD_SCORE:
    buttons[coord[0]][coord[1]]['text'] = "DWS"
    buttons[coord[0]][coord[1]]["style"] = "DWS.TLabel" 
for coord in TRIPLE_LETTER_SCORE:
    buttons[coord[0]][coord[1]]['text'] = "TLS"
    buttons[coord[0]][coord[1]]["style"] = "TLS.TLabel" 
for coord in DOUBLE_LETTER_SCORE:
    buttons[coord[0]][coord[1]]['text'] = "DLS"
    buttons[coord[0]][coord[1]]["style"] = "DLS.TLabel" 
buttons[7][7]['text'] = '***'
buttons[7][7]['style'] = 'POINT.TLabel'


for i in range(ROW):
    for j in range(COLUMNS):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)

# функция для обработки внесенных данных 
def save_data(): 
    user_word = entered_text.get() # получаем введенный текст
    user_column = column_entry.get()
    user_row = row_entry.get()
    user_direct = selected_direct.get()
    user_location = random_let.row_column_check(user_column, user_row)
    global new_letters
    global user_all_words
    global all_score 
    global user_used_letters
    user_column_int = int(user_column)
    user_row_int = int(user_row)
    # проверка слова на соответствие букв и на присутствие в словаре
    user_letters = us_let.cget("text") # получаем буквы из списка в приожении
    if random_let.letters_control(user_word, user_letters, user_used_letters): #and random_let.word_location_control(user_all_words, user_column_int, user_row_int, user_direct, buttons, user_word): #and word.word_in_dict_control(user_word) 
        # random_let.word_place(user_word, user_direct, user_row_int, user_column_int, buttons)
        # print(user_all_words, user_column_int, user_row_int, user_direct, user_word)
        if len(user_all_words)==0:
            if  user_column_int == 8 and user_row_int == 8: # если в списке слов нет слов просто поомещаем слово в ту колонку и ряд который юзер ввел
                random_let.word_place(user_word, user_direct, user_row_int, user_column_int, buttons)
                print("Pass")
                user_all_words.append(user_word)
                score = random_let.pointsCount(user_word)
                l, used_letters = random_let.user_letters_update( user_word, user_letters)
                us_let['text'] = l
                u_l = list(used_letters)
                #user_letters = str(new_letters)
                print(l, " ", user_letters, " ", u_l)
                user_all_words_var = StringVar(value=user_all_words)
                user_all_words_listbox = Listbox(frame, listvariable=user_all_words_var)
                user_all_words_listbox.grid(column=2, row=1, rowspan=5, padx=6)

                all_score += score
                for i in u_l:
                    if i != " ":
                        user_used_letters.append(i)
                print(f"used letters list {user_used_letters}")
                print(f"your score {score}")
                print(f"all score {all_score}")
            else:
                print("wrong column or row number. Please begin from ***")
        else: # если в списке слов уже есть слова проверяем что буквы в пересекающемся слове совпадают
            # print(buttons[user_column_int-1][user_row_int-1]['text'])
            if random_let.word_and_field_control(direct, user_column_int, user_row_int, buttons, user_word):
                random_let.word_place(user_word, user_direct, user_row_int, user_column_int, buttons)
                print("second")
                user_all_words.append(user_word)
                score = random_let.pointsCount(user_word)
                l, used_letters = random_let.user_letters_update( user_word, user_letters)
                us_let['text'] = l
                u_l = list(used_letters)
                #user_letters = str(new_letters)
                print(l, " ", user_letters, " ", u_l)
                user_all_words_var = StringVar(value=user_all_words)
                user_all_words_listbox = Listbox(frame, listvariable=user_all_words_var)
                user_all_words_listbox.grid(column=2, row=1, rowspan=5, padx=6)

                all_score += score
                for i in u_l:
                    if i != " ":
                        user_used_letters.append(i)
                print(f"used letters list {user_used_letters}")
                print(f"your score {score}")
                print(f"all score {all_score}")
    else:
        print("Dont pass. Please enter your word")

btn_save = ttk.Button(frame, text="Save", command=save_data, padding=[20, 5]) # кнопка сохранить слово
btn_save.grid(column=0, row=5, columnspan=2, padx=25, pady=5)


# print(f"letters {l}")

footer = ttk.Frame(borderwidth=1, relief=SOLID, height=100, width=700)
footer['padding'] = (50, 1)

# minutes = StringVar()
# seconds = StringVar()
minutes = '00'
seconds ='00'
def countdown():
    t = 10
    global minutes
    global seconds
    while t > -1:
        mins, secs = divmod(t, 60)
        seconds.set(secs)
        minutes.set(mins)
        # minutes = '{:02d}'.format(mins)
        # seconds = '{:02d}'.format(secs)

        # print(timer, end="\r")
        rootWindow.update()
        time.sleep(1)
        if t == 0:
            seconds.set("00")
            minutes.set("00")
        t -= 1
      
    print('Fire in the hole!!')

timer = ttk.Label(footer, text=f'Time: {minutes}:{seconds} ', background="#856ff8")
timer['padding'] = (10, 0, 130, 0)
timer.grid(column=0, row=0, sticky=E) 
timer_btn =ttk.Button(footer, text="Start timer", command=countdown)
timer_btn.grid(column=1, row=0)
view_score = ttk.Label(footer, text=f"Your score: {all_score}")
view_score['padding'] = (10, 0, 130, 0)
view_score.grid(column=2, row=0)

def restart_program():
    rootWindow.destroy()
    os.startfile("tkin.py")

btn_new_game = ttk.Button(footer, command=restart_program) #command=restart_program) # Создаем кнопку новой игры
btn_new_game.grid(column=3, row=0, sticky=W,ipadx=10, ipady=15) # Параметры ipadx и ipady позволяют указать отступы содержимого виджета от границ виджета
btn_new_game["text"] ="New Game" # устанавливаем параметр text на кнопку новая игра
btn_new_game['padding'] = (10, 0, 10, 0)


footer.pack(anchor=S, padx=5, pady=5) # выводим рамку на экран
rootWindow.mainloop()
