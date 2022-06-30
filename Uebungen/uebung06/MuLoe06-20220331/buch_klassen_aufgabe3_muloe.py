# -*- coding: utf-8 -*-
# klassen_aufgabe3_muloe.py

import time


class Roboter:
    '''Ich bin die "Roboter"-Klasse.'''

    # Alle möglichen Strings,
    # Key: (alter > 20, self.energie >= 50)
    _stringwerte = {
            (False, False): 'Ausgelaugt',
            (False, True): 'Super!',
            (True, False): 'In Anbetracht meines Alters nicht so schlecht!',
            (True, True): 'Super. Vor allem in Anbetracht meines Alters!',
    }

    def __init__(self, name, baujahr, energie=100):
        '''Ich bin die Initialisierungsmethode.

        Argumente:
            name -- Name des Roboters
            baujahr -- Herstellungsjahr des Roboters
            energie -- Energiewert von 0-100 (default: 100)
        '''
        self.name = name
        self.baujahr = baujahr
        self.energie = energie

    @property
    def befinden(self):
        '''Gibt das Wohlbefinden des Roboters an.
        '''
        # Alter bestimmen
        alter = time.localtime().tm_year - self.baujahr
        # passender String auswählen
        choice = (alter > 20, self.energie >= 50)
        # String zurückgeben
        return Roboter._stringwerte.get(choice)


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    x = Roboter('Hugo', 1950, 60)
    y = Roboter('iRobot', 1997, 20)
    z = Roboter('Wall-E', 2008, energie=80)

    print(f'{x.name}: {x.befinden}')
    print(f'{y.name}: {y.befinden}')
    print(f'{z.name}: {z.befinden}')

#    help(Roboter)
