

class Player():
    
    HUMAN = 0
    AI = 1
    
    def __init__(self, side):
        self.team = []
        self.side = side
        
    def add_teammember(self, creature):
        self.team.append(creature)

    

        
        