import tkinter as tk
from tkinter import filedialog
from random import randint


class Cipher:
    text = ""
    crypt = ""
    keys = ""

def select_radio():
    action = select_action.get()
    if action == 1:
        btn_key.grid(row=1, column=1)
    else:
        btn_key.grid_forget()


def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    Cipher.text = file.read()
    file.close()

def openKeyFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    Cipher.keys = file.read()
    file.close()


def decipher():
    action = select_action.get()
    if action == 0:
        Cipher.keys = ""
        Cipher.crypt = ""
        for i in Cipher.text:
            key = randint(65, 91)
            Cipher.keys += chr(key)
            Cipher.crypt += chr(ord(i) ^ key)
        f_crypt = open("crypt.txt", "w")
        f_crypt.write(Cipher.crypt)
        f_crypt.close
        f_key = open("keys.txt", "w")
        f_key.write(Cipher.keys)
        f_key.close


    else:
        new = [chr(ord(a) ^ ord(b)) for a, b in zip(Cipher.crypt, Cipher.keys)]
        result = "".join(new)
        f = open("result.txt", "w")
        f.write(result)
        f.close


win = tk.Tk()
win.title("Encrypt")
win.geometry("220x160")
win.resizable(False, False)

select_action = tk.IntVar()

label_1 = tk.Label(win, text="Файл",
                   font=("Arial", 14, "bold"),
                   padx=20,
                   pady=10,
                   ).grid(row=0, column=0)
tk.Label(win, text="Ключ",
         font=("Arial", 14, "bold"),
         padx=20,
         pady=10,
         ).grid(row=1, column=0)

tk.Radiobutton(win, text="Зашифровать", variable=select_action, value=0, command=select_radio).grid(row=2, column=0)
tk.Radiobutton(win, text="Расшифровать", variable=select_action, value=1, command=select_radio).grid(row=2, column=1)

btn_file = tk.Button(win, text="Выберите файл", command=openFile, font=("Arial", 10)).grid(row=0, column=1)
btn_key = tk.Button(win, text="Выберите файл", font=("Arial", 10), command=openKeyFile)

tk.Button(win, text="Выполнить", font=("Arial", 14, "bold"), command=decipher).grid(row=3, column=0, columnspan=2)

win.mainloop()