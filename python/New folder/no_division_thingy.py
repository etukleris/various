"""from datetime import datetime
start=datetime.now()



f = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
z = []
def mults(l):
  x=1
  for i in l:
    x=x*i
  return x
print(mults(f[0:1])*mults(f[1:]))
for i in range(len(f)):
  z.append(mults(f[:i]) * mults(f[1+i:]))
  #print(z)
print(z)


#Statements

print (datetime.now()-start)
"""
nums = [1,2,3,4,5]
result = [1]*5
t1 =  [1]*5
t2 =  [1]*5
t1[0]=1;
t2[4]=1;

#scan from left to right
for i in range(len(nums)-1):
  print(t1)
  print(nums)
  t1[i+1] = nums[i] * t1[i]




#scan from right to left
for i in range(len(nums)-1,0,-1):
  t2[i-1] = t2[i] * nums[i]

#multiply
for i in range(len(nums)):
  result[i] = t1[i] * t2[i]

print (t1)
print(t2)
print(result)


