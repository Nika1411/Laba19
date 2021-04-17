#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


root = Tk()


def summa():
    get_ent1 = ent1.get()
    get_ent2 = ent2.get()
    z = int(get_ent1) + int(get_ent2)
    lab['text'] = z


def sub():
    get_ent1 = ent1.get()
    get_ent2 = ent2.get()
    z = int(get_ent1) - int(get_ent2)
    lab['text'] = z


def multi():
    get_ent1 = ent1.get()
    get_ent2 = ent2.get()
    z = int(get_ent1) * int(get_ent2)
    lab['text'] = z


def div():
    get_ent1 = ent1.get()
    get_ent2 = ent2.get()
    z = int(get_ent1) / int(get_ent2)
    lab['text'] = z


ent1 = Entry(root, width=20)
ent2 = Entry(root, width=20)
but1 = Button(
    root,
    text="/",
    width=17
)
but2 = Button(
    root,
    text="*",
    width=17
)
but3 = Button(
    root,
    text="+",
    width=17
)
but4 = Button(
        root,
        text="-",
        width=17
)
lab = Label(
        root,
        width=20,
        bg='#00CED1',
        fg='white'
)

but1['command'] = div
but2['command'] = multi
but3['command'] = sum
but4['command'] = sub
ent1.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()

root.mainloop()
