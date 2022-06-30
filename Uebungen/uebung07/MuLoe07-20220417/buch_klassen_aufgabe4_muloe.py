# -*- coding: utf-8 -*-
# klassen_aufgabe4_muloe.py

# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types


class CaveInt:
    '''Neandertal integer numbers.'''

    def __init__(self, s):
        '''Creates an integer number.

        Argumente:
            s -- string that contains the characters
        '''
        # If the argument is invalid
        if not isinstance(s, str):
            raise TypeError('invalid argument')

        # Save the argument as internal string.
        self._s = s

    def __str__(self):
        '''Returns the internal string.
        '''
        return self._s

    def _test_compatibility(self, other):
        if not isinstance(other, (CaveInt, str)):
            raise TypeError(f'CaveInt and {type(other)} are incompatible.')

    def __add__(self, other):
        '''Returns the sum of the two objects.

        Arguments:
            other -- CaveInt or string object
        '''
        # Check the type.
        self._test_compatibility(other)

        # Return the result as a new object.
        return CaveInt(str(self) + str(other))

    def __sub__(self, other):
        '''Returns the difference of the two objects.

        Arguments:
            other -- CaveInt or string object
        '''
        # Check the type.
        self._test_compatibility(other)

        # Keep the difference of the characters.
        s_new = self._s[:max(0, len(self._s) - len(str(other)))]

        # Return the result as a new object.
        return CaveInt(s_new)

    def __mul__(self, other):
        '''Returns the product of the two objects.

        Arguments:
            other -- CaveInt or string object
        '''
        # Check the type.
        self._test_compatibility(other)

        # Return the result as a new object.
        return CaveInt(self._s*len(str(other)))

    def __floordiv__(self, other):
        '''Returns the integer quotient of the two objects.

        Arguments:
            other -- CaveInt or string object
        '''
        # Check the type.
        self._test_compatibility(other)

        # Return the result as a new object.
        return CaveInt(self._s[:len(self._s)//len(str(other))])

    def __truediv__(self, other):
        ''' Same as __floordiv__().
        '''
        return self.__floordiv__(other)

    def __int__(self):
        '''Returns the number as int.
        '''
        return len(self._s)


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    x = CaveInt('IIIII')
    y = CaveInt('iii')

    print('x =', x)
    print('y =', y)

    print('int(x) =', int(x))
    print('int(y) =', int(y))
    print('x + y =', x + y)
    print('x - y =', x - y)
    print('x + "II" =', x + 'II')
    print('x - "II" =', x - 'II')

    print('x*y =', x*y)
    print('x/y =', x/y)
    print('x//y =', x//y)

#    help(x)
