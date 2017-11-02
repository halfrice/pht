# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a
# palindrome. A palindrome is a word or phrase that is the same forwards
# and backwards. A permutation is a rearrangement of letters. The
# palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:    Tact Coa
# Output:   True (permutations: "taco cat", "atco, cta", etc.)

def palindromePermutation(str):
  s = ''.join(str.lower().split())
  freq = {}
  for w in s:
    if w in freq: freq[w] += 1
    else: freq[w] = 1
  isOdd = len(s)%2 != 0
  foundOdd = False
  for w in freq:
    # print(w, freq[w], odd)
    if isOdd and foundOdd: return False
    if isOdd & not foundOdd: 
      print('found odd!')
      foundOdd = True 
  return True


test = 'Tact Coac'
print( palindromePermutation(test) )