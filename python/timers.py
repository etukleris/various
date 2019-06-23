#For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
classes = [(900, 910), (940, 1200), (950, 1120),(1100, 1130), (1500, 1900), (1800, 2000)]
started = []
for x,i in classes:
    started+= [(x,'started'),(i,'ended')]
started = sorted(started)
needed = 0
ongoing = 0
print(started)
for i in range(len(started)):
    if started[i][1] == 'started':
        ongoing +=1
        #print(started[i][0])
        if ongoing > needed:
            needed = ongoing
    else:
        ongoing -=1
print (needed)

