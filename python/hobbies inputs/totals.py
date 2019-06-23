def product(prods):
  total = 1
  for i in range(len(prods)):
    total *= prods[i]
  print ("prods: "+ str(prods))
  print ("total: "+ str(total))
  return total
