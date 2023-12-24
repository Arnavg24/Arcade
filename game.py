import connect4
import hangman

class Game:
    
    def __init__(self):
        self.player1 = 0
        self.player2 = 0

        while True:
            print("Welcome to Our Gaming Parlour")
            print("Would you like to play?")
            print("1. Hangman")
            print("2. Connect-4")
            print("3. Exit")
            game_choice = input("Enter Game Choice : ")

            if game_choice == "":
                print("No input, exiting.....")
                break

            if game_choice == "1":
                print("Which player wants to play Hangman?")
                print("1. Player 1")
                print("2. Player 2")
                player_choice = input("Enter Player Choice (1/2): ")

                if player_choice == "1":
                    h = hangman.Hangman()
                    if h.who_won == 1:
                        self.player1 += 1
                    else:
                        self.player2 += 1

                elif player_choice == "2":
                    h = hangman.Hangman()
                    if h.who_won == 1:
                        self.player2 += 1
                    else:
                        self.player1 += 1
                else:
                    print("Wrong Input.")

            elif game_choice == "2":
                c=connect4.Connect4()
                if(c.who_won==1):
                    self.player1+=1
                else:
                    self.player2+=1

            elif game_choice == "3":
                print("Exiting the Game.")
                break

            else:
                print("Wrong Input for Game Choice.")

            print(f"Player 1 has {self.player1} points")
            print(f"Player 2 has {self.player2} points")
            print()

g = Game()
