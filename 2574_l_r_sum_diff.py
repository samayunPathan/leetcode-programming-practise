import tkinter as tk

class TicTacToe(tk.Tk):

    def __init__(self):
        super().__init__()

        self.board = [[tk.Label(text=" ") for _ in range(3)] for _ in range(3)]
        for row in self.board:
            for cell in row:
                cell.grid(row=row, column=cell)

        self.turn = "X"
        self.winner = None

        self.buttons = []
        for i in range(9):
            button = tk.Button(text=" ", command=self.on_click)
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.label = tk.Label(text="")
        self.label.grid(row=3, column=0, columnspan=3)

    def on_click(self, event):
        button = event.widget
        index = button.grid_info()["row"] * 3 + button.grid_info()["column"]

        if self.board[index // 3][index % 3].cget("text") == " ":
            self.board[index // 3][index % 3].config(text=self.turn)
            self.check_winner()
            self.turn = "O" if self.turn == "X" else "X"

        if self.winner is not None:
            self.label.config(text="Winner: {}".format(self.winner))
            for button in self.buttons:
                button.config(state="disabled")

    def check_winner(self):
        for row in range(3):
            if self.board[row][0].cget("text") == self.board[row][1].cget("text") == self.board[row][2].cget("text") != " ":
                self.winner = self.board[row][0].cget("text")
                return

        for column in range(3):
            if self.board[0][column].cget("text") == self.board[1][column].cget("text") == self.board[2][column].cget("text") != " ":
                self.winner = self.board[0][column].cget("text")
                return

        if self.board[0][0].cget("text") == self.board[1][1].cget("text") == self.board[2][2].cget("text") != " ":
            self.winner = self.board[0][0].cget("text")
            return

        if self.board[2][0].cget("text") == self.board[1][1].cget("text") == self.board[0][2].cget("text") != " ":
            self.winner = self.board[2][0].cget("text")
            return

        if all([cell.cget("text") != " " for row in self.board for cell in row]):
            self.label.config(text="Tie!")
            for button in self.buttons:
                button.config(state="disabled")

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
