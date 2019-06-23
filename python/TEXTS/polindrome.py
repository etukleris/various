import string
path = 'C:/Users/Edgaras/Desktop/python/TEXTS/polindromes.txt'
#st = input("Enter potential Palindrome: ")
#my_file =
lines = 0
with open(path, encoding="utf8") as f:
    for line in f:
        istrue = False
        lines +=1
        stst = ""
        for i in line:
            if i in string.ascii_letters:
                stst += i.lower()
        #halfpoint:
        #print("length is" +str(len(stst)))

        hp = len(stst)//2
        #print("length half is" +str(hp))

        #print ("first half =" + stst[0:hp])
        #print ("middle =" + stst[hp])
        #print ("second half =" + stst[:hp:-1])
        if (len(stst)%2 == 0):
            istrue = (stst[0:hp] == stst[:hp-1:-1])
        else:
            istrue = (stst[0:hp] == stst[:hp:-1])
        if not istrue: #checking if this isn't a palindrome
            print (line[:len(line)-1] + " ^^^^^ found on lane: " + str(lines))
#my_file.close()
#print(lines)
"""
#convert whole text to just strings:
stst = ""
for i in st:
    if i in string.ascii_letters:
        stst += i.lower()
#halfpoint:
#print("length is" +str(len(stst)))

hp = len(stst)//2
print("length half is" +str(hp))

#print ("first half =" + stst[0:hp])
#print ("middle =" + stst[hp])
#print ("second half =" + stst[:hp:-1])
if (len(stst)%2 == 0):
    print(stst[0:hp] == stst[:hp-1:-1])
else:
    print(stst[0:hp] == stst[:hp:-1])
"""
