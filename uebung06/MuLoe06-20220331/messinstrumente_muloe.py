# -*- coding: utf-8 -*-


class MeasuringInstrument:
    inventory = {}

    def __init__(self, inventory_number, name):
        self._inventory_number = inventory_number
        self._name = name
        MeasuringInstrument.inventory[inventory_number] = {'name': name}

    @property
    def inventory_number(self):
        return self._inventory_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        MeasuringInstrument.inventory[self._inventory_number]['name'] = name

    def __del__(self):
        MeasuringInstrument.inventory.pop(self._inventory_number)


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    print(MeasuringInstrument.inventory)

    inst1 = MeasuringInstrument(inventory_number=64581, name='Fluke 85')
    print(inst1.inventory_number)
    print(inst1.name)

    print(MeasuringInstrument.inventory)

    inst2 = MeasuringInstrument(inventory_number=301991, name='HP 34401A')

    print(MeasuringInstrument.inventory)

    del inst1
    print(MeasuringInstrument.inventory)

    inst2.name = 'Keysight 34470A'
    print(MeasuringInstrument.inventory)
