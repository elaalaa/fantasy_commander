from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QGraphicsRectItem
from PyQt5.QtGui import QColor, QBrush

from location import Location
from tile import Tile
from creature_graphitem import Creature_graphitem



class Gamewindow(QtWidgets.QMainWindow):
    '''
    The class GUI handles the drawing of a RobotWorld and allows user to
    interact with it.
    '''
    def __init__(self, game, tile_size):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout() # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.game = game
        self.tile_size = tile_size
        self.gameobjects = []
        self.init_window()
        self.init_buttons()
        #self.init_textbox()

        self.add_tile_graphitems()
        self.add_creature_graphitems()
        self.update_objects()
        
        #self.scene = scene

        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_objects)
        self.timer.start(10) # Milliseconds


    def add_tile_graphitems(self):
        
        rock = QBrush(QColor(20,20,20))
        free = QBrush(QColor(211,211,211))
        tree = QBrush(QColor(34,139,34))
        
        for x in range(0, self.game.get_width()):
            for y in range(0, self.game.get_height()):
                if self.game.get_tile(Location(x, y)).get_type() == Tile.FREE:
                    item = QGraphicsRectItem(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    item.setBrush(free)
                    self.scene.addItem(item)
                elif self.game.get_tile(Location(x, y)).get_type() == Tile.TREE:
                    item = QGraphicsRectItem(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    item.setBrush(tree)
                    self.scene.addItem(item)
                else:
                    item = QGraphicsRectItem(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                    item.setBrush(rock)
                    self.scene.addItem(item)

    def get_gameobjects(self):
        return self.gameobjects


    def add_creature_graphitems(self):
        
        # Calls your code in gui_exercise.py
        for creature in self.game.get_creatures():
            if creature not in self.get_gameobjects():
                item = Creature_graphitem(creature, self.tile_size)
                self.scene.addItem(item)
                self.gameobjects.append(item)


    def init_buttons(self):
        '''
        Adds buttons to the window and connects them to their respective functions
        See: QPushButton at http://doc.qt.io/qt-5/qpushbutton.html
        '''
        pass
        '''self.next_turn_btn = QtWidgets.QPushButton("Next full turn")
        self.next_turn_btn.clicked.connect(self.world.next_full_turn)
        self.horizontal.addWidget(self.next_turn_btn)'''

    def update_objects(self):
        '''
        Iterates over all robot items and updates their position to match
        their physical representations in the robot world.
        '''
        for item in self.get_gameobjects():
            item.updateAll()

    def init_window(self):
        '''
        Sets up the window.
        '''
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Gamewindow')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
