

class Creature():
    '''
    The class Robot represents robots (or "bots") which inhabit two
    dimensional grid worlds. More specifically, each instance of the class represents
    a "robot body" (or "chassis" or "hardware") and basic functionality of such a robot.
    Each "robot body" is associated with a "robot brain" that controls the body
    and determines what functionality is activated and when.

    A robot is equipped with the various capabilities:

     - It can sense its own surroundings (location, facing, the world that it is in).

     - It can move forward.

     - It can spin around in any one of the four main compass directions.

     - It can sense whether it is broken or not, and whether it is "stuck" in a square
        between four walls.

    When a robot's take_turn() method is called, it uses its "brain" to figure
    out what to do (move, turn about, etc.). Robots with different kinds of brains behave
    differently.

    See the documentation of RobotWorld and RobotBrain.
    '''

    def __init__(self, name):
        '''
        Creates a new robot with the given name. The newly
        created robot is initially just a "dumb shell" until
        it's given a brain later using the method
        set_brain().

        If the given name is None or an empty
        string, the name is set to "Incognito".

        Parameter name is the name of the bot: string

        See set_brain(RobotBrain)
        '''
        self.set_name(name)
        self.map = None        # fixed value
        self.location = None     # most-recent holder
        self.destroyed = False   # flag
        self.brain = None       #brain varmaan mika tyyppi se on? tai miten liikkuu?


    def set_name(self, name):
        '''
        Sets the name of the robot.
        If the given name is None or an empty
        string, the name is set to "Incognito".

        Parameter name is the new name of the robot: string
        '''
        if not name:
            self.name = "Incognito"   # most-recent holder
        else:
            self.name = name


    def get_name(self):
        '''
        Returns the robot name : string
        '''
        return self.name


    def set_brain(self, new_brain):
        '''
        Sets a "brain" (or AI) for the robot (replacing any brain
        previously set, if any): spinbot, lovebot, drunkbot, ...

        Parameter new_brain is the artificial intelligence that controls the robot: spinbot/lovebot/drunkbot/... object
        '''
        self.brain = new_brain # tata ei valttamatta tarvi?


    def get_brain(self):
        '''
        Returns the "brain" (or AI) of the robot: spinbot/lovebot/drunkbot/... object
        '''
        return self.brain # taa olis tyyppi


    def get_map(self):
        '''
        Returns the world in which the bot is, or None if the robot has not been placed in any robot world: RobotWorld
        '''
        return self.map


    def get_location(self):
        '''
        Returns the current location of the robot in the robot world, or None if the robot has not been placed in any robot world: Coordinates

        See get_location_square()
        '''
        return self.location


    def get_tile(self):
        '''
        Returns the square that the robot is in: Square

        See get_location()
        '''
        return self.get_map().get_tile(self.get_location())



    def destroy(self):
        '''
        Breaks the robot, rendering it unoperational.

        See fix() and take_turn()
        '''
        self.destroyed = True



    def is_dead(self):
        '''
        Determines whether the robot is broken or not. A robot is broken
        if it has been broken with the method destroy() and
        not fixed since, or if it is lacking a brain.

        Returns the boolean value which states whether the bot is broken: boolean
        '''
        return self.destroyed



    def set_map(self, map, location):
        '''
        Places the robot in the given robot world at the specified
        coordinates.  Note! This method is supposed to be used from the
        addRobot method in the RobotWorld class,
        which makes sure that the robot is appropriately recorded as
        being part of the robot world.

        Parameter world is the robot world in which the bot is placed: RobotWorld

        Parameter location is the coordinates at which the bot is placed: Coordinates

        Parameter facing is the direction the robot is facing initially : tuple

        Returns False if the square at the given location is not empty or the robot is already located in some world (the given one or some other world), True otherwise: boolean

        See RobotWorld.add_robot(Robot, Coordinates, Direction)
        '''
        target_tile = map.get_tile(location)
        if not target_tile.is_empty() or self.get_map() is not None:
            return False
        else:
            self.map = map
            self.location = location
            return True


    def move(self, direction): # ei tarvita jos tehdaan mousepressilla?
        '''
        Changes the place of the robot within its current world
        from the current square to the square next to it in the
        given direction. The direction does not necessarily have
        to be the same one that the robot is originally facing in.
        This method changes the robot to face the direction it
        moves in. A broken robot can't move.

        Two robots can never be in the same square, neither can
        a robot and a wall. If the square at the given coordinates
        is not empty, a collision occurs instead and the robot
        does not move (but still turns to face whatever it collided
        with). If the moving robot collides with a wall,
        the robot itself breaks. If a moving robot collides with
        another robot, the other robot breaks and the moving robot
        stays intact.

        Parameter direction is the direction to move in: tuple

        Returns a boolean value indicating if the movement was successful (False means that either the robot was broken to begin with or that it collided with something instead of successfully moving): boolean
        '''
        if self.is_broken():
            return False

        target = self.get_location().get_neighbor(direction)
        current_square = self.get_location_square()
        target_square = self.get_world().get_square(target)
        self.spin(direction)
        if target_square.is_empty():
            current_square.remove_robot()
            self.location = target
            target_square.set_robot(self)
            return True
        elif target_square.get_robot() is not None:
            target_square.get_robot().destroy()
            return False
        else:   # collided with wall
            self.destroy()
            return False


    def move_forward(self): # ei tarvita
        '''
        Moves the robot forward one square. This is equivalent to calling self.move(self.get_facing()).

        See move(Direction)

        Returns a boolean value indicating if the movement was successful (False means that either the robot was broken to begin with or that it collided with something instead of successfully moving): boolean
        '''
        return self.move(self.get_facing())


    def take_turn(self): # ehka tarvitaan, pit‰‰ kattoo rakenne
        '''
        Gives the robot a turn to act. An unstuck, unbroken robot, however, consults its brain to
        find out what to do. This is done by calling the brain's method move_body().
        Here is a general outline of what happens during a robot's turn:
         1. The robot checks its sensors to see if it is stuck or broken. (If it is, it doesn't do anything.)
         2. If not, it call's it's brain's move_body() method, leaving it up to the brain to decide
            what happens next.
         3. The move_body() method will then determine how the robot behaves, usually calling
            various methods of the robot's body (i.e., the Robot object whose turn it is),
            e.g. move, spin. However, it is not up to the Robot object
            to decide which of its methods get called - that depends on the implementation of the robot's brain.

        See is_broken()

        See is_stuck()

        See RobotBrain.move_body()
        '''
        if not self.is_stuck() and not self.is_broken():
            self.brain.move_body()

    def __str__(self):
        return self.get_name() + ' at location ' + str(self.get_location())
