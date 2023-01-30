from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random_let
import word
import time
# import main


def finish():
    rootWindow.destroy()
    print("Закрытие окна")

rootWindow = Tk() # создаем новый обьект - окно
ttk.Style().configure(".",  font="helvetica 9", foreground="#004D40")  
rootWindow.title("SCRABBLE for everyone!!!") # устанавливаем заголовок окна
rootWindow.iconbitmap(default="img/scrabble.ico")
rootWindow.geometry("850x800+400+0") # устанавливаем размеры окна
# rootWindow.attributes("-alpha", 0.2) # установка прозрачности
# rootWindow.attributes("-toolwindow", True) # отключение верхней панели окна

# rootWindow.resizable(False, False) # Неизменяемые размеры окна
gameName = Label(text="SCRABBLE", font="Helvetica 16 italic", foreground="#A53EFB") # создаем текстовую метку
gameName.pack() # размещаем метку в окне
# rootWindow.protocol("WM_DELETE_WINDOW", finish) # хрень какая то перехватываем закрытие окна 

us_let = ttk.Label()
us_let["text"] = ""
us_let.pack()
# рамка с вводом слова кнопкой сейва и листом со словами
frame = ttk.Frame(borderwidth=1, relief=SOLID, height=100, width=700) # Создаем новое окно в корневом окне
frame['padding'] = (80, 10)

# выводим слово которое пользователь придумал
user_word_label = ttk.Label(frame, justify=LEFT, text="Your word ")
user_word_label.grid(column=0, row=0, sticky=W)  

def is_valid(newval):
    if newval == "" or newval not in [str(x) for x in range(15)]:
        return False
    else:
        return True
check = (frame.register(is_valid), "%P")
# список слов польззователя
user_words_list = ttk.Label(frame, text=f"List of your words: ")
user_words_list.grid(column=2, row=0)
entered_text = ttk.Entry(frame)
entered_text.grid(column=1, row=0, sticky=W, padx=25)

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
# радиокнопки, выбор направления
direct = ["Right", "Down"]
selected_direct = StringVar()
direction = ttk.Label(frame, text="Choose direction")
direction.grid(column=0, row=3, sticky=W)

def select():
    direction.config(text=f"Your choice {selected_direct.get()}")

 # Радиокнопки 
direct_btn = ttk.Radiobutton(frame, text=direct[0], value=direct[0], variable=selected_direct, command=select)
direct_btn.grid(**position, column=1, row=3, padx=25)
direct_btn = ttk.Radiobutton(frame, text=direct[1], value=direct[1], variable=selected_direct, command=select)
direct_btn.grid(**position, column=1, row=4, padx=25, pady=5)

# выбор языка
lang = ["English", "Estonian", "Russian"]
selected_language = StringVar()
language = ttk.Label(frame, text="")
language.grid(column=3, row=0)
# url_en = 
img_en =PhotoImage(file="img/icon-en.png")
eng_btn = ttk.Button(frame, image=img_en, padding=0, text="English", cursor='man')
eng_btn.config(command=lambda button=eng_btn: lang_choice(button))
eng_btn.grid(column=3, row=1, ipady=1, ipadx=1, sticky=E)
# url_est = 
img_est =PhotoImage(file="img/icon-est.png")
est_btn = ttk.Button(frame, image=img_est, padding=0, text="Estonian")
est_btn.config(command=lambda button=est_btn: lang_choice(button))
est_btn.grid(column=3, row=2, ipady=1, ipadx=1, sticky=E)
# url_rus = 
img_rus =PhotoImage(file="img/icon-rus.png")
rus_btn = ttk.Button(frame, image=img_rus, padding=0, text="Russian")
rus_btn.config(command=lambda button=rus_btn: lang_choice(button))
rus_btn.grid(column=3, row=3, ipady=1, ipadx=1, sticky=E)

def lang_choice(clicked_button):
    selected_language = clicked_button["text"]
    l = random_let.letters_add(selected_language)
    us_let["text"] = l
    language.config(text=f"{selected_language}")
    print(selected_language)
    eng_btn['state']= 'disabled'
    est_btn['state']= 'disabled'
    rus_btn['state']= 'disabled'


# устанавливаем рамку
frame.pack(anchor=N, padx=5, pady=5) 

