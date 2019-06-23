def letter_swapper(s):
    if len(s) > 4:
        first2 = s[0:2]
        last2 = s[-2:]
        fixed_str = s[2:-2]
        return last2 + fixed_str + first2
    else:
        return (s)
    
print (letter_swapper("Complete"))
print (letter_swapper("No"))
print (letter_swapper("Hello World"))