# from tkinter import *
from re import X
import tkinter as tk

def generate():
    print("Inside Generate Function")
    pass

main = tk.Tk()
main.config(background="red", height = "1200", width=  "720")

generateButton=tk.Button(text = "Click Here", background = "orange", command = generate)
generateButton.grid(row = 2, column = 5)
main.mainloop()