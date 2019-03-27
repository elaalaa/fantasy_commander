import sys
from PyQt5.QtWidgets import QApplication

from GUI import Gamewindow

from map import * # use tile somewhere?
from location import *
from creature import *


def main():
    '''
    Creates a RobotWorld, adds robots and launches the Graphical User Interface.

    Use this for testing your code.

    You can modify this however you like.
    '''
    test_map = Map(10, 8)
    '''wall1_coordinates = Coordinates(2, 4)
    test_world.add_wall(wall1_coordinates)
    wall2_coordinates = Coordinates(0, 5)
    test_world.add_wall(wall2_coordinates)'''

    nose_location = Location(9, 7)
    nose_body = Creature('Nose')
    #nose_brain = Nosebot(nose_body)
    #nose_body.set_brain(nose_brain)
    test_map.add_creature(nose_body, nose_location)

    spin_location = Location(2, 3)
    spin_body = Creature('Spin')
    #spin_brain = Spinbot(spin_body)
    #spin_body.set_brain(spin_brain)
    test_map.add_creature(spin_body, spin_location)

    love_location = Location(8, 5)
    love_body = Creature('Love')
    #love_brain = Lovebot(love_body, spin_body)
    #love_body.set_brain(love_brain)
    test_map.add_creature(love_body, love_location)

    drunk_location = Location(5, 5)
    drunk_body = Creature('Drunk')
    #seed = 2
    #drunk_brain = Drunkbot(drunk_body, seed)
    #drunk_body.set_brain(drunk_brain)
    test_map.add_creature(drunk_body, drunk_location)

    # Every Qt application must have one instance of QApplication.
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = Gamewindow(test_map, 50)

    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec_())

    # Any code below this point will only be executed after the gui is closed.

if __name__ == '__main__':
    main()
