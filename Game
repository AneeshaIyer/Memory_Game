import tkinter as tk
import random

class MemoryGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Memory Game")
        self.root.config(bg="white")
        self.cards = self.shuffle()
        self.revealed = [False] * (4 * 4)
        self.first = None
        self.second = None
        self.buttons = []
        self.create()

    def shuffle(self):
        icons = list(range(1, 8 + 1)) * 2
        random.shuffle(icons)
        return icons

    def create(self):
        for i in range(4 * 4):
            button = tk.Button(self.root, text="", width=8, height=3, command=lambda i=i: self.flip(i), font=("Lucida Bright", 20))
            button.grid(row=i // 4, column=i % 4)
            self.buttons.append(button)

    def flip(self, index):
        if self.revealed[index]:
            return
        self.revealed[index] = True
        self.buttons[index].config(text=str(self.cards[index]), state=tk.DISABLED, relief="sunken", bg="pink")
        if self.first is None:
            self.first = index
        elif self.second is None:
            self.second = index
            self.check_match()

    def check_match(self):
        if self.cards[self.first] == self.cards[self.second]:
            self.reset()
        else:
            self.root.after(500, self.hide)

    def hide(self):
        self.revealed[self.first] = False
        self.revealed[self.second] = False
        self.buttons[self.first].config(text="", state=tk.NORMAL, relief="raised", bg="white")
        self.buttons[self.second].config(text="", state=tk.NORMAL, relief="raised", bg="white")
        self.reset()

    def reset(self):
        self.first = None
        self.second = None
        if all(self.revealed):
            self.display_end()
            
    def display_end(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        game_over_label = tk.Label(self.root, text="Game Over! Congratulations!", font=("Lucida Bright",20,), fg="black", bg="white")
        game_over_label.grid(row=4, column=0, columnspan=4, pady=10)

    def run(self):
        self.root.mainloop()

game = MemoryGame()
game.run()
