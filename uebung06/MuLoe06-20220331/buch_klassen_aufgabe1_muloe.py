# -*- coding: utf-8 -*-
# klassen_aufgabe1_muloe.py


class Robot:
    '''This is a Robot.'''

    def __init__(self, name):
        '''Initializes the Robot with the given name.

        Arguments:
            name -- the name of the robot
        '''
        # the setter method of the property is triggered here
        self.name = name

    @property
    def name(self):
        '''Returns the name of the robot.'''
        return self._name

    @name.setter
    def name(self, name):
        '''Sets the name of the robot.'''
        if name == 'Hugo':
            name = 'Marvin'
        self._name = name

#    @name.deleter
#    def name(self):
#        del self._name


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    x = Robot('Marvin')
    y = Robot('Hugo')
    print(x.name, y.name)

#    help(Robot)
