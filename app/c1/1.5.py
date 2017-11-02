# One Away
# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to 
# check if they are one edit (or zero edits) away.
# EXAMPLE
# pale,  ple   -> true
# pales, pale  -> true
# pale,  bale  -> true
# pale,  bake  -> false

def oneAway(s1, s2):
  min,max = (s1,s2) if len(s1) <= len(s2) else (s2,s1)
  freqMin = getFreqTable(min)
  freqMax = getFreqTable(max)

  diff = 0
  for c in freqMax:
    if c in freqMin: diff += freqMax[c] - freqMin[c] 
    else: diff += freqMax[c]
  print(diff)

  if diff <= 1 and not diff < 0: return True
  return False

def getFreqTable(array):
  ht = {}
  for c in array:
    if c in ht: ht[c] += 1
    else: ht[c] = 1
  return ht

# test = ['pale', 'ple']
# test = ['pale', 'bake']
test = ['abdcefgbeg', 'abbcdeefggg']
print( oneAway(test[0], test[1]) )