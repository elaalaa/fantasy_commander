

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
    
    def move(self):
        if self.side == Player.HUMAN:
            self.moving = True
        
    def attack(self):
        if self.side == Player.HUMAN:
            self.attacking = True
            
    
    def is_moving(self):
        return self.moving
    
    def is_attacking(self):
        return self.attacking
    
    '''def set_moving(self):
        self.moving = True
        
    def set_attacking(self):
        self.attacking = True'''
        
        