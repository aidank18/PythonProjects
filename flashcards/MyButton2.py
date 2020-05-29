#Create a few easy to use themes with the ttk buttons such as a large theme
#or a start theme
from tkinter import *
from tkinter.ttk import *



class ThemedButton:
    def __init__(self, window):
        self.window = window
        self.button = None
        ttk.Style().configure("big", padding = 20)

    def display(self, theme):
        return


    def delete(self):
        return
