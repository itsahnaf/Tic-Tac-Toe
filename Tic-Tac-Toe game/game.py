import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x400")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        self.create_board()
    
    def create_board(self):
        # Set the background color for the window
        self.root.config(bg="#d3d3d3")
        
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 24, "bold"), height=2, width=5,
                            command=lambda i=i: self.make_move(i), relief="solid", bd=2)
            # Color based on index for visual differentiation
            if i % 2 == 0:
                btn.config(bg="#f0f8ff")  # Light blue for even indexed buttons
            else:
                btn.config(bg="#fafad2")  # Light yellow for odd indexed buttons
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
    
    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, disabledforeground="#FFFFFF")
            
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a Tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for (x, y, z) in winning_combinations:
            if self.board[x] == self.board[y] == self.board[z] and self.board[x] != "":
                self.highlight_winner(x, y, z)
                return self.board[x]
        return None

    def highlight_winner(self, x, y, z):
        self.buttons[x].config(bg="#98fb98")  # Light green for winning buttons
        self.buttons[y].config(bg="#98fb98")
        self.buttons[z].config(bg="#98fb98")
    
    def reset_board(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", bg="#f0f8ff")  # Reset to default colors
            button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
