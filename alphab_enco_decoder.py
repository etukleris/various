def enco(s):
    out = ""
    count = 1
    current = s[0]
    for i in range(1,len(s)):
        if s[i] == current:
            count += 1
        else:
            out = out + str(count) + current
            current = s[i]

            count = 1
    out = out + str(count) + current
    return (out)

def deco(s):
    numberino = ''
    out= ''
    for i in s:
        if i.isdigit():
            numberino += str(i)
        else:
            out += i*int(numberino)
            numberino = ''
    return(out)


s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#4A3B2C1D2A
print (enco(s))
print (deco(enco(s))==s)