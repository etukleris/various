def shop_que(arr,n):
    l = len(arr)
    if l == 0: return (0)
    elif n == 1: return (sum(arr))
    out = 0
    while len(arr) > n:
        mini = min(arr[0:n])
        out += mini
        arr.pop(arr[0:n].index(mini))
        for j in range(n-1):
            arr[j] -= mini
    out += max(arr)
    return (out)
print(shop_que([5,3,4,12,7,9,10,3,8],3))