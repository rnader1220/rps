import random

class Player:

    def __init__(self, window, tokens,  name,  is_user):
        self.tokens = tokens
        self.window = window
        self.name = name
        self.is_user = is_user
        self.wins = 0
        self.selection = None
        self.pikk = window.getVariable('string')
        self.widgets = {}
        
    def catchPick(self):
        picked = self.pikk.get()
        for token in self.tokens:
            if token.keystroke == picked:
                self.selection = token
                break
        for token in self.tokens:
            widget = self.widgets.pop(token.label)
            self.window.kill(widget)

    def select(self):
        self.pikk.set(None)
        if not self.is_user:
            self.selection = random.choice(self.tokens)
        else: 
            index = 0
            for token in self.tokens:
                self.window.addText("     ", row=3, col=index)
                self.widgets[token.label] = self.window.addRadio( \
                    caption=token.label, \
                    variable=self.pikk, \
                    value=token.keystroke, \
                    command=self.catchPick, \
                    row=4, col=index, \
                    image=token.image )

                index += 1

            self.window.wait(self.pikk)
        return True
    
    def test(self, token):
        if self.selection.test(token.label):
            self.wins += 1
            return True
        else:
            return False  
            
        
