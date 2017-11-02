# URLify
# Wirte a method to replace all spaces in a string with "%20".
# You may assume the string has sufficient space at the end to
# hold the additional characters, and that you are given the
# "true" length of the string.
# e.g. 
# Input:    'Mr. John Smith    ', 13
# output:   'Mr.%20John%20Smith'

def urlify(str, trueLength):
  s = ''
  for i in range(trueLength):
    print(i, str[i])
    if str[i] == ' ' and ord(str[i]) == 32: s += '%20'
    else: s += str[i]
  return s


test = 'what the fuck haha    '
print( urlify(test, 18) )