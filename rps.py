from Game import Game

def main():
    print("Welcome to Mr. Nader's Rock, Paper, Scissors game!")
    user_name = input('Please enter your name:  ')
    game = Game(user_name)
    
    while True:
        winner = game.play()
        if winner is None:
            print ("its a tie!")
            continue
        
        print (f"winner: {winner.name}!")
        for player in game.players:
            print(f"{player.name}: {player.wins} wins!")
        if str(input('Shall we go again? (y):Yes  ')).lower() == "y":
            continue
        else:
            break
        
if "__main__":
    main()