#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

root = Tk()


def red():
    lab['text'] = "красный"
    ent.delete(0, END)
    ent.insert(0, "#ff0000")


def oran():
    lab['text'] = "оранжевый"
    ent.delete(0, END)
    ent.insert(0, "#ff7d00")


def yellow():
    lab['text'] = "желтый"
    ent.delete(0, END)
    ent.insert(0, "#ffff00")


def green():
    lab['text'] = "зеленый"
    ent.delete(0, END)
    ent.insert(0, "#00ff00")


def sblue():
    lab['text'] = "голубой"
    ent.delete(0, END)
    ent.insert(0, "#007dff")


def blue():
    lab['text'] = "синий"
    ent.delete(0, END)
    ent.insert(0, "#0000ff")


def purple():
    lab['text'] = "фиолетовый"
    ent.delete(0, END)
    ent.insert(0, "#7d00ff")


ent = Entry(root, width=25)
lab = Label(
    root,
    width=20
)
but1 = Button(
    root,
    bg='#ff0000',
    width=20
)
but2 = Button(
    root,
    bg='#ff7d00',
    width=20
)
but3 = Button(
    root,
    bg='#ffff00',
    width=20
)
but4 = Button(
    root,
    bg='#00ff00',
    width=20
)
but5 = Button(
    root,
    bg='#007dff',
    width=20
)
but6 = Button(
    root,
    bg='#0000ff',
    width=20
)
but7 = Button(
    root,
    bg='#7d00ff',
    width=20
)

but1['command'] = red
but2['command'] = oran
but3['command'] = yellow
but4['command'] = green
but5['command'] = sblue
but6['command'] = blue
but7['command'] = purple
lab.pack()
ent.pack(pady=2)
but1.pack(pady=1)
but2.pack(pady=1)
but3.pack(pady=1)
but4.pack(pady=1)
but5.pack(pady=1)
but6.pack(pady=1)
but7.pack(pady=1)

root.mainloop()
