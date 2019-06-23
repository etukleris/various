'''Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:'''


def median(arr):
    for i in range(len(arr)):
        ongoing = sorted(arr[:i + 1])
        if i%2==0:

            l = len(ongoing)
            print(ongoing[(l//2)])
        else:
            x = (ongoing[(l//2)]+ongoing[(l//2)+1])/2
            if x.is_integer():
                print(int(x))
            else:
                print(x)

s = [2, 1, 5, 7, 2, 0, 5]
median(s)