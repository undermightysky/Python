#%%
import numpy as np

class Sudoku:
  def __init__(self, init_values):
    self.b = np.array(init_values)
  
  def __str__(self):
    #s = '\n'.join(' '.join(line) for line in self.b[:])
    return ('\n'.join(' '.join(str(e) for e in line) for line in self.b))

  def insert(self, row, col, value):
    if(self.b[row, col] == 0 and
      value not in self.b[row, :] and
      value not in self.b[:, col])  :
      self.b[row, col] = value
      return True
    else:
      return False

sudoku_init = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
               [8, 0, 0, 0, 2, 3, 0, 0, 6],
               [0, 3, 0, 0, 6, 0, 0, 7, 0], 
               [0, 0, 1, 0, 0, 0, 6, 0, 0], 
               [5, 4, 0, 0, 0, 0, 0, 1, 9], 
               [0, 0, 2, 0, 0, 0, 7, 0, 0], 
               [0, 9, 0, 0, 3, 0, 0, 8, 0], 
               [2, 0, 0, 8, 0, 4, 0, 0, 7], 
               [0, 1, 0, 9, 0, 7, 0, 6, 0]]

s = Sudoku(sudoku_init)
print(s.insert(0,2,666))
print(s)


#%%

#%%

#%%

