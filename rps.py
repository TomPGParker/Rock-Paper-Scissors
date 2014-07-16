import random

class Agent:
    firstCheck = {}
    secondCheck = {}
    previousMoves = {}

    response = {"rock":"paper", "paper":"scissors", "scissors":"rock"}
    
    def __init__(self):
        #Creating random previous moves isn't perfect but the effect is negligable  
        self.previousMoves[0] = random.choice(["rock", "paper", "scissors"])
        self.previousMoves[1] = random.choice(["rock", "paper", "scissors"])

        self.firstCheck["rock"] = []
        self.firstCheck["paper"] = []
        self.firstCheck["scissors"] = []
        
        self.secondCheck["rock"] = {"rock":[], "scissors":[], "paper":[]}
        self.secondCheck["paper"] = {"rock":[], "scissors":[], "paper":[]}
        self.secondCheck["scissors"] = {"rock":[], "scissors":[], "paper":[]}

    def addMove(self, move):
        self.firstCheck[self.previousMoves[1]].append(move)
        self.secondCheck[self.previousMoves[0]][self.previousMoves[1]].append(move)
        self.previousMoves[0] = self.previousMoves[1]
        self.previousMoves[1] = move
        return self.secondCheck

    def makeMove(self):
        #If this sequence of moves hasn't been made before a random move will be made
        highest = random.choice(["rock", "paper", "scissors"])

        #First I'll check see if there's a highest 1 gauge response
        data = self.firstCheck[self.previousMoves[1]]
        for i in {"rock", "paper", "scissors"}:
            if (data.count(i) > data.count(highest)):
                highest = i
        #Now if there isn't a second gague response at least we'll get an approximation

        #this line doesn't need to exist but it makes the code neater
        data = self.secondCheck[self.previousMoves[0]][self.previousMoves[1]]

        #check which move has been played the most in the past from this sequence
        for i in {"rock", "paper", "scissors"}:
            if (data.count(i) > data.count(highest)):
                highest = i
                
        return self.response[highest]

    
    def runTest(self, n):
        wins = 0
        losses = 0
        results = [];
        
        for i in xrange(n):
            print "Game:", i, "Wins:", wins, "Losses:", losses
            
            ownMove = self.makeMove()
            print "I played:", ownMove
            otherMove = raw_input("Enter move: ")
            

            quick = {"p":"paper", "r":"rock", "s":"scissors"}
            if otherMove in quick:
                otherMove = quick[otherMove]
            
            while otherMove not in ["rock", "paper", "scissors"]:
                otherMove = raw_input("Please enter move again: ")
                if otherMove in quick:
                    otherMove = quick[otherMove]

            self.addMove(otherMove)
            
            if (self.response[otherMove] == ownMove):
                wins += 1
                print "I win!"
            elif (self.response[ownMove] == otherMove):
                  losses += 1
                  print "Aww, you win!"
            else:
                print "A draw! Lets try again."

            results.append((wins, losses))
        print "Wins:", wins
        print "Losses:", losses
        print results
        
        

#Testing
one = Agent()


one.runTest(50)
