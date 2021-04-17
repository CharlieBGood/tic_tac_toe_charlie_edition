#Defines a player with a name, a score and a path to its image
class Player:
    
    def __init__(self):
        self.name = ''
        self.score = 0
        self.imgPath = ''
    
    #Adds a win to a player
    def addWin(self):
        self.score += 1
    
    #Changes a player name    
    def setName(self, name):
        self.name = name
    
    #Changes the path to the image of the player    
    def setImgPath(self, path):
        self.imgPath = path
        
 
 #Defines a session with two players, a turn, a winner, a draw result, an XO state and a board       
class Session:
    
    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.turn = self.playerOne
        self.winner = None
        self.draw = False
        self.XO = 'x'
        self.board = [[None]*3, [None]*3, [None]*3]
    
    #Sets the winner of the game    
    def setWinner(self, player):
        if player == None:
            self.winner == None
        else:
            self.winner = player
    
    #Sets the draw state    
    def setDraw(self):
        self.Draw = True
    
    #Changes the player turn
    def nextTurn(self):
        if self.turn == self.playerOne:
            self.turn = self.playerTwo
        else:
            self.turn = self.playerOne

    #Resets the board 
    def resetBoard(self):
        self.board = [[None]*3, [None]*3, [None]*3]