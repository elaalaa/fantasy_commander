

class Player():
    
    HUMAN = 0
    AI = 1
    
    def __init__(self, side):
        self.team = []
        self.side = side
        self.moving = False
        self.attacking = False
        
    def add_teammember(self, creature):
        self.team.append(creature)
    
    def play_turn(self):
        # 1. choose creature to move
        self.moving = True
        # print a message that it's your turn
        
        
        # choose tile to move to
        
        self.moving = False
        # update position
        
        self.attacking = True
        
        # choose creature to attack with
        
        # update effects
        self.attacking = False
        
    
    def is_moving(self):
        return self.moving
    
    def is_attacking(self):
        return self.attacking
    
    '''def set_moving(self):
        self.moving = True
        
    def set_attacking(self):
        self.attacking = True'''
        
        