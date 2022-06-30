# -*- coding: utf-8 -*-
# primzahlen_muloe.py

import timeit


def primes(n):
    results = []
    for i in range(2, n + 1):
        for k in range(2, i):
            if not (i % k):
                break
        else:
            results.append(i)
    return results


def primes_fast(n):
    results = [2] if n >= 2 else []
    for i in range(3, n + 1):
        if not (i % 2):
            continue
        for k in range(3, int(i**0.5) + 2, 2):
            if not (i % k):
                break
        else:
            results.append(i)
    return results


if __name__ == '__main__':

    print(primes(30))
    print(primes_fast(30))

    n = 10000
    t_normal = timeit.timeit(lambda: primes(n), number=5)
    t_fast = timeit.timeit(lambda: primes_fast(n), number=5)
    print(f'primes({n}): {t_normal:g} s')
    print(f'primes_fast({n}): {t_fast:g} s')
    print(f'speedup: {t_normal/t_fast*100:.1f}%')
