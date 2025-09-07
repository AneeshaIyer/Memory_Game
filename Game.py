import tkinter as tk
import random

class MemoryGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Memory Game")
        self.root.config(bg="purple")
        self.rows, self.cols = 4,4
        self.setup()
        self.create()

    def setup(self):
        self.cards = self.shuffle()
        self.revealed = [False] * (self.rows * self.cols)
        self.first = None
        self.second = None
        self.lock = False
        self.moves = 0
        self.buttons = []

    def shuffle(self):
        emojis = ["🍕","🍔","🍟","🥐","🍞","🥩","🍪","🍩","🍭","🧃","🍸","🎂","🧁","🍚","🍜","🍿"]
        n_pairs = (self.rows * self.cols) // 2  
        chosen = random.sample(emojis, n_pairs) 
        icons = chosen * 2                      
        random.shuffle(icons)                  
        return icons

    def create(self):
        for i in range(self.rows * self.cols):
            button = tk.Button(self.root, text="", width=7, height=3, command=lambda i=i: self.flip(i), font=("Lucida Bright", 20), bg="lavender")
            button.grid(row=i // self.cols, column=i % self.cols, padx=3, pady=3)
            self.buttons.append(button)

        self.move = tk.Label(self.root, text="Moves: 0", font=("Lucida Bright", 16), bg="lavender")
        self.move.grid(row=self.rows, column=0, columnspan=self.cols, pady=10)

    def flip(self, index):
        if self.lock or self.revealed[index]:
            return

        self.buttons[index].config(text=str(self.cards[index]), state=tk.DISABLED, relief="sunken", bg="lightyellow")
        if self.first is None:
            self.first = index
        elif self.second is None:
            self.second = index
            self.moves += 1
            self.move.config(text=f"Moves: {self.moves}")
            self.check()

    def check(self):
        if self.cards[self.first] == self.cards[self.second]:
            self.revealed[self.first] = True
            self.revealed[self.second] = True
            self.buttons[self.first].config(bg="lightgreen")
            self.buttons[self.second].config(bg="lightgreen")
            self.reset()
        else:
            self.lock = True
            self.root.after(800, self.hide)

    def hide(self):
        self.buttons[self.first].config(text="", state=tk.NORMAL, relief="raised", bg="lavender")
        self.buttons[self.second].config(text="", state=tk.NORMAL, relief="raised", bg="lavender")
        self.lock = False
        self.reset()

    def reset(self):
        self.first = None
        self.second = None
        if all(self.revealed):
            self.display_end()
            
    def display_end(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        label = tk.Label(self.root, text=f"🎉 Game Over! You won in {self.moves} moves! 🎉", font=("Lucida Bright", 15), fg="black", bg="lavender")
        label.grid(row=self.rows+1, column=0, columnspan=self.cols, pady=10)

        restart = tk.Button(self.root, text="Play Again", command=self.restart, font=("Lucida Bright", 16), bg="white")
        restart.grid(row=self.rows+2, column=0, columnspan=self.cols, pady=10)

    def restart(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup()
        self.create()

    def run(self):
        self.root.mainloop()

game = MemoryGame()
game.run()
