# Is Unique
# Implement an algorithm to determine if a stirng has all unique charaters.
# What if you cannot use additional data structures?

def isUnique(str):
  ht = {}
  for i,w in enumerate(str):
    if w in ht: return False
    ht[w] = 1
  return True


test = 'abdcdefghijklmnop'
print( isUnique(test) )