import random

class Player:
    def __init__(this, name,  is_user):
        this.name = name
        this.is_user = is_user
        this.wins = 0
        
    def select(this, tokens):
        if this.is_user:
            while True:
                for token in tokens:
                    print(token.prompt)
                    
                response = input("select: ").lower()
                
                for token in tokens:
                    if token.keystroke == response:
                        this.selection = token
                        return
        else: 
            this.selection = random.choice(tokens)
            
    def test(this, token):
        if this.selection.test(token.label):
            this.wins += 1
            return True
        else:
            return False  
            
        
