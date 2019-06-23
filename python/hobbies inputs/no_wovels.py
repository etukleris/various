def anti_vowel(text):
  total = ""
  print (text)
  for i in text:
    if i != "a" and i !="e" and i != "i" and i != "o" and i != "u" and i != "A" and i !="E" and i != "I" and i != "O" and i != "U":
      total= total + i
  print (total)
      
  return total

def anti_vowel2(text):
  total = ""
  print (text)
  for i in text:
    if i not in ['a','e','i','o','u','A','E','I','O','U']:
      total= total + i
  print (total)
      
  return total
anti_vowel("aaaaaaabaaaaaaaacdeeeeeeeeeeeed")
anti_vowel2("aaaaaaabaaaaaaaacdeeeeeeeeeeeed")
