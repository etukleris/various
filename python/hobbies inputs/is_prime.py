def is_prime(x):
  if x > 1:
    for n in range(2,x-1):
      #if x/n == int(x/n):
      if x%n == 0:
        print (x%n)
        return False
    else:
      print (x)
      return True
  else:
    return False
"""
  for n in range(2, x-1):
      print (x/n)"""

while True:
  number = int(input("Enter prime? number"))
  print (is_prime(number))
  inp = input("Should we go on? Y/N")
  if inp == "N" or inp == "n":
      print ("Too Bad, bye!")
      break

