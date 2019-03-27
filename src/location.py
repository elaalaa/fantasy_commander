class Location():
    
    def __init__(self, x, y):
        '''
        Creates a new coordinate pair.

        Parameter x: int

        Parameter y: int
        '''
        self.x = x    # fixed value
        self.y = y    # fixed value


    def get_x(self):
        '''
        Returns the x coordinate (int)
        '''
        return self.x



    def get_y(self):
        '''
        Returns the y coordinate (int)
        '''
        return self.y



    def __str__(self):
        '''
        Returns a string of the form (X, Y) representing of the coordinate pair

        '''
        return '({:.0f}, {:.0f})'.format(self.get_x(), self.get_y())
