import tkinter as tk
from tkinter import ttk

class MyButton:

    def __init__(self, win, text = "", fc = "black", font = ("Courier", 25),
    x = 0, y = 0, width = 5, command = None, padx = 5, pady = 5, tk = False, id = -1):
        self.window = win
        self.text = text
        self.fc = fc
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.command = command
        self.padx = padx
        self.pady = pady
        self.id = id
        self.tk = tk
        self.button = None

    def display(self, x = None, y = None):
        if self.tk:
            self.button = tk.Button(self.window, text = self.text, fg = self.fc,
             font = self.font, width = self.width, command = self.command,
              padx = self.padx, pady = self.pady)
        else:
            self.button = ttk.Button(self.window, text = self.text,
             width = self.width, command = self.command)
        if x == None and y == None:
            self.button.place(x = self.x, y = self.y)
        else:
            self.button.place(x = x, y = y)

    def delete(self):
        if self.button != None:
            self.button.destroy()
