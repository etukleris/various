def stamps(n): # my code
    return (n//5, (n%5)//2, (n%5)%2)

print (stamps(8))
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp #<- results that i am supposed to get
print (stamps(5))
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print (stamps(29))
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print (stamps(0))
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps