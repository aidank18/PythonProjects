from Card import *
from random import random
import UpdateFile as up

class StudySet:

    def __init__(self, window, setname, startOnFront = True):
        self.window = window
        self.setname = setname
        self.set = []
        self.order = []
        self.curr = 0
        self.markedCount = 0
        self.startOnFront = startOnFront
        self.cards = self.readFile()
        self.onlyMarked = False
        self.markButton = None
        self.nextButton = None
        self.shuffleButton = None
        self.unshuffleButton = None
        self.backButton = None
        self.resetButton = None
        self.onlyMarkedButton = None
        self.quitButton = None
        self.noMarkedCardsMessage = None



    def readFile(self):
        set = open(self.setname)
        aspects = [None, None, None, None, None]
        for i, line in enumerate(set, start = 1):
            aspects[i % 5] = line[:-1]
            if i % 5 == 0:
                self.makeCard(aspects)
                self.order.append(int((i / 5) - 1))
        set.close()

    def makeCard(self, aspects):
        if aspects[0] == "F":
            aspects[0] = False
        else:
            aspects[0] = True
            self.markedCount += 1
        self.set.append([Card(self.window, aspects[1], aspects[3], aspects[2],
        aspects[4], self.startOnFront), aspects[0]])

    def display(self):
        test.set[0][0].display()
        self.addButtons()
        self.addNoMarkedMessage()
        self.loadMark()

    def addNoMarkedMessage(self):
        if self.markedCount == 0:
            self.noMarkedCardsMessage = tk.Message(self.window,
            text = "No Marked Cards", font = ("Courier", 25))
            self.noMarkedCardsMessage.place(x = 670, y = 300)
        else:
            if self.noMarkedCardsMessage != None:
                self.noMarkedCardsMessage.destroy()
                self.noMarkedCardsMessage = None

    def delete(self):
        self.set[self.order[self.curr]][0].delete()
        self.markButton.destroy()
        self.nextButton.destroy()
        self.shuffleButton.destroy()
        self.unshuffleButton.destroy()
        self.backButton.destroy()
        self.resetButton.destroy()
        self.onlyMarkedButton.destroy()
        self.quitButton.destroy()
        if self.noMarkedCardsMessage != None:
            self.noMarkedCardsMessage.destroy()

    def addButtons(self):
        self.markButton = tk.Button(self.window, text = "Mark",
         command = self.clickMark, font = ("Courier", 15))
        self.markButton.place(x = 490, y = 120)

        self.nextButton = ttk.Button(self.window, text = "Next",
        command = self.clickNext)
        self.nextButton.place( x = 210, y = 360)

        self.shuffleButton = ttk.Button(self.window, text = "Shuffle",
        command = self.clickShuffle)
        self.shuffleButton.place(x = 650, y = 100)

        self.unshuffleButton = ttk.Button(self.window, text = "Un-Shuffle",
         width = 9, command = self.clickUnshuffle)
        self.unshuffleButton.place(x = 750, y = 100)

        self.backButton = ttk.Button(self.window, text = "Back",
        command = self.clickBack)
        self.backButton.place(x = 650, y = 140)

        self.resetButton = ttk.Button(self.window, text = "Start over",
        width = 9, command = self.clickStartOver)
        self.resetButton.place(x = 750, y = 140)

        self.onlyMarkedButton = ttk.Button(self.window,
        text = "Study Only Marked Cards", width = 20,
        command = self.clickOnlyMarked)
        self.onlyMarkedButton.place(x = 650, y = 180)

        self.quitButton = ttk.Button(self.window, text = "Quit Set", width = 20,
         command = self.clickQuit)
        self.quitButton.place(x = 650, y = 220)

    def clickOnlyMarked(self):
        if self.markedCount == 0:
            #display message
            return
        self.onlyMarked = not self.onlyMarked
        if self.onlyMarked:
            self.onlyMarkedButton.config(text = "Study All")
            if not self.set[self.order[self.curr]][1]:
                self.set[self.order[self.curr]][0].delete()
                self.findMarked()
                self.set[self.order[self.curr]][0].display()
                self.liftButtons()
                self.loadMark()
        else:
            self.onlyMarkedButton.config(text = "Study Only Marked Cards")


    def findMarked(self, forward = True):
        if self.markedCount == 0:
            return False
        while not self.set[self.order[self.curr]][1]:
            if forward:
                self.curr += 1
                if self.curr >= len(self.order):
                    self.curr = 0
            else:
                self.curr -= 1
                if self.curr < 0:
                    self.curr = len(self.order) - 1
        return True


    def clickUnshuffle(self):
        self.set[self.order[self.curr]][0].delete()
        for i in range(0, len(self.order)):
            self.order[i] = i
        if self.onlyMarked:
            self.findMarked()
        self.set[self.order[self.curr]][0].display()
        self.liftButtons()
        self.loadMark()

    def clickShuffle(self):
        self.set[self.order[self.curr]][0].delete()
        self.mixOrder()
        if self.onlyMarked:
            self.findMarked()
        self.set[self.order[self.curr]][0].display()
        self.liftButtons()
        self.loadMark()

    def mixOrder(self):
        for i in range(0, len(self.order) * 7):
            val1 = self.randomNum()
            val2 = self.randomNum()
            temp = self.order[val1]
            self.order[val1] = self.order[val2]
            self.order[val2] = temp


    def randomNum(self):
        return int(random() * (len(self.set)))

    def clickQuit(self):
        self.delete()
        up.update(self.set, self.setname)

    def clickStartOver(self):
        self.set[self.order[self.curr]][0].delete()
        self.curr = 0
        if self.onlyMarked:
            self.findMarked()
        self.set[self.order[self.curr]][0].display()
        self.liftButtons()
        self.loadMark()

    def clickBack(self):
        self.set[self.order[self.curr]][0].delete()
        self.curr -= 1
        if self.curr < 0:
            self.curr = len(self.set) - 1
        if self.onlyMarked:
            self.findMarked(False)
        self.set[self.order[self.curr]][0].display()
        self.liftButtons()
        self.loadMark()

    def clickNext(self):
        self.set[self.order[self.curr]][0].delete()
        self.curr += 1
        if self.curr >= len(self.set):
            self.curr = 0
        if self.onlyMarked:
            self.findMarked()
        self.set[self.order[self.curr]][0].display()
        self.liftButtons()
        self.loadMark()

    def liftButtons(self):
        self.markButton.lift()
        self.nextButton.lift()
        self.shuffleButton.lift()
        self.backButton.lift()
        self.onlyMarkedButton.lift()
        self.quitButton.lift()
        if self.noMarkedCardsMessage != None:
            self.noMarkedCardsMessage.lift()

    def loadMark(self):
        if self.set[self.order[self.curr]][1]:
            self.markCard()
        else:
            self.unmarkCard()

    """
    * Purpose: marks the card for extra practice
    * Arguments: none
    * Returns: nothing
    * Effects: changes the color and size of the text
    * Notes: should take this out
    """
    def clickMark(self):
        if not self.set[self.order[self.curr]][1]:
            self.markCard()
            self.markedCount += 1
            self.set[self.order[self.curr]][1] = (not
            self.set[self.order[self.curr]][1])
        else:
            self.unmarkCard()
            self.markedCount -= 1
            if self.markedCount == 0:
                self.onlyMarkedButton.config(text = "Study Only Marked Cards")
                self.onlyMarked = False
                #display Message
            self.set[self.order[self.curr]][1] = (not
            self.set[self.order[self.curr]][1])
            if self.onlyMarked:
                self.clickNext()
        self.addNoMarkedMessage()

    def markCard(self):
        self.markButton.config(fg = "green", font = ("Courier", 25),
        text = "Marked")

    def unmarkCard(self):
        self.markButton.config(fg = "black", font = ("Courier", 15),
        text = "Mark")

window = tk.Tk()
window.geometry("900x600")
test = StudySet(window, "cardStoringTest.txt")
test.display()
window.mainloop()
