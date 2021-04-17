#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def sel():
    s = str(var.get())
    l1.config(text=s)


root = Tk()
f_top = Frame(root)
f_bot = Frame(root)

var = IntVar()
r1 = Radiobutton(f_top, text='Вася', indicatoron=0, width=15, height=3, state=ACTIVE, variable=var,
                 value='89097525555', command=sel)
r2 = Radiobutton(f_top, text='Петя', indicatoron=0, width=15, height=3, state=ACTIVE, variable=var,
                 value='87512456635', command=sel)
r3 = Radiobutton(f_top, text='Маша', indicatoron=0, width=15, height=3, state=ACTIVE, variable=var,
                 value='84652487598', command=sel)
l1 = Label(f_bot, width=30, bg="white", height=11)

f_top.pack(side=LEFT)
f_bot.pack(side=LEFT)
r1.pack(pady=1)
r2.pack(pady=1)
r3.pack(pady=1)
l1.pack()

root.mainloop()
