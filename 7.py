#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
root = Tk()

text = Text(width=100, height=10)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

root.mainloop()
