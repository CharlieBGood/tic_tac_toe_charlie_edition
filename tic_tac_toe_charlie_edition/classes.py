class Player:
    
    def __init__(self):
        self.name = ''
        self.score = 0
    
    def addWin(self):
        self.score += 1
        
    def setName(self, name):
        self.name = name
        
        
class Session:
    
    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.turn = self.playerOne
        self.winner = None
        self.draw = False
        self.XO = 'x'
        self.board = [[None]*3, [None]*3, [None]*3]
        
    def setWinner(self, player):
        if player == None:
            self.winner == None
        else:
            self.winner = player
        
    def setDraw(self):
        self.Draw = True
    
    def nextTurn(self):
        if self.turn == self.playerOne:
            self.turn = self.playerTwo
        else:
            self.turn = self.playerOne

    def resetBoard(self):
        self.board = [[None]*3, [None]*3, [None]*3]