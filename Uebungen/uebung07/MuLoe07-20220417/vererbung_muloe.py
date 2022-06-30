# -*- coding: utf-8 -*-

from pet import Pet


class Dog(Pet):
    def __init__(self, name, date_of_birth, **kwargs):
        # cooperative inheritance
        super().__init__(name=name, date_of_birth=date_of_birth, **kwargs)

    @property
    def age(self):
        return super().age*5.5

    def woof(self):
        print('bow-wow!')


class Hamster(Pet):
    def __init__(self, name, date_of_birth, **kwargs):
        # cooperative inheritance
        super().__init__(name=name, date_of_birth=date_of_birth, **kwargs)

    @property
    def age(self):
        return super().age*39


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':

    d = Dog('Lassie', '1.1.2019')
    print(f'{d.name} is {d.age:.1f} years old.')
    d.woof()

    h = Hamster(name='Daisy', date_of_birth='1.1.2019')
    print(f'{h.name} is {h.age:.1f} years old.')
