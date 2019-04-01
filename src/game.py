import sys
from PyQt5.QtWidgets import QApplication

from GUI import Gamewindow

from map import *
from location import *
from creature import *
from player import *
from GUI import *

# Qtextbrowser

class Game():
    
    def __init__(self, human, ai, map, gui):
        self.human = human # human goes always first
        self.ai = ai
        self.map = map
        self.gui = gui
        
    def full_turn(self):
        self.console.append("Player 1, your turn.")
        self.human.play_turn()
        
        self.console.append("Player 2, your turn.")
        self.ai.play_turn()
        


def main():
    
    test_map = Map('maps/map2.txt')

    tank_location = Location(0, 0)
    tank_body = Creature('Tank1', Creature.TANK, Player.HUMAN, tank_location)
    test_map.add_creature(tank_body, tank_location)

    mage_location = Location(0, 1)
    mage_body = Creature('Mage1', Creature.MAGE, Player.HUMAN, mage_location)
    test_map.add_creature(mage_body, mage_location)

    ninja_location = Location(0, 2)
    ninja_body = Creature('Ninja1', Creature.NINJA, Player.HUMAN, ninja_location)
    test_map.add_creature(ninja_body, ninja_location)

    sniper_location = Location(0, 3)
    sniper_body = Creature('Sniper1', Creature.SNIPER, Player.HUMAN, sniper_location)
    test_map.add_creature(sniper_body, sniper_location)
    
    tank_location = Location(0, 4)
    tank_body = Creature('Tank2', Creature.TANK, Player.HUMAN, tank_location)
    test_map.add_creature(tank_body, tank_location)

    mage_location = Location(0, 5)
    mage_body = Creature('Mage2', Creature.MAGE, Player.HUMAN, mage_location)
    test_map.add_creature(mage_body, mage_location)

    ninja_location = Location(0, 6)
    ninja_body = Creature('Ninja2', Creature.NINJA, Player.HUMAN, ninja_location)
    test_map.add_creature(ninja_body, ninja_location)

    sniper_location = Location(0, 7)
    sniper_body = Creature('Sniper2', Creature.SNIPER, Player.HUMAN, sniper_location)
    test_map.add_creature(sniper_body, sniper_location)
    
    tank_location = Location(13, 0)
    tank_body = Creature('Tank1', Creature.TANK, Player.AI, tank_location)
    test_map.add_creature(tank_body, tank_location)

    mage_location = Location(13, 1)
    mage_body = Creature('Mage1', Creature.MAGE, Player.AI, mage_location)
    test_map.add_creature(mage_body, mage_location)

    ninja_location = Location(13, 2)
    ninja_body = Creature('Ninja1', Creature.NINJA, Player.AI, ninja_location)
    test_map.add_creature(ninja_body, ninja_location)

    sniper_location = Location(13, 3)
    sniper_body = Creature('Sniper1', Creature.SNIPER, Player.AI, sniper_location)
    test_map.add_creature(sniper_body, sniper_location)
    
    tank_location = Location(13, 4)
    tank_body = Creature('Tank2', Creature.TANK, Player.AI, tank_location)
    test_map.add_creature(tank_body, tank_location)

    mage_location = Location(13, 5)
    mage_body = Creature('Mage2', Creature.MAGE, Player.AI, mage_location)
    test_map.add_creature(mage_body, mage_location)

    ninja_location = Location(13, 6)
    ninja_body = Creature('Ninja2', Creature.NINJA, Player.AI, ninja_location)
    test_map.add_creature(ninja_body, ninja_location)

    sniper_location = Location(13, 7)
    sniper_body = Creature('Sniper2', Creature.SNIPER, Player.AI, sniper_location)
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
