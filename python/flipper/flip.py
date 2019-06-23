import time
start_time = time.time()
#amount = input()

fabbits = [0]*96
fabbits[2] = 4
mabbits = [0]*96
mabbits[2] = 2
month = 0
dead = 0
while True:
  month +=1
  #print("Month", i, ":", fabbits, sep=" ")
  fertil = sum(fabbits[4:len(fabbits)+1])
  fabbits = [fertil *9] + fabbits[0:96]
  mabbits = [fertil *5] + mabbits[0:96]
  total = sum(mabbits) + sum(fabbits)
  dead = fabbits.pop() + mabbits.pop() + dead
  #print("month",month,total, "dead:",dead, sep=" ")

  if total >= 15000000000:
    break
print("month",month,total, "dead:",dead, sep=" ")
print("--- %s seconds ---" % (time.time() - start_time))
