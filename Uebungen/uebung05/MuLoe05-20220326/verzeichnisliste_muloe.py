# -*- coding: utf-8 -*-

import pathlib


def directory_listing(directory, suffix=None):

    elements = []
    # iterate over all files and subdirectories in the given directory
    for path in pathlib.Path(directory).glob('*'):
        # keep all or only the files with the given suffix
        if suffix is None or path.suffix == suffix:
            element_type = 'f' if path.is_file() else 'd'
            element_size = path.stat().st_size
            element_name = path.name + ('/' if not path.is_file() else '')
            # append the element's information as tuple
            elements.append((element_type, element_size, element_name))

    if not elements:
        return '--- nothing found ---'

    # determine the length of the largest size number
    size_len = max(len(str(x[1])) for x in elements)

    # create the formatted output string
    text = '\n'.join(f'{t} {size:{size_len}d} {name}'
                     for t, size, name in elements)

    return text


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print('--- all ---')
    print(directory_listing('C:/Windows'))
    print('\n--- .exe only ---')
    print(directory_listing('C:/Windows', suffix='.exe'))