message = ttk.Label(font="helvetica 11", justify=CENTER, text="Welcome to our game. Here you can check your words knowledge")
message.pack()

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

# стили для бонусных полей
btn_style =ttk.Style()
btn_style.configure("SL.TButton", background="#FBFBDD")
btn_style.configure("TWS.TLabel", background="#B2DFDB")
btn_style.configure("TLS.TLabel", background="#B7F590")
btn_style.configure("DWS.TLabel", background="#F9A8C9")
btn_style.configure("DLS.TLabel", background="#E8AEF9")
btn_style.configure("POINT.TLabel", background="#A53EFB")

# создаем поле для игры с бонусными полями
ROW = 16
COLUMNS = 16
COLUMN_NAME = ((0,0), (0, 1), (0,2), (0,3), (0,4), (0,5),(0,6), (0,7), (0,8), (0,9), (0,10),(0,11),(0,12),(0,13),(0,14),(0,15))
ROW_NAME = ((0,0), (1, 0), (2,0), (3,0), (4,0), (5,0),(6,0), (7,0), (8,0), (9,0), (10,0),(11,0),(12,0),(13,0),(14,0),(15,0))
TRIPLE_WORD_SCORE = ((1,1), (8, 1), (15,1), (1, 8), (15, 8), (1, 15), (8, 15), (15,15))  # поля с утраиванием слова 
DOUBLE_WORD_SCORE = ((2,2), (3,3), (4,4), (5,5), (2, 14), (3, 13), (4, 12), (5, 11), (14, 2), (14, 3), (12, 4), (11, 5), (14,14), (13, 13), (12,12), (11,11)) # поля с удваиванием слова
TRIPLE_LETTER_SCORE = ((2,6), (2, 10), (6,2), (6,6), (6,10), (6,14), (10,2), (10,6), (10,10), (10,14), (14, 6), (14,10)) # поля с утраиванием буквы
DOUBLE_LETTER_SCORE = ((1, 4), (1,12), (3,7), (3,9), (4,1), (4,8), (4,15), (7,3), (7,7), (7,9), (7,13), (8,4), (8,12), (9,3), (9,7), (9,9), (9, 13), (12,1), (12,8), (12,15), (13,7), (13,9), (15, 4), (15, 12)) # поля с удваиванием буквы
buttons =[]
for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn = ttk.Button(game_field, width=5, padding=2, style="SL.TButton") #, style="SL.TLabel")
        temp.append(btn)
    buttons.append(temp)
for i in COLUMN_NAME:
    buttons[i[0]][i[1]]['text'] = i[1]
