from tkinter import *
from tkinter import ttk
import random_let
import word


def finish():
    rootWindow.destroy()
    print("Закрытие окна")

rootWindow = Tk() # создаем новый обьект - окно
rootWindow.title("SCRABBLE for everyone!!!") # устанавливаем заголовок окна
rootWindow.iconbitmap(default="img/scrabble.ico")
rootWindow.geometry("700x800+400+0") # устанавливаем размеры окна
# rootWindow.attributes("-alpha", 0.2) # установка прозрачности
# rootWindow.attributes("-toolwindow", True) # отключение верхней панели окна

rootWindow.resizable(False, False) # Неизменяемые размеры окна
gameName = Label(text="SCRABBLE") # создаем текстовую метку
gameName.pack() # размещаем метку в окне
rootWindow.protocol("WM_DELETE_WINDOW", finish) # хрень какая то перехватываем закрытие окна 

#получаем набор 7 букв добавляем его на поле
user_letters = random_let.letters_add()
us_let = ttk.Label(text=user_letters)
us_let.pack()


frame = ttk.Frame(borderwidth=1, relief=SOLID, height=100, width=700) # Создаем новое окно в корневом окне
frame['padding'] = (100, 10)

user_word_label = ttk.Label(frame, justify=LEFT, text="Your word ")
user_word_label.grid(column=0, row=0, sticky=W)  # выводим слово которое пользователь придумал
# user_word_label.pack()
user_words_list = ttk.Label(frame, text="List of your words: ")
user_words_list.grid(column=2, row=0)
entered_text = ttk.Entry(frame)
entered_text.grid(column=1, row=0, sticky=W, padx=25, pady=5)
# entered_text.pack(anchor=S, padx=6, pady=6)

row_label = ttk.Label(frame, text="Enter row number") # выбираем ряд в который устанавливаем слово
row_label.grid(column=0, row=1, sticky=W)
row_entry = ttk.Entry(frame, width=3)
row_entry.grid(column=1, row=1, sticky=W, padx=25, pady=5)
 
column_label = ttk.Label(frame, text="Enter column number") # выбираем колонку с которой слово начинается
column_label.grid(column=0, row=2, sticky=W)
column_entry = ttk.Entry(frame, width=3)
column_entry.grid(column=1, row=2, sticky=W, padx=25, pady=5)

position = {"sticky":W} # выбираем направление в котором устанавливаем слово
direct = ["Right", "Down"]
selected_direct = StringVar()
header = ttk.Label(frame, text="Choose direction")
header.grid(column=0, row=3, sticky=W)

def select():
    header.config(text=f"Your choice {selected_direct.get()}")


direct_btn = ttk.Radiobutton(frame, text=direct[0], value=direct[0], variable=selected_direct, command=select)
direct_btn.grid(**position, column=1, row=3, padx=25)
direct_btn = ttk.Radiobutton(frame, text=direct[1], value=direct[1], variable=selected_direct, command=select)
direct_btn.grid(**position, column=1, row=4, padx=25, pady=5)

frame.pack(anchor=N, padx=5, pady=5) # выводим рамку на экран


user_all_words = []
user_word = ""
user_row = 0
user_column = 0
user_direct = ""

# Создаем поле для игры 
game_field = Canvas(bg="#ccc", width=600, height=600, borderwidth=0)
game_field.pack(anchor=CENTER, expand=1)

# column_label = ttk.Label(game_field, text="1    2   3   4   5   6   7   8   9   ")
# column_label.grid(column=0, row=0)

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
        btn = ttk.Button(game_field, width=5, padding=2)
        temp.append(btn)
    buttons.append(temp)

for coord in TRIPLE_WORD_SCORE: # присваивание полям текста об удваивании или утраивании
    buttons[coord[0]][coord[1]]['text'] = "TWS"
for coord in DOUBLE_WORD_SCORE:
    buttons[coord[0]][coord[1]]['text'] = "DWS"
for coord in TRIPLE_LETTER_SCORE:
    buttons[coord[0]][coord[1]]['text'] = "TLS"
for coord in DOUBLE_LETTER_SCORE:
    buttons[coord[0]][coord[1]]['text'] = "DLS"
buttons[7][7]['text'] = '***'

for i in range(ROW):
    for j in range(COLUMNS):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)

def save_data(): # выводим текст на экран если соответствует условиям (не работает)
    user_word = entered_text.get() # получаем введенный текст
    user_column = column_entry.get()
    user_column = int(user_column)
    user_row = row_entry.get()
    user_row = int(user_row)
    user_direct = selected_direct.get()
    user_location = random_let.row_column_check(user_column, user_row)
    # print(user_all_words[0][0])
    #print(user_all_words)
    if random_let.letters_control(user_word) and word.word_in_dict_control(user_word):
        print("Pass")
        global user_all_words
        user_all_words.append(user_word)
    else:
        print("Dont pass. Please enter your word")

    print(user_word, user_location, user_direct)
    print(user_all_words)
    random_let.word_place(user_word, user_direct, user_column, user_row, buttons)


btn_save = ttk.Button(frame, text="Save", command=save_data, padding=[20, 5]) # кнопка сохранить слово
btn_save.grid(column=0, row=5, columnspan=2, padx=25, pady=5)

footer = ttk.Frame(borderwidth=1, relief=SOLID, height=100, width=700)
footer['padding'] = (50, 1)

timer = ttk.Label(footer, text='Time: ')
timer['padding'] = (10, 0, 130, 0)
timer.grid(column=0, row=0, sticky=E) 
score = ttk.Label(footer, text="Your score: ")
score['padding'] = (10, 0, 130, 0)
score.grid(column=1, row=0)

btn_new_game = ttk.Button(footer) # Создаем кнопку новой игры
btn_new_game.grid(column=2, row=0, sticky=W,ipadx=10, ipady=15) # Параметры ipadx и ipady позволяют указать отступы содержимого виджета от границ виджета
btn_new_game["text"] ="New Game" # устанавливаем параметр text на кнопку новая игра
btn_new_game['padding'] = (10, 0, 10, 0)

footer.pack(anchor=S, padx=5, pady=5) # выводим рамку на экран
rootWindow.mainloop()