# -*- coding: utf-8 -*-

matrix = [[1, 2, 3, 4, 5, 6],
          [10, 20, 30, 40, 50, 60],
          [100, 200, 300, 400, 500, 600]]

# Anstelle von Listen-Abstraktionen werden hier Generator-Ausdrücke als
# Argumente für die join-Methoden benutzt.
matrix_str = '\n'.join(';'.join(str(n) for n in row) for row in matrix)

matrix_csum = [sum(col) for col in zip(*matrix)]

print(matrix_str)
print(matrix_csum)
