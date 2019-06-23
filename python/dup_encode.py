from collections import Counter as count
def duplicate_encode(word):
    out = ''
    word = list(word)
    counts = {i:word.count(i) for i in word}
    for i in word:
        print(i)
        if counts.get(i) > 1:
            out += '('
        else:
            out += ')'
    print(out)

duplicate_encode("james is")
#james = 'thommas is here'
#james = list(james)
#my_dict = {i:james.count(i) for i in james}
#print(my_dict.get(' '))