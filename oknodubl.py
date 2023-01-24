
from tkinter import *
from tkinter import messagebox
import tkin
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из игры?" ):
        root.destroy()



root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Scrabble')
root.geometry('945x945')
root.resizable(width=False, height=False)

# root.image = PhotoImage(file='img/5.png')
# bg_logo = Label(root, image=root.image)
# bg_logo.grid(row=0, column=0)

def start_window_2():
    Toplevel(tkin.rootWindow) #как сделать что бы открывалось окно со скраблом?

btn = Button(root, text='Start!', bg='#bc201d', fg='#cfb28a', font=('Comic Sans MS', 20, 'bold'), command=start_window_2)
btn.place(x =470, y=160, width=120, height=60 )

root.mainloop()