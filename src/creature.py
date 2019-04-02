

class Creature():
    TANK = 0
    MAGE = 1
    NINJA = 2
    SNIPER = 3

    def __init__(self, name, type, player, location):
        
        self.set_name(name)
        self.map = None
        self.location = location     # most-recent location
        self.destroyed = False   # flag if character is destroyed
        self.set_type(type)      # creature type, defines movement and attack
        self.player = player
        self.moving = False
        self.attacking = False
        self.set_hp()

    
    def set_hp(self):
        if self.type == Creature.TANK:
            self.hp = 30
        elif self.type == Creature.MAGE:
            self.hp = 10
        elif self.type == Creature.NINJA:
            self.hp = 20
        elif self.type == Creature.SNIPER:
            self.hp = 10
            
    def get_hp(self):
        return self.hp
        
    
    def set_name(self, name):
        
        if not name:
            self.name = "Incognito"
        else:
            self.name = name


    def get_name(self):
        
        return self.name
    
    def is_moving(self):
        return self.moving
    
    def set_moving(self):
        self.moving = True
        
    
    def is_attacking(self):
        return self.attacking
    
    def set_attacking(self):
        self.attacking = True

    def set_type(self, type):
        
        self.type = type


    def get_type(self):
        
        return self.type


    def get_map(self):
        
        return self.map


    def get_location(self):
        
        return self.location


    def get_tile(self):
        
        return self.get_map().get_tile(self.get_location())



    def destroy(self):
        
        self.destroyed = True



    def is_dead(self):
        
        return self.destroyed



    def set_map(self, map, location):
        
        target_tile = map.get_tile(location)
        if not target_tile.is_empty() or self.get_map() is not None:
            return False
        else:
            self.map = map
            self.location = location
            return True
        
    def attack(self, location):
        pass


    '''def move(self, direction): # ei tarvita jos tehdaan mousepressilla?
        
        if self.is_broken():
            return False

        target = self.get_location().get_neighbor(direction)
        current_square = self.get_location_square()
        target_square = self.get_world().get_square(target)
        self.spin(direction)
        if target_square.is_empty():
            current_square.remove_robot()
            self.location = target
            target_square.set_robot(self)
            return True
        elif target_square.get_robot() is not None:
            target_square.get_robot().destroy()
            return False
        else:   # collided with wall
            self.destroy()
            return False'''



    '''def take_turn(self): # ehka tarvitaan, pitaa kattoo rakenne
        
        if not self.is_stuck() and not self.is_broken():
            self.brain.move_body()'''

    def __str__(self):
        return self.get_name() + ' at location ' + str(self.get_location())
