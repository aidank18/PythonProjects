from EditCard import EditCard as ec
import tkinter as tk
from tkinter import ttk
from tkinter import tix
import UpdateFile as up
from MyButton import MyButton as mb
from Card import Card
from ScrollableFrame import ScrollableFrame as SFrame

class EditSet:

    def __init__(self, window, setname):
        self.window = window
        self.set = []
        self.editSet = []
        self.setname = setname
        self.addButton = mb(self.window, text = "New Card", width = 25, command = self.clickAdd)
        self.readFile()


    def readFile(self):
        set = open(self.setname)
        aspects = [None, None, None, None, None]
        for i, line in enumerate(set, start = 1):
            aspects[i % 5] = line[:-1]
            if i % 5 == 0:
                self.makeCard(aspects, (i / 5) - 1)
        set.close()

    def makeCard(self, aspects, index):
        if aspects[0] == "F":
            aspects[0] = False
        else:
            aspects[0] = True
        self.set.append([Card(self.window, aspects[1], aspects[3], aspects[2],
        aspects[4]), aspects[0]])
        self.editSet.append(self.makeEditCard(self.set[-1][0], index))

    def makeEditCard(self, card, index):
        edit = []
        edit.append(ec(self.window, card))
        edit.append(mb(self.window, text = "Edit", command = lambda index = index: self.editCard(index),
        x = 550, y = (index * 225) + 55, id = index))
        edit.append(mb(self.window, text = "Delete", command = lambda index = index: self.deleteCard(index),
        x = 550, y = (index * 225) + 105, id = index))
        edit.append(mb(self.window, text = "Done", command = lambda index = index: self.redisplay(index),
        x = 950, y = 50, id = index))
        return edit

    def updateIndex(self, index):
        index = int(index)
        self.editSet[index][1].command = lambda index = index: self.editCard(index)
        self.editSet[index][2].command = lambda index = index: self.deleteCard(index)
        self.editSet[index][3].command = lambda index = index: self.redisplay(index)

    def displayEC(self, index, small = True):
        if small:
            self.updateIndex(index)
            self.editSet[index][0].smallDisplay(top = ((index + 1) * 225) - 185)
            self.editSet[index][1].display(x = 550, y = (index * 225) + 55)
            self.editSet[index][2].display(x = 550, y = (index * 225) + 105)
        else:
            self.editSet[index][0].editDisplay()
            self.editSet[index][3].display()

    def deleteEC(self, index):
        self.editSet[index][0].delete()
        self.editSet[index][1].delete()
        self.editSet[index][2].delete()
        self.editSet[index][3].delete()

    def deleteECS(self):
        for i, edit in enumerate(self.editSet):
            self.deleteEC(i)

    def display(self):
        i = 0
        for i in range(0, len(self.editSet)):
            self.displayEC(i)
        if len(self.set) != 0:
            self.addButton.display(x = 150, y = ((i + 2) * 225) - 185)
        else:
            self.addButton.display(x = 150, y = ((i + 1) * 225) - 185)
        self.window.config(height = (i + 2) * 225)



    def editCard(self, index):
        self.deleteECS()
        self.addButton.delete()
        index = int(index)
        self.window.config(width = 1050)
        self.displayEC(index, False)

    def deleteCard(self, index):
        self.deleteECS()
        self.addButton.delete()
        index = int(index)
        del self.set[index]
        del self.editSet[index]
        self.display()

    def redisplay(self, index):
        index = int(index)
        self.deleteEC(index)
        self.display()

    def updateFile(self):
        up.update(self.set, self.setname)

    def addCard(self):
        aspects = ["F", "", "", "", ""]
        self.makeCard(aspects, len(self.set))

    def clickAdd(self):
        self.addCard()
        self.editCard(len(self.set) - 1)

    def exit(self):
        self.updateFile()
        self.deleteECS()
        self.addButton.delete()
        return len(self.set)


window = tk.Tk()
window.geometry("900x600")
#--------------------
frame = SFrame(window) #650
frame.pack(fill = "both")
frame.scrollable_frame.config(width = 685, height = 1300)
canvas = tk.Canvas(frame.scrollable_frame, width = 10000, height = 100000)
canvas.place(x=0,y=0)
# scrollbar = tk.Scrollbar(window)
# scrollbar.pack(side = tk.RIGHT, fill = "y")
window.minsize(700, 200)
#frame.config(yscrollcommand = scrollbar.set)
# frame.scrollable_frame.config(bg = "white")
#-----------------
# scrollbar = tk.Scrollbar(window)
# scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
#
# canvas = tk.Canvas(window, scrollregion = window.bbox('all'), width = 630)
# canvas.place()
#-------------------
# container = ttk.Frame(window)
# container.pack(side = "left", fill = "both")
# canvas = tk.Canvas(container)
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")
# scrollable_frame = ttk.Frame(canvas)
# scrollable_frame.pack(side = "left", fill = "both")
#
# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# canvas.configure(yscrollcommand=scrollbar.set)


#---------------
test = EditSet(frame.scrollable_frame, "cardStoringTest.txt")
test.display()
#scrollbar.lift()
window.mainloop()
test.updateFile()

#.place(relx=1, rely=0, relheight=1, anchor='ne')
