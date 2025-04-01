import random
import tkinter as tk

class Player:


    def __init__(self, window, tokens,  name,  is_user):
        self.tokens = tokens
        self.window = window
        self.name = name
        self.is_user = is_user
        self.wins = 0
        self.selection = None
        self.pikk = tk.IntVar()
        self.pikk.set(None)
        
    def pick(self):
        picked = self.pikk.get()
        self.selection = self.tokens[picked]
        print(self.selection.label)
        return


    def select(self, window):
        if not self.is_user:
            self.pikk = random.choice(self.tokens)
        else: 
            icon = []
            for i in range(len(self.tokens)):
                icon.append(tk.PhotoImage(file=self.tokens[i].image))
                tk.Radiobutton( \
                    window, \
                    variable=self.pikk, \
                    value=i, \
                    text=self.tokens[i].label, \
                    image= icon[i], \
                    compound='top', \
                    command=self.pick \
                ).grid(column=i, row=3, padx=20, pady=10)

            window.mainloop()

            
    def test(self, token):
        if self.selection.test(token.label):
            self.wins += 1
            return True
        else:
            return False  
            
        
