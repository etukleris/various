x = "#----"
#x[1] = '#'
f = 10
for i in range(1,f):
  #for j in range(len(x),-1,-1):
  for j in range(1,f):
    x = '-'*(i-j) + '#' #+ '-'*(j-i)
    print(x)
  print('~~~~~~~~~~')
  
