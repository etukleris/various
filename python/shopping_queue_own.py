def queue_time(arr,n):
    l = [0]*n
    for i in arr:
        l[l.index(min(l))] += i

    return max(l)



print(queue_time([5, 3, 4, 12, 7, 9, 10, 3, 8], 3))
