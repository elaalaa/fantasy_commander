import sys
from PyQt5.QtWidgets import QApplication

from GUI import Gamewindow

from map import * # use tile somewhere?
from location import *
from creature import *
from player import *

class Game():
    
    def __init__(self, human, ai, map):
        self.human = human # human goes always first
        self.ai = ai
        self.map = map
        
    def full_turn(self):
        self.human.play_turn()
        self.ai.play_turn()
        

def main():
    
    test_map = Map(10, 8)
    '''wall1_coordinates = Coordinates(2, 4)
    test_world.add_wall(wall1_coordinates)
    wall2_coordinates = Coordinates(0, 5)
    test_world.add_wall(wall2_coordinates)'''

    tank_location = Location(0, 0)
    tank_body = Creature('Tank1', Creature.TANK, Player.HUMAN)
    test_map.add_creature(tank_body, tank_location)

    mage_location = Location(0, 1)
    mage_body = Creature('Mage1', Creature.MAGE, Player.HUMAN)
    test_map.add_creature(mage_body, mage_location)

    ninja_location = Location(0, 2)
    ninja_body = Creature('Ninja1', Creature.NINJA, Player.HUMAN)
    test_map.add_creature(ninja_body, ninja_location)

    sniper_location = Location(0, 3)
    sniper_body = Creature('Sniper1', Creature.SNIPER, Player.HUMAN)
    test_map.add_creature(sniper_body, sniper_location)

    # Every Qt application must have one instance of QApplication.
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = Gamewindow(test_map, 50)

    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec_())

    # Any code below this point will only be executed after the gui is closed.

if __name__ == '__main__':
    main()
