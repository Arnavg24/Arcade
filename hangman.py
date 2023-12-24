import random



class Hangman:
   
    def __init__(self):

        self.wordlist = []
        random.seed(random.randint(1,100))

        self.word =  random.choice(open("words.txt").readlines()) 
        self.word=self.word.strip()
        self.length  = len(self.word)


        self.mock_word = "_ " * self.length 
        self.mock_word =  self.mock_word.split() 

        self.used_lets = []

        self.lives = 7

        self.who_won = self.play()

        

    def play(self):

        while True:
            print(" ".join(self.mock_word)) 
            let = input("Give a letter: ")

            if len(let) > 1: #User can only give one letter
                print ("Only one!")

            elif (let not in self.word):
                if let not in self.used_lets:
                    self.lives = self.lives - 1 
                    if self.lives == 0:
                        print ("Sorry you lost, the word was:", self.word)
                        return 2
                    print ("Try again, you have only %r lives left!" % self.lives )
                    self.used_lets.append(let)
                    print ("So far you have used:")
                    print (self.used_lets) 

            else:
                for i in range(self.length):
                    if let == self.word[i]:
                        self.mock_word[i] = let

            if "".join(self.mock_word) == self.word:
                print (self.word + " Player 1 won!")
                return 1
