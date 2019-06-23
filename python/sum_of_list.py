def sumItUp(args):
    sum = 0

    for i in args:
        #print(i)
        if str(i).isdigit():
            sum+=i
        else:
            sum+=sumItUp(i)
    return(sum)

a=[1,2,3,4,[2,3],[1,8,[2,2]]]
print(sumItUp(a))