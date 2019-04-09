from location import Location

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
        #self.set_hp()

    
            
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
    

    def __str__(self):
        return self.get_name() + ' at location ' + str(self.get_location())
    
    
class Tank(Creature):
       
    def __init__(self, name, player, location):
        super().__init__(name, Creature.TANK, player, location)
        self.hp = 30
    
    def movement_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 2, location.x + 3):
            for y in range(location.y - 2, location.y + 3):
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).is_empty():
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
    
    def attack_squares(self):
        pass
    
    def attack(self, location):
        pass
    
    
class Mage(Creature):
    
    def __init__(self, name, player, location):
        super().__init__(name, Creature.MAGE, player, location)
        self.hp = 10
    
    def movement_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 1, location.x + 2):
            for y in range(location.y - 1, location.y + 2):
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).is_empty():
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
    
    def attack_squares(self):
        pass
    
    def attack(self, location):
        pass
    
class Ninja(Creature):
    
    def __init__(self, name, player, location):
        super().__init__(name, Creature.NINJA, player, location)
        self.hp = 20
        
    def movement_squares(self):
        squares = []
        directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        location = self.location
        for direction in directions:
            step = 1
            while (1):
                next = Location(location.x + (direction[0] * step), location.y + (direction[1] * step))
                if self.map.contains(next):
                    if self.map.get_tile(next).is_empty():
                        squares.append(self.map.get_tile(next))
                    else:
                        break
                else:
                    break
                step = step + 1
        return squares
    
    def attack_squares(self):
        pass
    
    def attack(self, location):
        pass
    
    
class Sniper(Creature):
    
    def __init__(self, name, player, location):
        super().__init__(name, Creature.SNIPER, player, location)
        self.hp = 10
        
    def movement_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 1, location.x + 2):
            for y in range(location.y - 1, location.y + 2):
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).is_empty():
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
    
    def attack_squares(self):
        pass
    
    def attack(self, location):
        pass