st = input("Enter stringerooni: ")
count = 0
vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
#print (vowels)
for i in st:
    if i in (vowels.keys()):
        count+=1
        print("found one!")
        vowels[i] += 1
print ('Input string = '+  st)
print ("Total vowels: " + str(count))
for i in vowels.keys():
    print('Letter ' + i + ' appears ' + str(vowels[i]) + ' times')
#print (vowels)
