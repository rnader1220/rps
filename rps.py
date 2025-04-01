

import tkinter as tk

from Game import Game


def play():
    user_name = name_entry.get()
    name_label.destroy()
    name_entry.destroy()
    sub_button.destroy()
    game = Game(root, user_name)
    while True:
        winner = game.play()
        if winner is None:
            print ("its a tie!")
            continue
        print (f"winner: {winner.name}!")
        for player in game.players:
            print(f"{player.name}: {player.wins} wins!")
        print('Shall we go again? (y):Yes  ')
        if str(input()).lower() == "y":
            continue
        else:
            break

root = tk.Tk()
root.geometry("600x200")
root.title("Mr. Nader RPS")

name_entry = tk.StringVar()
welcome_label = tk.Label(root, text="Welcome to Mr. Nader's Rock, Paper, Scissors game!")
welcome_label.grid(column=0, row=0, columnspan=3, padx=20, pady=10)
name_label = tk.Label(root, text="Enter your name:  ")
name_label.grid(column=0, row=3, padx=20, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(column=1, row=3, padx=20, pady=10)
sub_button = tk.Button(root, text="Lets Play!", command=play)
sub_button.grid(column=2, row=3, padx=20, pady=10)

root.mainloop()

 