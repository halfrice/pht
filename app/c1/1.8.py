# Zero Matrix
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.

import unittest

def zero_matrix(m):
  print('\ntesting zero_matrix() with matrix:')
  for i in m:
    print(i)

  z = []
  for r in range(len(m)):
    for c in range(len(m[r])):
      if m[r][c] == 0:
        z.append([r,c])

  for v in range(len(z)):
    r = z[v][0]
    c = z[v][1]
    for i in range(len(m)):
      if i == r:
        for j in range(len(m)):
          if m[r][j] != 0:
            m[r][j] = 0
      if m[i][c] != 0:
        m[i][c] = 0

  print('\nmatrix after calculations:')
  for j in range(len(m)):
    print(m[j])
  return

class Test(unittest.TestCase):
  def setUp(self):
    self.test_matrix = [[1,0,3],[4,5,6],[7,8,9]]

  def test_zero_matrix(self):
    zero_matrix(self.test_matrix)

if __name__ == '__main__':
  unittest.main()