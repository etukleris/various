from collections import Counter
scrap = 0
total = []
inp = ""
while True:
    try:
        inp = input("scraps from phyla ('done' to exit): ")
        total.append(int(inp))
    except ValueError:
        if inp == "done":
            break
        else:
            print("that wasn't a number, reenter")
    else:
       # total += scrap
       # print (total)
        for x in Counter(total).keys():
            print(x,' ',Counter(total)[x], str(100 * (Counter(total)[x]/len(total)))[0:5] + '%', sep=' ')
