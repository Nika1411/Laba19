#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


root = Tk()
e1 = Entry(width=50)


def insert():
    e1.insert(0, "Tkinter - GUI ")


but = Button(text="Вставить", command=insert)
e1.pack()
but.pack()
root.mainloop()
