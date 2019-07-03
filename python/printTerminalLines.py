import os, time
''' tryin out single line character print
before moving on to multi line characters
like the one below '''
wordDict= {
" ": ["     ",
      "     ",
      "     ",
      "     ",
      "     "],
"a": ["  █  ",
      " █ █ ",
      "█   █",
      "█████",
      "█   █"],
"b": ["████ ",
      "█   █",
      "████ ",
      "█   █",
      "████ "],
"c": [" ████",
      "█    ",
      "█    ",
      "█    ",
      " ████"]
}


def pushLeft(arg):
    return arg[1:]+" "


def singleLineScrollerPrint(word):
    print('hi')
    l = len(word)
    word=  " "*l + word
    for i in range(l*2+1):

        print("\r{0}".format(word[:l]), end='')
        word = pushLeft(word)
        time.sleep(0.5)


#singleLineScrollerPrint("Hello world")

'''Multiline print function uses predefined letters as arrays of string, appends them
to empty string, then pushes every single line left and prints the result.
Scrolling effect is done via clearing the terminal/command line screen.
Could probably find some plugin that would move cursor back N lines to print over them
instead of clearing the screen. Only has 3 letters in the dict but can be easily
added more if needed, also could use a check for letters that are not in the library
to either cause error, print another symbol (like "?") or simply ignore it'''
def multiLineScrollerPrint(words):
    l = 80
    word = [" "*l]*5
    wordsLen = len(words)
    tmpItr= 0
    for letter in words:
        for i in range(5):
            word[i] +=  wordDict[letter][i]
            if tmpItr<wordsLen: word[i] +=" "
        tmpItr +=1

    for i in range(len(word[i])):
        os.system('cls' if os.name == 'nt' else 'clear')
        for j in range(5):
            print(word[j][:l])
            word[j] = pushLeft(word[j])

        time.sleep(0.2)
print (wordDict["a"][0])
multiLineScrollerPrint("a bcba")