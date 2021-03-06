# -*- coding: utf-8 -*-

# %%

# --- Implementierung Testat --------------------------------------------------
# Implementieren Sie hierdie Lösung für die zweite Testataufgabe.

import numpy as np


def netlist_parser(fname) -> dict:
    '''
    returns dictionary with elements read from textfile
    '''
    netlist = {}
    with open(fname) as f:
        for line in f:
            if line.startswith('*'):
                continue
            name, npl, nm, *kwargs, val = line.split(';')[0].split()
            try:
                val = float(val)
            except (ValueError):
                pref = {'f': 10**-15,
                        'p': 10**-12,
                        'n': 10**-9,
                        'u': 10**-6,
                        'm': 10**-3,
                        'k': 10**3,
                        'meg': 10**6,
                        'g': 10**9,
                        't': 10**12
                        }

                prfx = ''
                while val[-1:].isalpha():
                    prfx = val[-1:] + prfx
                    val = val[:-1]

                val = pref[prfx.lower()] * float(val)

            netlist[name] = {'n+': 'Vn'+npl,
                             'n-': 'Vn'+nm,
                             'value': float(val)}

    return netlist


def inventory(elements) -> str:
    '''
    returns element names as formated string
    '''

    inv = {'Resistors': [], 'Voltage Sources': [], 'Current Sources': []}

    for e in elements.keys():
        if('R' in e.upper()):
            inv['Resistors'].append(e.capitalize())
        if('V' in e.upper()):
            inv['Voltage Sources'].append(e.capitalize())
        if('I' in e.upper()):
            inv['Current Sources'].append(e.capitalize())

    res = ''

    for key, value in inv.items():
        res += key + ': '
        res += ', '.join(value)
        res += '\r\n'

    return '\r\n'.join(res.splitlines())


def mna_build(elements) -> tuple:
    '''
    returns list of unknowns, matrix M and sourcevector
    '''
    # add unknown knot-voltages to unknowns
    unknowns = []
    for it in elements.values():
        if it['n+'] not in unknowns and it['n+'] != 'Vn0':
            unknowns.append(it['n+'])
            unknowns.sort()

    # add unknown currents of voltage sources to unknowns
    unknI = []
    for e in elements.keys():
        if('V' in e.upper()):
            unknI.append('I'+e.lower())
    unknowns += sorted(unknI)

    # build M
    M = np.zeros((len(unknowns), len(unknowns)))
    y = np.zeros_like(unknowns, dtype=float)

    # iterate all elements
    for k, val in elements.items():
        # get index of N+
        iNp = int(val['n+'].replace('Vn', ''))-1
        # get index of N-
        iNm = int(val['n-'].replace('Vn', ''))-1
        # fill resistor stamps
        if 'R' in k.upper():
            if (iNp >= 0):
                M[iNp, iNp] += 1 / float(val['value'])
            if (iNm >= 0):
                M[iNm, iNm] += 1 / float(val['value'])
            if (iNp >= 0 and iNm >= 0):
                M[iNp, iNm] -= 1 / float(val['value'])
                M[iNm, iNp] -= 1 / float(val['value'])
        # fill current stamps
        if 'I' in k.upper():
            if (iNp >= 0):
                y[iNp] = -float(val['value'])
            if (iNm >= 0):
                y[iNm] = float(val['value'])
        # fill voltage stamps
        if 'V' in k.upper():
            iVs = unknowns.index('I'+k.lower())
            if (iNp >= 0):
                M[iNp, iVs] = 1
                M[iVs, iNp] = 1
            if(iNm >= 0):
                M[iVs, iNm] = -1
                M[iNm, iVs] = -1
            y[iVs] = val['value']
    return unknowns, M, y


def mna_solve(unknowns, M, y) -> dict:
    '''
    calculates unknowns of mna
    '''
    solution = {}

    x = np.linalg.solve(M, y)

    # build solution dict
    for i, xVal in enumerate(x):
        solution[unknowns[i]] = xVal

    return solution


def mna_report(elements, solution) -> dict:
    '''
    returns calculated currents and voltages as dictionary
    '''
    report = {}
    solution['Vn0'] = 0

    # calculating U and I for every element and adding results to report dict
    for key, value in elements.items():
        if('R' in key.upper()):
            voltage = float(solution[value['n+']] - solution[value['n-']])
            current = float(voltage)/float(value['value'])
        if('V' in key.upper()):
            voltage = float(value['value'])
            current = float(solution['I'+key.lower()])
        if('I' in key.upper()):
            voltage = float(solution[value['n+']] - solution[value['n-']])
            current = float(value['value'])
        report[key.capitalize()] = {'V': voltage, 'I': current}
    return report


# --- Testcode ----------------------------------------------------------------
# Fügen Sie hier Ihren Testcode ein. Nutzen Sie dafür unter anderem die
# Code-Beispiele in den grauen Boxen der Aufgabenstellung sowie auch die
# Angaben in den *.results Files im abgegebenen Ordner.
if __name__ == '__main__':

    # print(netlist_parser('netlist_test.cir'))
    # print(netlist_parser('netlist.cir'))
    # print(netlist_parser('netlist2.cir'))
    # print(netlist_parser('netlist3.cir'))

    # print(inv1)
    # print(inv2)
    # print(inv3)

    # netlist.clr
    n1 = netlist_parser('netlist.cir')
    inv1 = inventory(n1)
    print(inv1)
    unkn, M, y = mna_build(n1)
    solution = mna_solve(unkn, M, y)
    report = mna_report(n1, solution)
    print('Report: \r\n', report)

    # netlist2.clr
    n2 = netlist_parser('netlist2.cir')
    inv2 = inventory(n2)
    print(inv2)
    unkn, M, y = mna_build(n2)
    solution = mna_solve(unkn, M, y)
    report = mna_report(n2, solution)
    print('Report: \r\n', report)

    # netlist3.clr
    n3 = netlist_parser('netlist3.cir')
    inv3 = inventory(n3)
    print(inv3)
    unkn, M, y = mna_build(n3)
    solution = mna_solve(unkn, M, y)
    report = mna_report(n3, solution)
    print('Report: \r\n', report)

    # netlist4.clr
    n4 = netlist_parser('netlist4.cir')
    inv4 = inventory(n4)
    print(inv4)
    unkn, M, y = mna_build(n4)
    solution = mna_solve(unkn, M, y)
    report = mna_report(n4, solution)
    print('Report: \r\n', report)

    elements = netlist_parser("netlist_with_comments.cir")
    inv5 = inventory(elements)
    print(inv5)

    pass
