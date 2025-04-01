from Token import Token
from Player import Player


class Game:
    
    def __init__(self, user_name) :
        self.players = [
            Player(name = user_name, is_user = True), 
            Player(name = 'Computer', is_user = False)
        ]
    
        self.tokens = [
            Token(keystroke = 'r', label = 'Rock', beats = 'Scissors', image = 'rock.png'),
            Token(keystroke = 'p', label = 'Paper', beats = 'Rock', image = 'paper.png'), 
            Token(keystroke = 's', label = 'Scissors', beats = 'Paper', image = 'scissors.png')
        ]
        
    def play(self):
        for player in self.players:
            player.select(self.tokens)
            print(f" {player.name} selects {player.selection.label}")
            
        for player in self.players:
            for alt_player in self.players:
                if player == alt_player:
                    continue
                else:
                    if player.test(alt_player.selection):
                        return player
