from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из игры?" ):
        root.destroy()



root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Scrabble')
root.geometry('850x850')
root.resizable(width=False, height=False)

width = 850
heigh = 850
screenwidth = root.winfo_screenwidth()# что бы окно по центру всплывало
screenheight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
image = PhotoImage(file='img/5.png')
bg_logo = Label(root, image=image)
bg_logo.grid(row=0, column=0)

def start_window_2():
    os.system("python game.py")
    sys.exit(0)

btn = Button(root, text='Start!', bg='#bc201d', fg='#cfb28a', font=('Comic Sans MS', 20, 'bold'), command=start_window_2)
btn.place(x =470, y=160, width=120, height=60 )

root.mainloop()




