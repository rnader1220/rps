from Token import Token
from Player import Player


class Game:
    
    window = None

    def __init__(self, window, user_name):
        
        self.window = window

        self.tokens = [
            Token(keystroke = 'r', label = 'Rock', beats = 'Scissors', image = 'rock.gif'),
            Token(keystroke = 'p', label = 'Paper', beats = 'Rock', image = 'paper.gif'), 
            Token(keystroke = 's', label = 'Scissors', beats = 'Paper', image = 'scissors.gif')
        ]

        self.players = [
            Player(window = window, name = user_name, tokens = self.tokens, is_user = True), 
            Player(window = window, name = 'Computer', tokens = self.tokens, is_user = False)
        ]
    


    
        
    def play(self):
        for player in self.players:
            response = player.select(self.window)
            print(f" {player.name} selects {player.selection.label}")
            
        for player in self.players:
            for alt_player in self.players:
                if player == alt_player:
                    continue
                else:   
                    if player.test(alt_player.selection):
                        return player

    