for i in ROW_NAME:
    buttons[i[0]][i[1]]['text'] = i[0]
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
buttons[8][8]['text'] = '***'
buttons[8][8]['style'] = 'POINT.TLabel'
buttons[0][0]['text'] = ''


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
    user_lang = language["text"]
    global new_letters
    global user_all_words
    global all_score 
    global user_used_letters
    global message
    
    user_column_int = 0 if user_column == "" else int(user_column)
    user_row_int = 0 if user_row == "" else int(user_row)

   # проверка слова на соответствие букв и на присутствие в словаре
    user_letters = us_let.cget("text") # получаем буквы из списка в приожении
    if user_word == "" :
        message["text"]="You forgot enter your word"
    elif user_location == False:
        message["text"]="Location is wrong"
    elif random_let.letters_control(user_word, user_letters, user_used_letters): #and word.word_in_dict_control(user_word, user_lang):
        # random_let.word_place(user_word, user_direct, user_row_int, user_column_int, buttons)
        # print(user_all_words, user_column_int, user_row_int, user_direct, user_word)
        if len(user_all_words)==0:
            if  user_column_int == 8 and user_row_int == 8: # если в списке слов нет слов, просто поомещаем слово в ту колонку и ряд который юзер ввел
                random_let.word_place(user_word, user_direct, user_row_int, user_column_int, buttons)
                user_all_words.append(user_word)
                score = random_let.pointsCount(user_word)
                l, used_letters = random_let.user_letters_update( user_word, user_letters, user_lang)
                us_let['text'] = l
                u_l = list(used_letters)
                user_all_words_var = StringVar(value=user_all_words)
                user_all_words_listbox = Listbox(frame, listvariable=user_all_words_var)
                user_all_words_listbox.grid(column=2, row=1, rowspan=5, padx=6)
                message["text"]=f"Good choice. Your word is {score} points"
                all_score += score
                for i in u_l:
                    if i != " ":
                        user_used_letters.append(i)
                print(f"used letters list {user_used_letters}")
                print(f"your score {score}")
                print(f"all score {all_score}")
                view_score["text"]=f"Your score: {all_score}"
            else:
                print("wrong column or row number. Please begin from ***")
                message["text"]="Wrong column or row number. Please begin from ***"

        else: # если в списке слов уже есть слова проверяем что буквы в пересекающемся слове совпадают
            # print(buttons[user_column_int-1][user_row_int-1]['text'])
            if random_let.word_and_field_control(user_direct, user_column_int, user_row_int, buttons, user_word, message):
                random_let.word_place(user_word, user_direct, user_row_int, user_column_int, buttons)
                user_all_words.append(user_word)
                score = random_let.pointsCount(user_word)
                l, used_letters = random_let.user_letters_update( user_word, user_letters, user_lang)
                us_let['text'] = l
                u_l = list(used_letters)
                user_all_words_var = StringVar(value=user_all_words)
                user_all_words_listbox = Listbox(frame, listvariable=user_all_words_var)
                user_all_words_listbox.grid(column=2, row=1, rowspan=5, padx=6)
                message["text"]=f"It's great!!! Your word is {score} points"
                all_score += score
                for i in u_l:
                    if i != " ":
                        user_used_letters.append(i)
                print(f"used letters list {user_used_letters}")
                print(f"your score {score}")
                print(f"all score {all_score}")

                view_score["text"]=f"Your score: {all_score}"

    else:
        print("Dont pass. Please enter your word")
        message["text"]="Dont pass. Please enter your word"

btn_save = ttk.Button(frame, text="Save", command=save_data, padding=[20, 5]) # кнопка сохранить слово
btn_save.grid(column=0, row=5, columnspan=2, padx=25, pady=5)


# print(f"letters {l}")

footer = ttk.Frame(borderwidth=1, relief=SOLID, height=100, width=700)
footer['padding'] = (50, 1)

minutes = StringVar()
seconds = StringVar()
minutes.set('01')
seconds.set ('00')
def countdown():
    t = 10
    global minutes
    global seconds
    while t > -1:
        mins, secs = divmod(t, 60)
        seconds.set('{:02d}'.format(secs))
        minutes.set('{:02d}'.format(mins))

        rootWindow.update()
        time.sleep(1)
        if t == 0:
            seconds.set("00")
            minutes.set("00")
            messagebox.showinfo("Time Countdown", f"Time is over. Your score: {all_score}")
        t -= 1
      
timer = ttk.Label(footer, text=f'Time:', background="#856ff8")
minuteEntry = Entry(footer, width=3, textvariable=minutes)
minuteEntry.grid(column=1, row=0, sticky=E)
secondEntry = Entry(footer, width=3, textvariable=seconds)
secondEntry.grid(column=2, row=0, sticky=E)
timer['padding'] = (10, 0, 130, 0)
timer.grid(column=0, row=0, sticky=E) 
timer_btn =ttk.Button(footer, text="Start timer", command=countdown)
timer_btn.grid(column=3, row=0)
view_score = ttk.Label(footer, text=f"Your score: {all_score}")
view_score['padding'] = (10, 0, 130, 0)
view_score.grid(column=4, row=0)

# def restart_program():
#     rootWindow.destroy()
#     os.startfile("tkin.py")

# btn_new_game = ttk.Button(footer, command=restart_program) #command=restart_program) # Создаем кнопку новой игры
# btn_new_game.grid(column=5, row=0, sticky=W,ipadx=10, ipady=15) # Параметры ipadx и ipady позволяют указать отступы содержимого виджета от границ виджета
# btn_new_game["text"] ="New Game" # устанавливаем параметр text на кнопку новая игра
# btn_new_game['padding'] = (10, 0, 10, 0)


footer.pack(anchor=S, padx=5, pady=5) # выводим рамку на экран
rootWindow.mainloop()
