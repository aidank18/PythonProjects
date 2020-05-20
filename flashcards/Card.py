# Card class
# Writen By: Aidan Knerr
# uses tkinter and ttk to create a GUI flashcard with a front and back and hints

import tkinter as tk
from tkinter import ttk

class Card:

    # initializes all necisary values for the program
    def __init__(self, win, front = "", back = "", fHint = "", bHint = "",
    startOnFront = True, mark = False, left = 100, right = 600, top = 100,
    bottom = 400):
        self.window = win
        self.front = front
        self.back = back
        self.fHint = fHint
        self.bHint = bHint
        self.onFront = startOnFront
        self.marked = mark
        self.canvas = None
        self.messageWindow = None
        self.markButton = None
        self.flipButton = None
        self.hintButton = None
        self.hintWindow = None
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    """
    * Purpose: displays the notecard in the window given when initialized
    * Arguments: none
    * Returns: nothing
    * Effects: none
    * Notes: none
    """
    def display(self):
        self.createOutline()
        self.addText()
        self.addButtons()


    """
    * Purpose: deletes the notecard
    * Arguments: none
    * Returns: a None val
    * Effects: none
    * Notes: none
    """
    def delete(self):
        self.canvas.destroy()
        self.messageWindow.destroy()
        self.flipButton.destroy()
        self.hintButton.destroy()
        if self.hintWindow != none:
            self.hintWindow.destroy()
        self.markButton.destroy()
        return None

    """
    * Purpose: creates the outline of the notecard
    * Arguments: none
    * Returns: nothing
    * Effects: runs horizontalLine and verticalLine functions and creates a
    *          canvas
    * Notes: none
    """
    def createOutline(self):
        self.canvas = tk.Canvas(self.window, width = (self.left + self.right),
        height = (self.bottom + self.top))
        self.canvas.grid(row = 0, column = 0)
        self.horizontalLine(True)
        self.horizontalLine(False)
        self.verticalLine(True)
        self.verticalLine(False)

    """
    * Purpose: creates a horizontal line
    * Arguments: a bool thats true if the line is the top of the card
    * Returns: nothing
    * Effects: draws on the canvas
    * Notes: none
    """
    def horizontalLine(self, top):
        if top:
            self.canvas.create_line(self.left, self.top, self.right, self.top)
        else:
            self.canvas.create_line(self.left, self.bottom, self.right,
            self.bottom)

    """
    * Purpose: draws a vertical line
    * Arguments: a bool thats true if the line is the left of the card
    * Returns: nothing
    * Effects: draws on the canvas
    * Notes: none
    """
    def verticalLine(self, left):
        if left:
            self.canvas.create_line(self.left, self.top, self.left, self.bottom)
        else:
            self.canvas.create_line(self.right, self.top, self.right,
            self.bottom)

    """
    * Purpose: adds text to the notecard
    * Arguments: none
    * Returns: nothing
    * Effects: creates a messagebox
    * Notes: text in the box changes based on the side of the card we are on
    """
    def addText(self):
        if self.onFront:
            self.messageWindow = tk.Message(self.window, text = self.front,
            width = (self.right - self.left - 100))
            self.setFont(self.front, self.messageWindow, True)
        else:
            self.messageWindow = tk.Message(self.window, text = self.back,
            width = (self.right - self.left - 100))
            self.setFont(self.back, self.messageWindow, True)
        self.messageWindow.grid(row = 0, column = 0)

    """
    * Purpose: determines the size of the font based on the length of the text
    * Arguments: the text to be judged, the messagebox the text is in, and a
    *            bool thats true if the font can be in its biggest form
    * Returns: nothing
    * Effects: changes the size of the font in the messagebox
    * Notes: want to change this so the cutoffs scale with the size of the card
    """
    def setFont(self, text, message, big = False):
        if len(text) < 20 and big:
            message.config(font = ("Courier", 35))
        elif len(text) < 55:
            message.config(font = ("Courier", 25))

    """
    * Purpose: adds flip mark and hint buttons
    * Arguments: none
    * Returns: nothing
    * Effects: none
    * Notes: should remove the mark button
    """
    def addButtons(self):
        self.flipButton = ttk.Button(self.window, text = "Flip",
        command = self.flipCard)
        self.flipButton.place(x = ((self.right - self.left) / 2) + self.left-40,
         y = self.bottom - 40)

        self.hintButton = ttk.Button(self.window, text = "Hint?",
        command = self.clickHint)
        self.hintButton.place(x = ((self.right - self.left) / 2) + self.left+60,
         y = self.bottom - 40)

        self.markButton = tk.Button(self.window, text = "Mark",
         command = self.markCard, font = ("Courier", 15))
        self.markButton.place(x = 490, y = 120)

    """
    * Purpose: marks the card for extra practice
    * Arguments: none
    * Returns: nothing
    * Effects: changes the color and size of the text
    * Notes: should take this out
    """
    def markCard(self):
        if not self.marked:
            self.markButton.config(fg = "green", font = ("Courier", 25),
            text = "Marked")
        else:
            self.markButton.config(fg = "black", font = ("Courier", 15),
            text = "Mark")
        self.marked = not self.marked

    """
    * Purpose: changes the card from the front to the back of vice versa
    * Arguments: none
    * Returns: nothing
    * Effects: remves the hint window if its active and removes the
    *          messageWindow and replaces it with the appropriate text
    * Notes: activates when the flip button is clicked
    """
    def flipCard(self):
        if self.hintWindow != None:
            self.hintWindow = self.removeWidget(self.hintWindow)
        self.removeWidget(self.messageWindow)
        self.onFront = not self.onFront
        self.addText()

    """
    * Purpose: adds the hint window if it doesnt exist and removes it if it does
    * Arguments: none
    * Returns: nothing
    * Effects: none
    * Notes: activates when the hint button is clicked
    """
    def clickHint(self):
        if self.hintWindow == None:
            self.addHint()
        else:
            self.hintWindow = self.removeWidget(self.hintWindow)

    """
    * Purpose: removes the given widget
    * Arguments: the widget to be removed
    * Returns: None value
    * Effects: none
    * Notes: none
    """
    def removeWidget(self, widget):
        widget.destroy()
        return None

    """
    * Purpose: adds the hint text
    * Arguments: none
    * Returns: nothing
    * Effects: chages hint depending on if we are on the front or back
    * Notes: dont use if the hint already exists
    """
    def addHint(self):
        if self.onFront:
            self.hintWindow = tk.Message(self.window,
            text = "Hint: " + self.fHint, width = self.right - self.left)
            self.setFont(self.fHint, self.hintWindow)
        else:
            self.hintWindow = tk.Message(self.window,
            text = "Hint: " + self.bHint, width = self.right - self.left)
            self.setFont(self.bHint, self.hintWindow)
        self.hintWindow.place(x = self.left, y = self.bottom + 30)


window = tk.Tk()
card = Card(window, "Hola", fHint = "aaaaaaaa aaaaa aaaaaa aaaaaaa aaaaaaaaaaa aaaaa aaaa aaaaa",
back = "Hello")
card.display()
window.mainloop()
