#simple program to find the longest word in sentence


#take a string/sentence, return list of words
def getOnlyWords(sentence):
    words=[]
    word = ""
    for i in sentence:
        if i.isalpha():
            word += i
        else:
            if word !="":
                words.append(word)
            word = ""
    if word != "":
        words.append(word)
    return words


def getLongestWord(sentence):
    if not sentence:
        return "Sentence is empty"
    else:
        longest = ""
        for i in getOnlyWords(sentence):
            if len(i) > len(longest):
                longest = i
        if not longest:
            return "There were no words in the sentence"
        else:
            return longest

print(getLongestWord("asd12asd2323sadasdasd12sd12verylongwordindeed"))
print(getLongestWord("12345"))