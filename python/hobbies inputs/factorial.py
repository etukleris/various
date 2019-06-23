def factorial(x):
  total = x
  while x > 0:
    x-=1
    if x == 0:
      break
    else:
      total *= x
  return total

a = True
while a == True:
  number = int(input("Enter factorial number"))
  print (factorial(number))
  inp = input("Should we go on? Y/N")
  if inp == "Y":
      a = True
  elif inp == "N":
      print ("Too Bad, bye!")
      a = False
  else:
      print ("Some random input? Sorry, shutting down")
      a = False
