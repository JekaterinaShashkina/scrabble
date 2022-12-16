from tkinter import *
from tkinter import ttk
import random_let


def finish():
    rootWindow.destroy()
    print("Закрытие окна")

rootWindow = Tk() # создаем новый обьект - окно
rootWindow.title("SCRABBLE for everyone!!!") # устанавливаем заголовок окна
rootWindow.iconbitmap(default="img/scrabble.ico")
rootWindow.geometry("700x700+600+200") # устанавливаем размеры окна
# rootWindow.attributes("-alpha", 0.2) # установка прозрачности
# rootWindow.attributes("-toolwindow", True) # отключение верхней панели окна

rootWindow.resizable(False, False) # Неизменяемые размеры окна
gameName = Label(text="SCRABBLE") # создаем текстовую метку
gameName.pack() # размещаем метку в окне
rootWindow.protocol("WM_DELETE_WINDOW", finish) # хрень какая то перехватываем закрытие окна 

btn_new_game = ttk.Button() # Создаем кнопку новой игры
btn_new_game.pack( side=BOTTOM, pady=20, ipadx=10, ipady=15) # Параметры ipadx и ipady позволяют указать отступы содержимого виджета от границ виджета
btn_new_game["text"] ="New Game" # устанавливаем параметр text на кнопку новая игра

#получаем набор 7 букв добавляем его на поле
user_letters = random_let.letters_add()
us_let = ttk.Label(text=user_letters)
us_let.pack()
entered_text = ttk.Entry()
entered_text.pack(anchor=S, padx=6, pady=6)

user_word = entered_text.get() # получаем введенный текст

def show_message(): # выводим текст на экран если соответствует условиям (не работает)
    print(user_word)
    u_w = Label(rootWindow, text=user_word)
    if random_let.letters_control(user_word) and random_let.word_in_dict_control(user_word) == True:
        u_w.pack()

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8,10]) # Создаем новое окно в корневом окне
user_word_label = ttk.Label(frame, text=f"Your word {user_word}")  # выводим слово которое пользователь придумал
user_word_label.pack(anchor=NW)

row_label = ttk.Label(frame, text="Enter row number") # выбираем ряд в который устанавливаем слово
row_label.pack()
row_entry = ttk.Entry(frame, width=3)
row_entry.pack(anchor=NW)
 
column_label = ttk.Label(frame, text="Enter column number") # выбираем колонку с которой слово начинается
column_label.pack()
column_entry = ttk.Entry(frame, width=3)
column_entry.pack(anchor=NW)

position = {"padx":6, "pady":6, "anchor":NW} # выбираем направление в котором устанавливаем слово
direct = ["Right", "Down"]
selected_direct = StringVar()
header = ttk.Label(frame, text="Choose direction")
header.pack(**position)

def select():
    header.config(text=f"Your choice {selected_direct.get()}")

for d in direct:
    direct_btn = ttk.Radiobutton(frame, text=d, value=d, variable=selected_direct, command=select)
    direct_btn.pack(**position)

btn_send = ttk.Button(frame, text="Send") # кнопка для отсылки инфо о выборе
btn_send.pack(anchor=S, padx=6, pady=6)

frame.pack(anchor=NW, padx=5, pady=5) # выводим рамку на экран


btn_save = ttk.Button(text="Save", command=show_message) # кнопка сохранить слово
btn_save.pack(anchor=S, padx=6, pady=6) 

# Создаем поле для игры 
game_field = Canvas(bg="#ccc", width=600, height=600, borderwidth=0)
game_field.pack(anchor=CENTER, expand=1)

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



rootWindow.mainloop()