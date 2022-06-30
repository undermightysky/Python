# -*- coding: utf-8 -*-


class PhoneBook:

    def __init__(self, data=None):
        if data is None:
            self._data = {}
        else:
            self._data = data.copy()

    def add(self, name, number):
        self._data[name] = number

    def remove(self, name):
        self._data.pop(name)

    def __str__(self):
        return '\n'.join(f'{name}: {self._data[name]}'
                         for name in sorted(self._data.keys()))

    def __contains__(self, term):
        return term in self._data.keys() or term in self._data.values()

    def __getitem__(self, term):
        return {k: v
                for k, v in self._data.items()
                if term == k or term == v}


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    d = {'Alice': '004102', 'Carol': '004101', 'Ted': '004103'}
    pb = PhoneBook(d)
    pb.add('Wally', '004104')
    pb.add('Boss', '004101')
    pb.remove('Wally')
    print(pb)
    # print('search(Ted):', pb.search('Ted'))
    # print('search(546):', pb.search('546'))
    # print('search(+41):', pb.search('+41'))
    print('Dave in pb:', 'Dave' in pb)
    print('Alice in pb:', 'Alice' in pb)
    print('004101 in pb:', '004101' in pb)
    print('004105 in pb:', '004105' in pb)
    print(pb['Alice'])
    print(pb['004101'])
    print(pb['Catbert'])
