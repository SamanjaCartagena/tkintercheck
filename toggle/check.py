# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:43:42 2024

@author: c.samanja09
"""

from tkinter import *
import ttkbootstrap as tb

root=tb.Window(themename='superhero')

root.title("TTK Bootstrap!")
root.geometry('500x350')

def checker():
    if var1.get() == 1:
        my_label.config(text="Checked!")
    else:
        my_label.config(text="Unchecked!")
my_label=Label(text="Click the checkbutton below", font=("Helvetica",18))
my_label.pack(pady=(40,10))

var1=IntVar()
my_check=tb.Checkbutton(bootstyle="primary", 
                        text="Check",
                        variable=var1,
                        onvalue=1,
                        offvalue=0,
                        command=checker)
my_check.pack(pady=10)

root.mainloop()