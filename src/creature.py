

class Creature():
    

    def __init__(self, name):
        
        self.set_name(name)
        self.map = None        # fixed value
        self.location = None     # most-recent holder
        self.destroyed = False   # flag
        self.brain = None       #brain varmaan mika tyyppi se on? tai miten liikkuu?


    def set_name(self, name):
        
        if not name:
            self.name = "Incognito"   # most-recent holder
        else:
            self.name = name


    def get_name(self):
        
        return self.name


    def set_brain(self, new_brain):
        
        self.brain = new_brain # tata ei valttamatta tarvi?


    def get_brain(self):
        
        return self.brain # taa olis tyyppi


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


    def move(self, direction): # ei tarvita jos tehdaan mousepressilla?
        
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
            return False


    def move_forward(self): # ei tarvita
        
        return self.move(self.get_facing())


    def take_turn(self): # ehka tarvitaan, pit‰‰ kattoo rakenne
        
        if not self.is_stuck() and not self.is_broken():
            self.brain.move_body()

    def __str__(self):
        return self.get_name() + ' at location ' + str(self.get_location())
