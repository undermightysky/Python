# -*- coding: utf-8 -*-


def rms(*values):

    # compute the square of the valid arguments only
    squares = [v**2 for v in values if isinstance(v, (int, float))]

    # raise an error if no valid values have been found.
    if not squares:
        raise TypeError('too few numeric arguments')

    # return the square root of the average
    return (sum(squares)/len(squares))**0.5


def vorstellung(**angaben):
    for k, v in angaben.items():
        print(f'Ihr {k} ist {v}.')


def append_to_book(name, phone_number='---', book=None):
    # You can not use book={} as default argument here. More information on:
    # https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
    if book is None:
        # create a new dictionary
        book = {}

    # add the new entry
    book[name] = phone_number

    return book

# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    print(rms(2, 3))
    print(rms(1, 5, 'x', 4))
    # print(rms('hallo'))

    vorstellung(Name="Susi", Alter=25, Wohnort="Rapperswil")

    my_book = {'Max': '+41582574111'}
    append_to_book('Moritz', '+41582574112', book=my_book)
    print(my_book)
    append_to_book('Susi', book=my_book)
    print(my_book)
    new_book = append_to_book('Julia')
    print(new_book)
    new_book2 = append_to_book('Romeo')
    print(new_book2)
