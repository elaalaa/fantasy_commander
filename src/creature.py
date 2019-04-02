

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



    def __str__(self):
        return self.get_name() + ' at location ' + str(self.get_location())
