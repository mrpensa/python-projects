import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
import random
import time 

def start_game(mode):
    global turn_machine
    global is_single_player
    is_single_player = (mode == 'single')
    turn_machine = is_single_player  
    reset_game()

def make_move(row, col):
    global current_player
    global turn_machine

    if game[row][col] == '':
        game[row][col] = current_player
        buttons[row][col].configure(text=current_player)
        
        if check_winner():
            return
        
        if current_player == "X":
            current_player = "O"
            turn_machine = is_single_player
            if is_single_player and turn_machine:
                root.after(1000, computer_move) 
        else:
            current_player = "X"
            turn_machine = False


def computer_move():
    global current_player
    global turn_machine

    turn_machine = False
    empty_spots = [(i, j) for i in range(3) for j in range(3) if game[i][j] == '']
    if empty_spots:
        row, col = random.choice(empty_spots)
        game[row][col] = current_player
        buttons[row][col].configure(text=current_player)
        if not check_winner():
            current_player = "O" if current_player == "X" else "X"

def check_winner():
    winning_combinations = (
        game[0], game[1], game[2],
        [game[i][0] for i in range(3)],
        [game[i][1] for i in range(3)],
        [game[i][2] for i in range(3)],
        [game[i][i] for i in range(3)],
        [game[i][2 - i] for i in range(3)]
    )

    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] != '':
            announce_winner(combination[0])
            return True

    if all(game[i][j] != '' for i in range(3) for j in range(3)):
        announce_winner("Draw")
        return True

    return False

def announce_winner(player):
    if player == "Draw":
        message = "It's a draw!"
    else:
        message = f"Player {player} wins!"
    messagebox.showinfo("Game Over", message)
    reset_game()

def reset_game():
    global game, current_player, turn_machine
    game = [['', '', ''] for _ in range(3)]
    current_player = "X"
    turn_machine = is_single_player 
    for row in buttons:
        for button in row:
            button.configure(text='')

def show_mode_selection():
    answer = messagebox.askquestion("Select Mode", "Do you want to play Single?")
    if answer == 'yes':
        start_game('single')
    else:
        start_game('two')

root = tk.Tk()
root.title("Tic-Tac-Toe")
style = Style(theme="flatly")

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text='', width=10, height=5, font=('Helvetica', 24),
                            command=lambda i=i, j=j: make_move(i, j))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    buttons.append(row)

game = [['', '', ''] for _ in range(3)]
current_player = "X"
is_single_player = False
turn_machine = False

show_mode_selection()

root.mainloop()
