numbers = [1,2,3,4,5]
toL = [1]*len(numbers)
toR = [1]*len(numbers)

for i in range(1,len(numbers)-1):
  toR[i+1] = toR[i] * numbers[i]
print(toR)

for i in range(len(numbers)-1,0,-1):
  toL[i-1] = toL[i] * numbers[i]
print (toL)

for i in range(len(numbers)):
  numbers[i] = toL[i] * toR[i]
print (numbers)
