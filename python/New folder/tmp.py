#plchld = input()
#b = reversed(sorted(input().split()))
    b = [int(x) for x in input().split()]
    b.sort(reverse=True)
    n = [int(x) for x in b]
    print (n)
    toppest = n[0]
    for i in n:  
      if toppest > i:
        toppest = i
        break
    print (toppest)
