

class Player():
    
    HUMAN = 0
    AI = 1
    
    def __init__(self, side, type):
        self.team = []
        self.side = side # player 1 or 2
        self.type = type
        
    def add_teammember(self, creature):
        self.team.append(creature)

    def ai_turn(self):
        # ai plays turn
        pass
    

        
        