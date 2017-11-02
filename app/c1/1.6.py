# String Compression
# Implement a method to perform basic string compression using the counts of
# repeated characters. For example, the string aabcccccaaa would become 
# a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string. You can
# assume the string has only uppercase and lowercase letters (a-z).

import unittest

def stringCompression(s):
  r = ''
  count = 1
  for i in range(len(s)):
    curChar = s[i]
    nextChar = s[i+1] if i+1 < len(s) else None
    if nextChar and nextChar == curChar: count += 1
    else: 
      r += curChar+str(count)
      count = 1
  print(r)
  return r

def string_compression(s):
  r = ''
  og = ''
  count = 0
  for i in range(1,len(s)):
    # print(i,s[i-1],s[i+count])
    j = i
    while j+count < len(s) and s[i-1] == s[i+count]:
      count += 1
    else:
      r += s[i-1]+str(count+1)
      i += count
      count = 0
    print(r)
  print(r)
  return r


class Test(unittest.TestCase):
  def setUp(self):
    # test = 'aaaabbbbccccdab'
    # test = 'aabcccccaaa'
    self.test_str = 'abbcccbbbbaaaaa'

  def test_string_compression(self):
    print("testing string_compression with test string as '"+self.test_str+"'")
    result = string_compression(self.test_str)
    # self.assertEqual(result, 'a1b2c3b4a5')

if __name__ == '__main__':
  unittest.main()
