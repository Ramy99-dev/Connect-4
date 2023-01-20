class Player():
    
    def __init__(self):
        self.currentPlayer = 1
    
    def switchPlayer(self):
        if(self.currentPlayer == 1):
            self.currentPlayer = 2
        else:
            self.currentPlayer = 1
    
    def getCurrentPlayer(self):
        return self.currentPlayer