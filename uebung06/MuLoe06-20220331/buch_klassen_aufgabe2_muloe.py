# -*- coding: utf-8 -*-
# klassen_aufgabe2_muloe.py


class Robot:
    '''This is a Robot.'''

    _orientation_vectors = {
            'north': [0, 1],
            'south': [0, -1],
            'west': [-1, 0],
            'east': [1, 0],
            }

    def __init__(self, name, position=[0, 0], orientation='north'):
        '''Initializes the robot.

        Arguments:
            name -- name of the robot, max length: 10 characters
            position -- the position [x, y] of the robot (default: [0, 0])
            orientation -- [north|south|west|east] (default: north)
        '''
        self.position = position
        self.orientation = orientation
        self.name = name

    def __str__(self):
        return 'Name: {}\nPosition: {}\nOrientation: {}'.format(
                self.name,
                self.position,
                self.orientation,
                )

    @property
    def position(self):
        '''Returns the position of the robot.
        '''
        return self._position

    @position.setter
    def position(self, position):
        # If the position is valid
        if isinstance(position, (list, tuple)) \
                and len(position) == 2 \
                and isinstance(position[0], (int, float)) \
                and isinstance(position[1], (int, float)):
            # Convert to a list if not already the case.
            # By doing so, a copy of the object is automatically created
            # and this ensures that any external reference is removed,
            # otherwise the attribute could still be modified by the external
            # references.
            self._position = list(position)
        else:
            raise ValueError('invalid position')

    @property
    def orientation(self):
        '''Returns the orientation of the robot: [north|south|west|east]
        '''
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        # If the orientation is not valid
        if orientation not in Robot._orientation_vectors:
            raise ValueError('invalid orientation')
        # Apply the new orientation.
        self._orientation = orientation

    @property
    def name(self):
        '''Returns the name of the robot.
        '''
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise
        # Limit the name to ten characters.
        self._name = name[:10]

    def move(self, distance):
        '''Moves the robot.
        '''
        # If the distance ist not an integer or float
        if not isinstance(distance, (int, float)):
            raise ValueError('invalid distance')
        # Move the robot
        vector = Robot._orientation_vectors[self.orientation]
        self.position[0] += distance*vector[0]
        self.position[1] += distance*vector[1]


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    x = Robot('Hugo', [0, 0], 'north')
    print(x)
    print('\nmove(1)\n')
    x.move(1)
    print(x)
    print('\norientation = west')
    x.orientation = 'west'
    print('move(2)\n')
    x.move(2)
    print(x)

#    help(Robot)
