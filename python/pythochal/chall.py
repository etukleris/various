import re
word = open('imp.txt', mode='r')
answer = ""
for c in word.read():
    if re.match("[a-zA-Z]", c):
        answer += c
print (answer)
