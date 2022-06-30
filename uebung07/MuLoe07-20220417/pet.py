# -*- coding: utf-8 -*-
# pet.py

from datetime import datetime


class Pet:
    def __init__(self, name, date_of_birth):
        self.name = name
        self._date_of_birth = datetime.strptime(date_of_birth, '%d.%m.%Y')

    @property
    def age(self):
        return (datetime.now() - self._date_of_birth).days/365


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    p = Pet('Daisy', '1.1.2019')
    print(f'{p.name} is {p.age:.1f} years old.')
