from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QGraphicsRectItem, QGraphicsPixmapItem, QPixmap
from PyQt5.QtGui import QColor, QBrush

from location import Location
from tile import Tile
from creature_graphitem import Creature_graphitem
from tile_graphitem import Tile_graphitem



class Gamewindow(QtWidgets.QMainWindow):
    
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

        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_objects)
        self.timer.start(10) # Milliseconds


    def add_tile_graphitems(self):
        
        for x in range(0, self.game.get_width()):
            for y in range(0, self.game.get_height()):
                tile = self.game.get_tile(Location(x, y))
                if tile.get_type() == Tile.FREE:
                    item = Tile_graphitem(tile, self.tile_size, x, y, self.tile_click_callback)
                    self.scene.addItem(item)
                elif tile.get_type() == Tile.TREE:
                    item = Tile_graphitem(tile, self.tile_size, x, y, self.tile_click_callback)
                    self.scene.addItem(item)
                else:
                    item = Tile_graphitem(tile, self.tile_size, x, y, self.tile_click_callback)
                    self.scene.addItem(item)

    def get_gameobjects(self):
        return self.gameobjects


    def add_creature_graphitems(self):
        
        for creature in self.game.get_creatures():
            if creature not in self.get_gameobjects():
                item = Creature_graphitem(creature, self.tile_size, self.creature_click_callback)
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
        
    def tile_click_callback(self, event, location):
        # do stuff
        pass
    
    def creature_click_callback(self, creature):
        # do stuff
        pass
