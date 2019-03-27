from tile import Tile

class Map():
    '''
    The class RobotWorld describes a two dimensional world made up
    of squares that different kinds of robots can inhabit. The squares are
    identified by unique coordinates which range from 0...width-1 and
    0...height-1. Each square is represented by a Square object.

    Robots can be added to the robot world, and the robot world
    maintains a robot listing which allows robots to take their turns in
    a round-robin fashion, in the order in which they were added.
    Each robot is represented by a Robot object.

    See the documentation Robot, Square, Coordinates
    '''


    def __init__ (self, width, height):
        '''
        Creates a new robot world with the specified dimensions.
        Initially all the squares of the new world are empty.

        Parameter width is the width of the world in squares: int

        Parameter height is the height of the world in squares: int
        '''
        self.tiles = [None] * width
        for x in range(self.get_width()):      # stepper
            self.tiles[x] = [None] * height
            for y in range(self.get_height()):    # stepper
                self.tiles[x][y] = Tile()    # fixed value
        self.creatures = []                        # container
        self.turn = 0                         # kinda like stepper (but not quite) index to robots list


    def get_width(self):
        '''
        Returns width of the world in squares: int
        '''
        return len(self.tiles)


    def get_height(self):
        '''
        Returns the height of the world in squares: int
        '''
        return len(self.tiles[0])


    def add_creature(self, creature, location):
        '''
        Adds a new robot in the robot world. (Note! This method also
        takes care that the robot is aware if its new position.
        This is done by calling robot's set_world method.)

        Parameter robot is the robot to be added: Robot

        Parameter location is the coordinates of the robot: Coordinates

        Parameter facing is the direction the robot is facing initially : tuple

        Returns False if the square at the given location is not empty or the given robot is already located in some world (this or some other world), True otherwise: boolean

        See Robot.set_world(RobotWorld, Coordinates, Direction)
        '''
        if creature.set_map(self, location):
            self.creatures.append(creature)
            self.get_tile(location).set_creature(creature)
            return True
        else:
            return False


    def get_tile(self, location):
        '''
        Parameter coordinates is a location in the world: Coordinates

        Returns the square that is located at the given location. If the given coordinates point outside of the world,
        this method returns a square that contains a wall and is not located in any robot world: Square
        '''
        if self.contains(location):
            return self.tiles[location.get_x()][location.get_y()]
        else:
            return Tile(True)


    def get_number_of_creatures(self):
        '''
        Returns the number of robots added to this world: int
        '''
        return len(self.creatures)


    def get_robot(self, turn_number):
        '''
        Returns the robot which has the given "turn number".
        The turn numbers of the robots in a world are determined by
        the order in which they were added. I.e., the first robot has
        a turn number of 0, the second one's number is 1, etc.

        Parameter turn_number is the turn number of a robot. Must be on the interval [0, (number of robots minus 1)].: int

        Returns the robot with the given turn number: robot object
        '''
        if 0 <= turn_number < self.get_number_of_creatures():
            return self.creatures[turn_number]
        else:
            return None


    def get_next_creature(self):
        '''
        Returns the robot to act next in this world's round-robin turn system, or None if there aren't any robots in the world: Robot

        See next_robot_turn()
        '''
        if self.get_number_of_creatures() < 1:
            return None
        else:
            return self.creatures[self.turn]


    def next_creature_turn(self):
        '''
        Lets the next robot take its turn. That is, calls the
        take_turn method of the robot whose turn it is,
        and passes the turn to the next robot. The turn is passed
        to the robot with the next highest turn number (i.e. the one
        that was added to the world after the current robot), or wraps
        back to the first robot (turn number 0) if the last turn number
        was reached. That is to say: the robot which was added first,
        moves first, followed by the one that was added second, etc.,
        until all robots have moved and the cycle starts over.
        If there are no robots in the world, the method does nothing.

        See get_next_robot()
        '''
        current = self.get_next_creature()
        if current is not None:
            self.turn = (self.turn + 1) % self.get_number_of_creatures()
            current.take_turn()



    def next_full_turn(self):
        '''
        Lets each robot take its next turn. That is, calls the next_robot_turn
        a number of times equal to the number of robots in the world.
        '''
        for count in range(self.get_number_of_creatures()):      # stepper
            self.next_robot_turn()


    def contains(self, location):
        '''
        Determines if this world contains the given coordinates.

        Parameter coordinates is a coordinate pair: Coordinates

        Returns a boolean value indicating if this world contains the given coordinates: boolean
        '''
        x_coordinate = location.get_x()
        y_coordinate = location.get_y()
        return 0 <= x_coordinate < self.get_width() and 0 <= y_coordinate < self.get_height()



    def get_creatures(self):
        '''
        Returns an array containing all the robots currently located in this world: list
        '''
        return self.creatures[:]
