# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# [1,2]   [3,1]
# [3,4]   [4,2]

# [1,2,3]   [7,4,1]
# [4,5,6]   [8,5,2]
# [7,8,9]   [9,6,3]


# [01,02,03,04]  [13,09,05,01]
# [05,06,07,08]  [14,10,06,02]
# [09,10,11,12]  [15,11,07,03]
# [13,14,15,16]  [16,12,08,04]


# [01,02,03,04,05]
# [06,07,08,09,10]
# [11,12,13,14,15]
# [16,17,18,19,20]
# [21,22,23,24,25]

# [21,16,11,06,01]
# [22,16,12,07,02]
# [23,18,13,08,03]
# [24,19,14,09,04]
# [25,20,15,10,05]

# 1 for 3
# 3 for 9
# 9 for 7
# 7 for 1
import unittest

def rotate_matrix(m):
  print('\ntesting rotate_matrix() with matrix:')
  for i in range(len(m)):
    print(m[i])

  for i in range(len(m)//2+1):
    for j in range(i,len(m[i])-1-i):
      # top = m[i][j]
      # right = m[j][len(m[i])-1-i]
      # bottom = m[len(m[i])-1-i][len(m[i])-1-j]
      # left = m[len(m[i])-1-j][i]
      # print(top, right, bottom, left)
      temp = m[i][j]
      m[i][j] = m[len(m[i])-1-j][i] #top with left
      m[len(m[i])-1-j][i] = m[len(m[i])-1-i][len(m[i])-1-j] # left with bottom
      m[len(m[i])-1-i][len(m[i])-1-j] = m[j][len(m[i])-1-i] #bottom with right
      m[j][len(m[i])-1-i] = temp #right with temp(top)

  print('\nmatrix after calculations:')
  for j in range(len(m)):
    print(m[j])
  return

def get_row(m, i):
  return m[i]

def get_col(m, i):
  r = []
  for j in range(len(m)):
    r.append(m[j][i])
  return r


class Test(unittest.TestCase):
  def setUp(self):
    self.test_matrix = [[1,2],[3,4]]
    # self.test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # self.test_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # self.test_matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

  def test_get_row(self):
    r = get_row(self.test_matrix, 1)
    # self.assertEqual(r, [4,5,6])

  def test_get_col(self):
    c = get_col(self.test_matrix, 1)
    # self.assertEqual(c, [2,5,8])

  def test_rotate_matrix(self):
    rotate_matrix(self.test_matrix)

if __name__ == '__main__':
  unittest.main()
