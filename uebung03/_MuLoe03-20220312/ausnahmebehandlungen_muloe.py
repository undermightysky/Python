# -*- coding: utf-8 -*-
# ausnahmebehandlungen_muloe.py


# ---

my_list = [0, 1, 2, 3, 'a', 'b', 'c']
for value in my_list:
    try:
        r_value = 1/value
    except ZeroDivisionError:
        print('ERROR: division by zero')
        r_value = None
    except TypeError:
        print('ERROR: wrong type')
        r_value = None

    print(f"Reziproker Wert von {value} ist {r_value}")

# ---

d = {'flower': 'lily', 'color': 'turquoise', 'fish': 'clownfish'}
t = (2020, 3, 4)
p = "1001.90 CHF"

try:
    d["dish"]
except KeyError:
    print('dish is not a key')

try:
    tup[0]
except NameError:
    print('the variable "tup" is not available')

try:
    t[3]
except IndexError:
    print('too few elements')

try:
    float(p)
except ValueError:
    print('invalid number')

try:
    c = t + p
except TypeError:
    print('these types can not added together')

try:
    t[0] = 2021
except TypeError:
    print('this variable can not be modified')

# ---


def student(name, id_number, visited_lectures):
    if not isinstance(name, str) or not name:
        raise ValueError(f'name is not a non-empty string')
    if not isinstance(id_number, int) or id_number < 0:
        raise ValueError(f'id_number={id_number} is not a non-zero integer')
    if not isinstance(visited_lectures, (list, tuple)):
        raise TypeError('visited_lectures is of type '
                        f'{type(visited_lectures).__name__} '
                        'instead of list or tuple')

    print(f'Name: {name}')
    print(f'ID: {id_number:d}')
    print('Visited:')
    for subject in visited_lectures:
        print(f' - {subject}')


# student('', 123456, ['FuVar', 'NaT', 'C++'])
# student('Dilbert', -5, ['FuVar', 'NaT', 'C++'])
# student('Dilbert', 123456, 'FuVar')
student('Dilbert', 123456, ['FuVar', 'NaT', 'C++'])

# ---
