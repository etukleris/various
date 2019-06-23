intList = [1, 4, 45, 6, 10, -8]
K = 16
for i in range(len(intList)):
  for j in range(i+1,len(intList)):
    if (intList[i] + intList[j] == K):
      print('found your solution', intList[i], intList[j], sep=' ')
      break
