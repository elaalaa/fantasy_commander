from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPointF
from PyQt5.QtGui import QColor, QBrush

class Creature_graphitem(QtWidgets.QGraphicsPolygonItem):
    '''
    The class RobotGraphicsItem extends QGraphicsPolygonItem to link it together to the physical
    representation of a Robot. The QGraphicsPolygonItem handles the drawing, while the
    Robot knows its own location and status.

    NOTE: unfortunately the PyQt5 uses different naming conventions than the rest
    of this project. We are also overriding the mousePressEvent()-method, whose
    name cannot be changed. Therefore, this class has a different style of naming the
    method names. (for example: updatePosition() vs update_position())
    '''
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
        '''
        This method sets the shape of this item into a triangle.

        The QGraphicsPolygonItem can be in the shape of any polygon.
        We use triangles to represent robots, as it makes it easy to
        show the current facing of the robot.
        '''
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
        '''
        Updates the visual representation to correctly resemble the current
        location, direction and status of the parent robot.
        '''
        self.updatePosition()
        #self.updateColor()

    def updatePosition(self):
        '''
        Implement me!

        Update the coordinates of this item to match the attached robot.
        Remember to take in to account the size of the squares.

        A robot in the first (0, 0) square should be drawn at (0, 0).

        See: For setting the position of this GraphicsItem, see
        QGraphicsPolygonItem at http://doc.qt.io/qt-5/qgraphicspolygonitem.html
        and its parent class QGraphicsItem at http://doc.qt.io/qt-5/qgraphicsitem.html

        For getting the location of the parent robot, look at the Robot-class
        in robot.py.
        '''
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
        
