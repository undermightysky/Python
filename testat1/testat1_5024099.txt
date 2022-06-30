# -*- coding: utf-8 -*-

from storage_lib import Storage


# --- Implementierung Testat --------------------------------------------------
# Implementieren Sie hier die beiden Klassen ModuleBuilder
# und MissingModuleError.


class ModuleBuilder:
    """ This is the ModuleBuilder class.
    """

    def __init__(self, order_file, storage_path):
        """
        Creates a ModuleBuilder object.

        Parameters
        ----------
        order_file : string
            path to prodution list file
        storage_path : string
            path to storage folder

        Returns
        -------
        None.

        """
        self._order_data = {}
        self._storage = Storage(storage_path)

        with open(order_file, encoding='utf-8') as f:

            self._units = int(f.readline().split(';')[1])

            for element in f.readlines()[1:]:
                eref, etype, *rest = element.split(';')

                if(etype in self._order_data.keys()):
                    self._order_data[etype].append(eref)
                else:
                    self._order_data[etype] = [eref]

    def __str__(self):
        """
        Prints a table of the order data.

        Returns
        -------
        string
            table of order data

        """
        header = ['Article Number', 'Quantity', 'References']
        slist = []

        for art in self._order_data.items():
            slist.append(f"{art[0]:<18} {len(art[1]):<12} {' '.join(art[1])}")

        slist.sort()
        slist.insert(0, f"{header[0]:<18} {header[1]:<12} {header[2]}")

        maxlen = len(slist[0])
        for i in slist:
            if len(i) > maxlen:
                maxlen = len(i)

        slist.insert(1, '-' * maxlen)
        return '\n'.join(slist)

    def availability(self, units=None):
        """
        Creates an overview with availability of modules used for production.

        Parameters
        ----------
        units : int, optional
            number of units to produce. The default is None.

        Raises
        ------
        ValueError
            Raises ValueError if unit <= 0.

        Returns
        -------
        avModules : dict
            dictionary with availability of modules.

        """
        avModules = {}

        for article_number in self._order_data:
            if (self._storage.module_info(article_number) is not None):
                av = int(self._storage.module_info(article_number)['count'])
            else:
                av = 0

            if (units is None):
                units = self._units

            if (units <= 0):
                raise ValueError("The given value for units must be "
                                 "greater than 0.")
            req = int(len(self._order_data[article_number]) * units)

            avModules[article_number] = {"available": av, "required": req,
                                         "missing": int(req-av) if req-av >= 0
                                         else 0}
        return avModules

    def build(self):
        """
        Builds monitorung systems and takes modules out of storage.

        Raises
        ------
        MissingModuleError
            Raises MissingModuleError if not all modules available.

        Returns
        -------
        usedElem : int
            Number of used modules.

        """
        missing = []
        usedElem = 0

        for article_number in self._order_data:
            if (self.availability()[article_number]['missing'] > 0):
                missing.append(article_number)

        if (len(missing) == 0):
            for article_number in self._order_data:
                count = self.availability()[article_number]['required']
                self._storage.take_module(article_number, count)

                usedElem += count
        else:
            raise MissingModuleError(missing)

        return usedElem


class MissingModuleError(Exception):
    """ This is the MissingModuleError class.
    """

    def __init__(self, modules):
        """
        Creates a MissingModuleBuilder object.

        Parameters
        ----------
        modules : TYPE
            list of missing modules

        Returns
        -------
        None.

        """
        self.modules = tuple(modules)
        super().__init__(f"The following modules are missing from storage: "
                         f"{', '.join(self.modules)}")


# --- Testcode ----------------------------------------------------------------
# Fügen Sie hier Ihren Testcode ein. Nutzen Sie dafür unter anderem die
# Code-Beispiele in den grauen Boxen der Aufgabenstellung.
if __name__ == '__main__':

    mb = ModuleBuilder('orders/produktionsliste_1.csv', 'storage')
    print(mb)
    # mb.availability(0)
    print(mb.availability(2))
    print(mb._order_data)
    print(type(mb._storage))
    print(mb._units)
    print(mb._storage.module_info("CO304"))
    print(mb.build())

    try:
        print(mb.availability(units=-1))
    except ValueError as e:
        print(e)

    mb2 = ModuleBuilder('orders/produktionsliste_2.csv', "storage")
    print(mb2)
    print(mb2.availability(2))
    print(mb2._order_data)
    print(type(mb2._storage))
    print(mb2._units)
    print(mb2._storage.module_info("CO304"))

    print(mb2.build())

    pass
