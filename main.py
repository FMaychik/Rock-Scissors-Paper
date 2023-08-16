import random
import tkinter as tk
from tkinter.messagebox import showinfo, askyesno
from tkinter import font
import pickle
import sys


def save_last_item():
    with open("last_item.pkl", "wb") as f:
        pickle.dump(last_item, f)

def load_last_item():
    try:
        with open("last_item.pkl", "rb") as f:
            last_item = pickle.load(f)
            lbl.config(text=last_item)
    except FileNotFoundError:
        lbl.config(text="Тут будет последний предмет!")

def play():
    global last_item
    nm = random.randint(1, 3)
    if nm == 1:
        showinfo(title="Game", message="Камень")
        last_item = "Камень"
        lbl.config(text=last_item)
    elif nm == 2:
        showinfo(title="Game", message="Ножницы")
        last_item = "Ножницы"
        lbl.config(text=last_item)
    elif nm == 3:
        showinfo(title="Game", message="Бумага")
        last_item = "Бумага"
        lbl.config(text=last_item)
    save_last_item()

def ext():
    e = askyesno(title="Game", message="Вы точно хотите выйти из игры?")
    if e:
        exit()
    else:
        showinfo(title="Game", message="Вы остались в игре!")

def arl():
    font2.config(family="Arial", size=11, weight="normal")

def df():
    font2.config(family="Comic sans ms", size=11, weight="normal")

win = tk.Tk()
win.geometry("400x300")
win.title("Game")
win.config(bg='grey')

#fonts
font2 = font.Font(family="Comic sans ms", size=11, weight="normal")

#diseng

shi = tk.Menu(win)

file_menu = tk.Menu(shi, tearoff=0)
file_menu.add_command(label="Новый", command=arl)
file_menu.add_command(label="Обычный", command=df)

shi.add_cascade(label="Ширифт", menu=file_menu)

win.config(menu=shi)

bg = 'grey'

label2 = tk.Label(win, text="Камень, ножницы, бумага", background=bg, font=font2)
label2.pack()

btn = tk.Button(win, text="Play", command=play, font=font2)
btn.pack()

btn = tk.Button(win, text="Exit", command=ext, background="red", font=font2)
btn.pack()

lbl = tk.Label(win, text="Тут будет последний предмет!", background=bg, foreground="blue", font=font2)
lbl.pack()

load_last_item()

win.mainloop()