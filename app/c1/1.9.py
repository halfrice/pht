# String Rotation
# Assume you have a method isSubstring which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation of 
# s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of
# "erbottlewat").

import unittest

def isSubstring(s1, s2):
  for i in range(len(s1)):
    if s1[i] == s2[0]:
      compare = ''
      overflow = 0
      for x in range(len(s1)):
        if i+x >= len(s1):
          overflow = len(s1)
        compare += s1[(i+x)-overflow]
      # print(compare)

      j = 0
      while compare[j] == s2[j]:
        # print(compare[j], s2[j])
        j += 1
        if j == len(s1)-1:
          return True
  return False


class Test(unittest.TestCase):
  def setUp(self):
    self.s1 = 'waterbottle'
    self.s2 = 'erbottlewat'

  def test_isSubstring(self):
    print('testing is_substring with s1:',self.s1,', and s2:',self.s2)
    ans = isSubstring(self.s1, self.s2) 
    print(ans)
    print('end of test_is_substring')

if __name__ == '__main__':
  unittest.main()
