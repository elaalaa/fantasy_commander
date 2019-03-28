from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QGraphicsRectItem, QGraphicsPixmapItem, QPixmap
from PyQt5.QtGui import QColor, QBrush
from tile import Tile

class Tile_graphitem(QGraphicsPixmapItem):
    
    rock = QBrush(QColor(20,20,20))
    free = QBrush(QColor(211,211,211))
    tree = QBrush(QColor(34,139,34))
    
    def __init__(self, tile, tile_size, x, y, callback):
        # Call init of the parent object
        super(Tile_graphitem, self).__init__()
        self.x = x
        self.y = y
        #x * tile_size, y * tile_size, tile_size, tile_size
        # Do other stuff
        self.callback = callback
        self.tile = tile
        self.tile_size = tile_size
        #brush = QtGui.QBrush(1) # 1 for even fill
        #self.setBrush(brush)
        self.set_sprite()
        #self.updateAll()
        
    def set_sprite(self):
        if self.tile.get_type() == Tile.FREE:
            #self.setBrush(Tile_graphitem.free)
            #item = QGraphicsPixmapItem(QPixmap('free_tile.png').scaled(self.tile_size, self.tile_size))
            self.setPixmap(QPixmap('graphics/free_tile.png').scaled(self.tile_size, self.tile_size))
            self.setOffset(self.x * self.tile_size, self.y * self.tile_size)
        elif self.tile.get_type() == Tile.TREE:
            self.setBrush(Tile_graphitem.tree)
        else:
            self.setBrush(Tile_graphitem.rock)
            
    def mousePressEvent(self, event): # move moving creature to tile
        click_type = event
        location = self.tile.get_location()
        self.callback(click_type, location)
        
        
        
        
    