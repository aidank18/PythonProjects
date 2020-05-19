import tkinter as tk

class TicTacToe:

    def __init__(self):
        self.__win = tk.Tk()
        self.__p1 = True
        self.__win.title("Tic Tac Toe")
        self.__buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.__set()

    def run(self):
        self.__win.mainloop()


    def __click(self, button):
        if button["text"] == "X" or button["text"] == "O":
            return
        if self.__p1:
            button.config(text = "X")
        else:
            button.config(text = "O")
        if self.__checkWin():
            self.__endGame()
        self.__p1 = not self.__p1

    def __checkWin(self):
        for i in range(0,3):
            if self.__checkRow(i) or self.__checkCol(i):
                return True
        return self.__checkDiag()


    def __checkRow(self, row):
        if self.__buttons[row][0]["text"] == self.__buttons[row][1]["text"]:
            if self.__buttons[row][1]["text"] == self.__buttons[row][2]["text"]:
                return True
        return False

    def __checkCol(self, col):
        if self.__buttons[0][col]["text"] == self.__buttons[1][col]["text"]:
            if self.__buttons[1][col]["text"] == self.__buttons[2][col]["text"]:
                return True
        return False

    def __checkDiag(self):
        if self.__buttons[0][0]["text"] == self.__buttons[1][1]["text"]:
            if self.__buttons[1][1]["text"] == self.__buttons[2][2]["text"]:
                return True
        if self.__buttons[0][2]["text"] == self.__buttons[1][1]["text"]:
            if self.__buttons[1][1]["text"] == self.__buttons[2][0]["text"]:
                return True
        return False

    def __endGame(self):
        for row in self.__buttons:
            for button in row:
                button.destroy()
        if self.__p1:
            message = tk.Message(text = "X won!!")
        else:
            message = tk.Message(text = "O won!!")
        message.place(x = 45, y = 70)
        message.config(font = ("Courier", 50))
        button = tk.Button(text = "quit", command = self.__stop, font =
        ("Courier", 20))
        button.place(x = 50, y = 180)
        button2 = tk.Button(text = "play again", font = ("Courier", 20))
        button2.place(x = 50, y = 215)
        widgets = [message, button, button2]
        button2.config(command = lambda test = widgets : self.__reset(test))

    def __stop(self):
        self.__win.destroy()

    def __reset(self, widgets):
        self.__p1 = True
        for wid in widgets:
            wid.destroy()
        self.__set()

    def __set(self):
        i = 0
        for row in range(0, 3):
            for col in range(0, 3):
                i += 1
                self.__buttons[row][col] = tk.Button(self.__win, text = str(i),
                padx = 20, pady = 17)
                self.__buttons[row][col].config(command = lambda button =
                self.__buttons[row][col]: self.__click(button))
                self.__buttons[row][col].place(x = (col + 1) * 50,
                y = (row + 1) * 50)

game = TicTacToe()
game.run()
