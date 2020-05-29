from Card import *
import tkinter as tk


class EditCard:
    def __init__(self, window, card):
        self.original = card
        self.window = window
        self.fCard = Card(window, card.front, card.back, card.fHint,
        card.bHint, small = True)
        self.bCard = Card(window, card.front, card.back, card.fHint,
        card.bHint, False, small = True)
        self.changeFront = None
        self.frontMessage = None
        self.commitFront = None
        self.changeBack = None
        self.backMessage = None
        self.commitBack = None
        self.changeFHint = None
        self.fHintMessage = None
        self.commitFHint = None
        self.changeBHint = None
        self.bHintMessage = None
        self.commitBHint = None



    def smallDisplay(self, top = 50):
        self.fCard.left = 50
        self.fCard.right = 250
        self.fCard.top = top
        self.fCard.bottom = top + 100
        self.fCard.displayNB()
        self.fCard.addHint()
        self.bCard.left = 300
        self.bCard.right = 500
        self.bCard.top = top
        self.bCard.bottom = top + 100
        self.bCard.displayNB()
        self.bCard.addHint()

    def editDisplay(self):
        self.fCard.left = 50
        self.fCard.right = 450
        self.fCard.top = 50
        self.fCard.bottom = 250
        self.fCard.displayNB()
        self.fCard.addHint()
        self.bCard.left = 500
        self.bCard.right = 900
        self.bCard.top = 50
        self.bCard.bottom = 250
        self.bCard.displayNB()
        self.bCard.addHint()
        self.addEditors()

    def addEditors(self):
        self.changeFront, self.frontMessage, self.commitFront = self.addEditor(x
         = self.fCard.left, y = self.fCard.bottom + 80, message = "Change Front", command = self.editFront)

        self.changeBack, self.backMessage, self.commitBack = self.addEditor(x =
        self.bCard.left, y = self.bCard.bottom + 80, message = "change Back", command = self.editBack)

        self.changeFHint, self.fHintMessage, self.commitFHint = self.addEditor(x
         = self.fCard.left, y = self.fCard.bottom + 150, message =
        "Change Front Hint", command = self.editFHint)

        self.changeBHint, self.bHintMessage, self.commitBHint = self.addEditor(x
         = self.bCard.left, y = self.bCard.bottom + 150, message =
        "change Back Hint", command = self.editBHint)


    def addEditor(self, x, y, message, width = 35, command = None):
        editor = tk.Entry(self.window, width = width)
        editor.place(x = x + 65, y = y)
        messagebox = tk.Message(self.window, text = message, width = 60)
        messagebox.place(x = x, y = y)
        button = tk.Button(self.window, command = command, text = "Commit Change")
        button.place(x = x + 65, y = y + 30)
        return editor, messagebox, button


    def editFront(self):
        self.original.front = self.changeFront.get()
        self.fCard.front = self.changeFront.get()
        self.fCard.delete()
        self.fCard.displayNB()
        self.fCard.addHint()

    def editFHint(self):
        self.original.fHint = self.changeFHint.get()
        self.fCard.fHint = self.changeFHint.get()
        self.fCard.delete()
        self.fCard.displayNB()
        self.fCard.addHint()

    def editBack(self):
        self.original.back = self.changeBack.get()
        self.bCard.back = self.changeBack.get()
        self.bCard.delete()
        self.bCard.displayNB()
        self.bCard.addHint()

    def editBHint(self):
        self.original.bHint = self.changeBHint.get()
        self.bCard.bHint = self.changeBHint.get()
        self.bCard.delete()
        self.bCard.displayNB()
        self.bCard.addHint()

    def delete(self):
        self.fCard.delete()
        self.bCard.delete()
        if self.changeFront != None:
            self.deleteEditors()

    def deleteEditors(self):
        self.changeFront.destroy()
        self.frontMessage.destroy()
        self.commitFront.destroy()
        self.changeBack.destroy()
        self.backMessage.destroy()
        self.commitBack.destroy()
        self.changeFHint.destroy()
        self.fHintMessage.destroy()
        self.commitFHint.destroy()
        self.changeBHint.destroy()
        self.bHintMessage.destroy()
        self.commitBHint.destroy()
