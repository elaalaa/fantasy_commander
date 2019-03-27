from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPointF
from PyQt5.QtGui import QColor, QBrush

class Creature_graphitem(QtWidgets.QGraphicsPolygonItem):
   

    def __init__(self, creature, tile_size):
        # Call init of the parent object
        super(Creature_graphitem, self).__init__()

        # Do other stuff
        self.creature = creature
        self.tile_size = tile_size
        brush = QtGui.QBrush(1) # 1 for even fill
        self.setBrush(brush)
        self.constructTriangleVertices()
        self.updateAll()

    def constructTriangleVertices(self):
        
        # Create a new QPolygon object
        triangle = QtGui.QPolygonF()

        # Add the corners of a triangle to the the polygon object
        triangle.append(QtCore.QPointF(self.tile_size/2, 0)) # Tip
        triangle.append(QtCore.QPointF(0, self.tile_size)) # Bottom-left
        triangle.append(QtCore.QPointF(self.tile_size, self.tile_size)) # Bottom-right
        triangle.append(QtCore.QPointF(self.tile_size/2, 0)) # Tip

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(triangle)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(self.tile_size/2, self.tile_size/2)

    def updateAll(self):
        
        self.updatePosition()
        #self.updateColor()

    def updatePosition(self):
        
        self.setPos(QPointF(self.creature.get_location().get_x()*self.tile_size, self.creature.get_location().get_y()*self.tile_size))
        #pass # Replace me with correct implementation!
        


    '''def updateColor(self): # copy to tile_graphitem # tiilille taa jos ne vaihtuu
        
        #pass # Replace me with correct implementation!
        if self.robot.is_broken():
            self.setBrush(QBrush(QColor(255,0,0)))
        elif self.robot.is_stuck():
            self.setBrush(QBrush(QColor(255,255,0)))
        else:
            self.setBrush(QBrush(QColor(0,255,0)))'''

    '''def mousePressEvent(self, *args, **kwargs): #jos on olion vuoro, laita aktiiviseksi
        
        #pass # Replace me with correct implementation!
        if self.robot.is_broken():
            self.robot.fix()''' # tiilelle oma press event, jos joku olio on aktiivinen, siirrä olio kyseiseen tiileen
        
