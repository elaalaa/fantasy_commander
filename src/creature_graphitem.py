from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPointF, QPixmap, QGraphicsPixmapItem
from PyQt5.QtGui import QColor, QBrush
from creature import Creature

class Creature_graphitem(QGraphicsPixmapItem):
   

    def __init__(self, creature, tile_size, callback):
        # Call init of the parent object
        super(Creature_graphitem, self).__init__()

        # Do other stuff
        self.creature = creature
        self.tile_size = tile_size
        #brush = QtGui.QBrush(1) # 1 for even fill
        #self.setBrush(brush)
        self.set_sprite()
        self.updateAll()
        self.callback = callback

    def set_sprite(self):
        
        if self.creature.type == Creature.TANK:
            self.setPixmap(QPixmap('graphics/tank2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.MAGE:
            self.setPixmap(QPixmap('graphics/mage2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.NINJA:
            self.setPixmap(QPixmap('graphics/ninja2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.SNIPER:
            self.setPixmap(QPixmap('graphics/sniper2.png').scaled(self.tile_size, self.tile_size))
        self.setOffset(self.creature.get_location().get_x() , self.creature.get_location().get_y())
        

    def updateAll(self):
        
        self.updatePosition()

    def updatePosition(self):
        
        self.setPos(QPointF(self.creature.get_location().get_x()*self.tile_size, (self.creature.get_location().get_y())*self.tile_size))
        


    def update_sprite(self): # modify tiles to free if trees burn
        
        if self.robot.is_broken():
            self.setBrush(QBrush(QColor(255,0,0)))
        elif self.robot.is_stuck():
            self.setBrush(QBrush(QColor(255,255,0)))
        else:
            self.setBrush(QBrush(QColor(0,255,0)))

    def mousePressEvent(self, event): # set creature active if it's players turn
        self.creature.set_moving(self.creature.player.is_moving())
        self.creature.set_attacking(self.creature.player.is_attacking())
        
            
        
