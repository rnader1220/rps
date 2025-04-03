from Token import Token
from Player import Player
from Window import Window

class Game:
    
    # main game flows here.
    def __init__(self):
        self.widgets = {}
        self.window = Window()
        self.tokens = [
            Token(keystroke = 'r', label = 'Rock', beats = 'Scissors', image = 'rock.gif'),
            Token(keystroke = 'p', label = 'Paper', beats = 'Rock', image = 'paper.gif'), 
            Token(keystroke = 's', label = 'Scissors', beats = 'Paper', image = 'scissors.gif')
        ]

        self.players = [
            Player(window = self.window, name = 'Player', tokens = self.tokens, is_user = True), 
            Player(window = self.window, name = 'Computer', tokens = self.tokens, is_user = False)
        ]
        self.welcome()
        self.getPlayer()
        self.window.window.mainloop()

    def replay(self):
        for player in self.players:
            self.window.kill(self.widgets.pop(player.name + '_name'))
            self.window.kill(self.widgets.pop(player.name + '_icon'))

        self.window.kill(self.widgets.pop('winner_name'))
        self.window.kill(self.widgets.pop('winner_icon'))

        self.window.kill(self.widgets.pop('play_again'))
        self.window.kill(self.widgets.pop('go_home'))

        self.letsPlay()

    def bowout(self):
        try :
            self.window.kill(self.widgets.pop('play_again'))
            self.window.kill(self.widgets.pop('go_home'))
            self.window.close()
        except :
            quit()

    def catchPlayer(self):
        self.players[0].name = self.playerName.get()
        self.window.kill(self.widgets.pop('name_label'))
        self.window.kill(self.widgets.pop('name_input'))
        self.window.kill(self.widgets.pop('name_button'))
        self.window.addText("Welcome, "+self.players[0].name , row=1, col=0, width=5)
        self.letsPlay()

    def welcome(self) :
        self.window.addText("Welcome to Mr. Nader's Rock, Paper, Scissors game!", row=0, col=0, width=5)
        
    def getPlayer(self) : 
        self.playerName = self.window.getVariable('string')
        self.widgets['name_label'] = self.window.addLabel("Enter Your Name:", row=1, col=0)
        self.widgets['name_input'] = self.window.addTextInput(self.playerName, row=1, col=1)
        self.widgets['name_button'] = self.window.addSubmit("Lets Play", command=self.catchPlayer, row=1, col=2, width=1)
        self.window.wait(self.players[0].name)

    def letsPlay(self) :
        for player in self.players:
            player.select()

        index = 0
        for player in self.players:
            self.widgets[player.name + '_name'] = self.window.addText(player.name, row=3, col=index)
            self.widgets[player.name + '_icon'] = self.window.addImage(player.selection.image, caption=player.selection.label, row=4, col=index)
            index += 1

        winner = self.testWin()
        if(winner) :
            self.widgets['winner_name'] = self.window.addText(winner.name+' Wins!', row=3, col=index)
            self.widgets['winner_icon'] = self.window.addImage(winner.selection.image, caption=winner.selection.label, row=4, col=index)
        else :
            self.widgets['winner_name'] = self.window.addText("It's a Tie!", row=3, col=index)
            self.widgets['winner_icon'] = self.window.addImage(self.players[0].selection.image, caption=self.players[0].selection.label, row=4, col=index)

        self.widgets['play_again'] = self.window.addSubmit("Go Again", command=self.replay, row=5, col=0, width=2)
        self.widgets['go_home'] = self.window.addSubmit("Go Home", command=self.window.window.destroy, row=5, col=2, width=2)

    def testWin(self) :
        for player in self.players:
            for alt_player in self.players:
                if player == alt_player:
                    continue
                else:
                    if player.test(alt_player.selection):
                        return player
        return False