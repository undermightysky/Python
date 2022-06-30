# -*- coding: utf-8 -*-


class SortedList(list):

    def __init__(self, x=None):
        '''Initializes the list and sorts it.
        '''
        super().__init__(x or [])
        super().sort()

    def __setitem__(self, index, value):
        '''Set self[index] to value.
        '''
        super().__setitem__(index, value)
        super().sort()

    def __iadd__(self, value):
        '''Implement self+=value.
        '''
        super().__iadd__(value)  # in-place add
        super().sort()
        return self  # return oneself

    def __imul__(self, value):
        '''Implement self*=value.
        '''
        super().__imul__(value)  # in-place multiplication
        super().sort()
        return self  # return oneself

    def append(self, object):
        '''Append object to the end of the list.
        '''
        super().append(object)
        super().sort()

    def extend(self, iterable):
        '''Extend list by appending elements from the iterable.
        '''
        super().extend(iterable)
        super().sort()

    def insert(self, index, object):
        '''Insert object before index.
        '''
        super().insert(index, object)
        super().sort()

    def reverse(self):
        '''Do nothing.
        '''
        pass

    def sort(self, *, key=None, reverse=False):
        '''Do nothing.

        The bare * is used to force the caller to use named arguments.
        See: https://www.python.org/dev/peps/pep-3102/
        '''
        pass


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    
    mylist = SortedList()
    print(mylist)

    mylist.append(3)
    print(mylist)

    mylist[0] = 5
    print(mylist)

    mylist += [20, 30]
    print(mylist)

    mylist *= 2
    print(mylist)

    mylist.append(1.5)
    print(mylist)

    mylist.extend([3.1, 3.2])
    print(mylist)

    mylist.insert(4, 0.5)
    print(mylist)

    mylist.reverse()
    mylist.sort(reverse=True)
    print(mylist)

#    help(SortedList)
