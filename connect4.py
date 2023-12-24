class Connect4:

    def __init__(self):

        self.board = [] 
        self.label = []
        self.whos_turn = 2
        self.winner = False
        self.last = 0
        self.column = 0
        self.boardheight = 6
        self.boardwidth = 7
        
        self.who_won=self.play()
    


    def play(self):
        print("Let's play Connect Four!")
        self.generate_board()
        self.print_board()
        while self.winner == False:
            self.whos_turn = 1 if self.whos_turn==2 else 2
            print(f"Player {self.whos_turn}'s turn")
        
            self.play_turn()
            self.winner = self.check_winner(str(self.whos_turn))
            
        if self.winner == True:
            print ("Player " + str(self.whos_turn) + " wins!")
            if(str(self.whos_turn)=='1'):
                return 1
            else:
                return 2



    #generate empty self.board
    def generate_board(self):
        for i in range(8):
            if i < self.boardheight:
                self.board.append(["_"] * self.boardwidth)
            elif i < self.boardwidth:
                self.board.append(["^"] * self.boardwidth)
            else:
                for j in range(self.boardwidth):
                    self.label.append(str(j+1))
                self.board.append(self.label)


    def print_board(self):
        print()
        for row in self.board:
            print(" ".join(row))
        print()
            


    def mark_board(self):
        if self.whos_turn == 1:
            self.board[self.last][self.column] = "1"
        else:
            self.board[self.last][self.column] = "2"
        self.print_board()

    def play_turn(self):
        while True:
            try:
                self.column = int(input("Pick a self.column (1-7): ")) - 1
                if self.column >= 0 and self.column <= self.boardwidth:
                    for i in range(6):
                        if self.board[i][self.column] == "_":
                            self.last = i
                    self.mark_board()
                else:
                    raise "You picked a column outside the board!"
                break
            except:
                print("Not a valid number! Please try again...")

    def check_winner(self, player):
        #check vertical spaces
        for y in range(self.boardwidth):
            for x in range(self.boardheight - 3):
            
                if self.board[x][y] == player and self.board[x+1][y] == player and self.board[x+2][y] == player and self.board[x+3][y] == player:
                    return True

        #check horizontal spaces
        for x in range(self.boardheight):
            for y in range(self.boardwidth - 3):
                
                if self.board[x][y] == player and self.board[x][y+1] == player and self.board[x][y+2] == player and self.board[x][y+3] == player:
                    return True

        #check / diagonal spaces
        for x in range(self.boardheight - 3):
            for y in range(3, self.boardwidth):
                if self.board[x][y] == player and self.board[x+1][y-1] == player and self.board[x+2][y-2] == player and self.board[x+3][y-3] == player:
                    return True

        #check \ diagonal spaces
        for x in range(self.boardheight - 3):
            for y in range(self.boardwidth - 3):
                if self.board[x][y] == player and self.board[x+1][y+1] == player and self.board[x+2][y+2] == player and self.board[x+3][y+3] == player:
                    return True

        return False
        
