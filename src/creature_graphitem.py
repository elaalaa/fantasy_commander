from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPointF, QPixmap, QGraphicsPixmapItem, QLabel
from PyQt5.QtGui import QColor, QBrush
from creature import Creature
from player import Player

class Creature_graphitem(QGraphicsPixmapItem):
   

    def __init__(self, creature, tile_size, callback):
        # Call init of the parent object
        super(Creature_graphitem, self).__init__()

        self.creature = creature
        self.tile_size = tile_size
        
        self.setToolTip("Name: {}\nHP: {}".format(self.creature.get_name(), self.creature.get_hp()))
        
        self.set_sprite()
        self.updateAll()
        self.callback = callback
        
    

    def set_sprite(self):
        
        if self.creature.type == Creature.TANK:
            if self.creature.player == Player.HUMAN:
                self.setPixmap(QPixmap('graphics/tank2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/tank2_p2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.MAGE:
            if self.creature.player == Player.HUMAN:
                self.setPixmap(QPixmap('graphics/mage2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/mage2_p2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.NINJA:
            if self.creature.player == Player.HUMAN:
                self.setPixmap(QPixmap('graphics/ninja2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/ninja2_p2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.SNIPER:
            if self.creature.player == Player.HUMAN:
                self.setPixmap(QPixmap('graphics/sniper2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/sniper2_p2.png').scaled(self.tile_size, self.tile_size))
        
    def update_tooltip(self):
        self.setToolTip("Name: {}\nHP: {}".format(self.creature.get_name(), self.creature.get_hp()))
    
    def updateAll(self):
        self.updatePosition()
        self.update_tooltip()

    def updatePosition(self):
        self.setPos(QPointF(self.creature.get_location().get_x()*self.tile_size, (self.creature.get_location().get_y())*self.tile_size))
        


    def update_sprite(self): # modify tiles to free if trees burn
        pass

    def mousePressEvent(self, event): # set creature active if it's players turn
        self.creature.set_moving(self.creature.player.is_moving())
        self.creature.set_attacking(self.creature.player.is_attacking())
        
    
        
            
        
