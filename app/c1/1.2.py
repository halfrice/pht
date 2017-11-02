# Check Permutation
# Given two strings, wrote a method to decide if one is a permutation 
# of the other.

def checkPerm(str1, str2):
  if len(str1) != len(str2): return False
  return sorted(str1) == sorted(str2)



# test =  ['lmao', 'amol']
test = ['God ', 'do G']
print(checkPerm(test[0],test[1]))
