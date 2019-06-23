def chance(a,b,c,d):
    currentKC = c
    thr = (currentKC // b) + 1
    dropch = 1 - ((a-thr)/a)**d
    return (dropch)
    #1 - ((2498)/2500)**453
"""base = int(input("Base drop rate: "))
thresh = int(input("Threshold: "))
kc = int(input("Your current KC: "))
amount = int(input("Kills: "))

print (chance(base, thresh, kc, amount))
"""
base = 2500
thresh = 500
kc = 547
kills = 0
while (True):
    kills += 1
    dropch = 1 - ((base-(kc//thresh)-1)/base)**kills
    if dropch >= 0.50:
        print (kills)
        break
        
