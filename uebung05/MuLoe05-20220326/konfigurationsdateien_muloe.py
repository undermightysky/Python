# -*- coding: utf-8 -*-

import pathlib


def save_parameters(data, fname, encoding='utf-8'):
    text = '\n'.join(f'{k}={v}' for k, v in data.items())
    pathlib.Path(fname).write_text(text, encoding=encoding)
    # alternative solution without pathlib:
    # with open(fname, 'w', encoding=encoding) as file:
    #     file.write(text)


def load_parameters(fname, encoding='utf-8'):
    data = {}
    with open(fname, encoding=encoding) as file:
        for line in file:
            param = line.split('=')
            if len(param) == 2:
                data[param[0].strip()] = param[1].strip()
    return data


if __name__ == '__main__':
    gui_settings = {
        'language': 'English',
        'size': (700, 500),
        'dpi': 96,
        'save_on_exit': True,
        }
    save_parameters(gui_settings, 'settings.txt')
    print(load_parameters('settings2.txt'))
