import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Board state
board = [' ' for _ in range(9)]

# Functions
def check_winner(player):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_cond:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw():
    return ' ' not in board

def computer_move():
    empty = [i for i, x in enumerate(board) if x == ' ']
    if empty:
        move = random.choice(empty)
        board[move] = 'O'
        buttons[move].config(text='O')
        if check_winner('O'):
            messagebox.showinfo("Game Over", "Computer wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()

def player_move(i):
    if board[i] == ' ':
        board[i] = 'X'
        buttons[i].config(text='X')
        if check_winner('X'):
            messagebox.showinfo("Game Over", "You won!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            computer_move()

def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ')

# Create buttons
buttons = []
for i in range(9):
    b = tk.Button(root, text=' ', font=('Arial', 40), width=5, height=2,
                  command=lambda i=i: player_move(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

# Run the GUI
root.mainloop()
