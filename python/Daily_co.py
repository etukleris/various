import itertools


def set_of_subsets(s):
    final_set = [[]]
    for i in range(len(s)):
        # print(i)
        # final_set.append(s[i])
        for j in range(1, 1+abs(i-len(s))):
            final_set.append(s[i:i+j])
            # print(j, '---------')
    return final_set
# s = [1,2,3,4]
# print(set_of_subsets(s))


def RGB (arr):
    r_count = 0
    out = []
    for i in arr:
        if i == 'G':
            out.insert(r_count,i)
        elif i == 'R':
            out.insert(0, 'R')
            r_count +=1
        else:
            out.append('B')
    return out


# 'better practice':
def RGB_v2(a):
    arr_size = len(a)
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 'R':
            a[lo],a[mid] = a[mid],a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 'G':
            mid = mid + 1
        else:
            a[mid],a[hi] = a[hi],a[mid]
            hi = hi - 1
    return a

#s = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
#print (RGB(s))
#print (RGB_v2(s))


def queen_threatens (N):        #for 2 queens in N*N place
    if N <= 3: return (0)
    elif N == 3: return (2*2*4)
    jd = (N)//2
    print(jd)
    # print(jd)
    total = 0
    starting = N*N - (N-1)*3 -1
    print(starting)
    into = N-1
    for i in range(1, jd+1):
        print(total, starting)
        total += 4*starting*(into)
        into -= 2
        starting -= 2
    if jd == (N-1)/2:
        total += starting
    return total


# print(queen_threatens(6))
# print(queen_threatens(5))

def inversions(arr):
    tmp = []
    l = len(arr)
    for i in range(l-1):
        for j in range(i+1, l):
            if arr[i] > arr[j]:
                tmp.append((arr[i], arr[j]))
    return(tmp)

# x =  [2, 4, 1, 3, 5]
# print(inversions( [2, 4, 1, 3, 5] ))

class Stack:
    def __init__(self, values=None):
        if values:
            self.values = values
        else:
            self.values = []
        # if values.isdigit():
            # self.max = values

    def push(self, val):
        self.values = [val] + self.values


    def pop(self):
        if len(self.values) == 0:
            return None
        tmp = self.values[0]
        self.values = self.values[1:]
        return(tmp)

    def max(self):
        if len(self.values) == 0:
            return None
        return max(self.values)

'''
objboi = Stack()
objboi.push(123)
objboi.push(25)
objboi.push(44)
print(objboi.pop())
print(objboi.pop())
print(objboi.pop())
print(objboi.pop())
print(objboi.pop())
#print(objboi.pop())
#print(objboi.pop())
print(objboi.max())
'''


def can_it_sum(arr,k):

    for i in range(1, len(arr) + 1):
        for combo in itertools.combinations(arr, i):
            if sum(list(combo)) == k:
                return(sorted(list(combo))[::-1])
    return "Nope"


'''s = [5, 5, 5, 5, 9, 2,10,1,10,20]
k = 20
print(can_it_sum(s,k))'''


def stocks_top_gain(arr):
    arr = arr[::-1]
    top = 0
    highest, lowest = 0, 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] - arr[j] > top:
                top = arr[i] - arr[j]
                highest, lowest = arr[i], arr[j]
    return (top, highest, lowest)


def stocks_top_gain2(arr):
    arr = arr[::-1]
    top = 0
    highest, lowest = 0, 0
    for x, i in enumerate(arr, 0):
        # print(x, i)
        m = min(arr[x::])
        # print(m)
        if top < i - m:
            top = i - m
            highest, lowest = i, m
    return (top, highest, lowest)

#s = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 1]
#print (stocks_top_gain(s))
#print (stocks_top_gain2(s))

'''def max_subset(arr):
    max = 0
    holder = []
    for i in range(1, len(arr) + 1):
        for combo in itertools.combinations(arr, i):
            if sum(list(combo)) > max:
                max = sum(list(combo))
                holder = list(combo)

    return holder, max

s = [34, -50, 42, 14, -5, 86]
print(max_subset(s)) # doesn't work like wanted



def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        print(max_so_far, max_ending_here)
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    #print(max_so_far, max_ending_here)
    return max_so_far


a = [34, -50, 42, 14, -5, 86]
print (maxSubArraySum(a, len(a)))

#ended up being the same
def myMyxSubArraySum(arr):
    current_max = 0
    final_max = 0
    for i in arr:
        current_max += i
        print(current_max, final_max)
        if current_max > final_max:
            final_max = current_max
        if current_max < 0:
            current_max = 0
    return final_max

print(myMyxSubArraySum(a))
'''

# import random
# print(random.randint(1,52))


def breakTextUp(arr,k):
    arr=arr.split()
    if len(arr[0]) > k:
        return None
    out = [arr[0]]
    for i in arr[1:]:

        if len(out[-1]) + len(i) +1 <= k :
            out[-1]= out[-1] + " " + i
        else:
            out.append(i)

    return(out)

# s = "the quick hoppotamus jumps loooooong jumps"

# print(breakTextUp(s,10))

def twoSetsWithSameSum(arr):
    total = sum(arr)
    arr= sorted(arr)
    if total%2 != 0 :
        return "Nope"
    half = total//2
    outs = []
    for i in range(1, len(arr) + 1):
        for combo in itertools.combinations(arr, i):
            if sum(list(combo)) == half:
                outs.append(list(combo))

    for i in range(1, len(outs) + 1):
        for combo in itertools.combinations(outs, i):
            #print(list(combo))
            if sorted(sum(list(combo), [])) == arr:
                return("yes")

    return outs

# s = [3, 1, 5, 9, 12]
# print(twoSetsWithSameSum(s))

'''For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 b 0 0 0]
[0 0 b 0 0]
[0 b 0 0 0] #edited
[b 0 0 0 0]'''


def bishops(N,arr):
    board = [[0]*N for _ in range(N)]
    for (i, j) in arr:
        board[i][j] = 'b'
    counter = 0
    for x in arr:
        i, j = x
        up, down = j, j
        down_i = i
        for k in range(j-1, -1, -1):

            i -= 1
            up -= 1
            down_i += 1
            down -=1
            if i >= 0:
                if board[i][up] == 'b':
                    counter += 1
            if down_i < N:
                if board[down_i][down] == 'b':
                    counter += 1
            print((i,up), (down_i,down))
    return (counter)


# s = [(0, 0),(1, 1),(2, 2),(3, 1), (4,0)]
# print(bishops(5,s))

def clockwiseSpirral(arr):
    l = len(arr) * len(arr[0])
    rev = 0
    while l > 0 :
        if rev % 4 == 0:
            for i in arr.pop(0):
                print(i)
                l -= 1
            rev += 1
        elif rev % 4 == 1:
            for i in range(len(arr)):
                print(arr[i].pop())
                l -= 1
            rev += 1
        elif rev % 4 == 2:
            for i in arr.pop()[::-1]:
                print(i)
                l -= 1
            rev += 1

        else:
            for i in range(len(arr)):
                print(arr[i].pop(0))
                l -= 1
            rev += 1
        # print(arr)

'''arr = [
 [1,  2,  3,  4,  5,],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
# clockwiseSpirral(arr)

'''

def wordInListThing(arr, word):
    l = len(arr)
    zipped_arr = list(zip(*arr))
    for i in range(l):
        "".join(arr[i])
        if word == "".join(arr[i]) or word == "".join(zipped_arr[i]):
            return ("Yes, found the word: " + word)

    return ("Nope, word: "+ word +" was not found.")


'''s = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

#word = 'FOAM'
word = 'MASS'
print(wordInListThing(s,word))'''


def highestSubseq(nums):
    l = [1]
    h = 1
    while h < len(nums):
        a = 0
        # print(h)
        for i in range(h):
            print(i)
            if nums[i] < nums[h]:
                print(nums[i], nums[h])
                if l[i] > a:
                    a = l[i]
        l.append(a+1)
        h += 1
    return l

    '''Given an array of numbers, find the length of the longest
     increasing subsequence in the array. The subsequence does 
     not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.'''

# a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# print(highestSubseq(a))
# print(a[-2])


def  downRightBoard(N):
    if N <= 1:
        return 0
    x = [1 for _ in range(N-1)]
    depth = 0
    while depth < N-1:
        tmp_sum = x[0]*2
        x[0] = tmp_sum
        for i in range(1, len(x[1:]) + 1):
            x[i] += x[i-1]
        x = x[1:]
        depth += 1
    return tmp_sum

# print(downRightBoard(7))


'''def notOverlapping(arr):
    arr = sorted(arr)
    out = [arr[0]]
    for i in arr[1:]:
        if i[0] >= out[-1][0] and i[1] <= out[-1][1]:
            continue
        elif i[0]>out[-1][1]:
            out.append(i)

    return out
'''


def notOverlapping(arr):
    arr = sorted(arr)
    out = [arr[0]]
    # print(out)
    # print(out[-1][1])
    for i in arr[1:]:
        #print(i[0])
        if i[0] <= out[-1][1] and i[1] >= out[-1][1]:
            # out[-1][1]=i[1]
            out[-1] = (out[-1][0],i[1])
            print(out)
        elif i[0] > out[-1][1]:

            out.append(i)

    #(1,10), (11,19) doesn't mean (1,19)

    return out

# a = [(1, 3), (5, 8), (4, 10),(10,19), (20, 25), (1,4)]
# a = [(1, 3), (1,4)], (4, 10), (5, 8), (20, 25)
# b = [ [6,8], [1,9], [2,4], [4,7] ]

# print(notOverlapping(a))


def division(a, b):
    out = 0
    while a >= b:
        a -= b
        out += 1
    return (out)

# print(division(500,2))


'''
functions = []
# makeFun= lambda x: x

for i in range(10):
    functions.append( lambda x = i:x )
print(i)'''


def target_game(amounts):
    prev, total = 0, 0
    for amount in amounts:
        prev,total = total,max(total, prev + amount)
        print(prev,total)
    return total

#print(target_game([26, 54, 36, 35, 63, 58, 31, 80, 59, 61, 34, 54, 62, 73, 89, 7, 98, 91, 78]))


def hops_to_take(arr):
    hopNumber = arr[0]
    index = hopNumber
    l = len(arr) -1
    while True:
        # print(hopNumber,index)

        try:
            hopNumber = arr[index]
        except IndexError:
            return False
        else:
            if hopNumber == 0:
                if index == l:
                    return True
                else:
                    return False
            else:
                index += hopNumber



'''a = [2, 0, 1, 0]
b = [1, 1, 0, 1]
c = [4,0,0,0,2,0,4,0,0,0,2,0,4,0,0,0,2,0,4,0,0,0,2,0,4,0,0,0,2,0,0]
print(hops_to_take(a))
print(hops_to_take(b))
print(hops_to_take(c))'''


def can_it_be_shifted(A, B):

    shift = lambda x, y: chr(ord(x) + y)  if ((ord(x.lower()) + y) >= 97 and (ord(x.lower()) + y) <= 122) else (
                chr(ord(x) + y - 25))

    for i in range(25):
        stringHolder = ''
        for j in A:
            stringHolder += shift(j,i)
        print(stringHolder)
        if stringHolder == B:
            return True
    return False

    #return (list(map(shift,[0])))
    # for i in range(36):


#a,b = 'wxyz', 'bcde'
#print(can_it_be_shifted(a,b))


def reversed_with_delimiters(str):
    words = []
    delimiters = []
    word = ''
    for i in str:
        #print(i)
        if i not in ' /\*:;?!@#$%^&()-_=~`':
            word += i
        else:
            words.append(word)
            word = ''
            delimiters.append(i)
    words.append(word)
    output = ''
    print(words,delimiters)
    for i in words[1:][::-1]:
        output+= i + delimiters.pop(0)
    output += words[0]
    return (output)

'''s  = 'hello/world:here'
x = 'hello/world:here/'
z = "hello//world:here"
print(reversed_with_delimiters(s) == 'here/world:hello')
print(reversed_with_delimiters(x) == '/here:world/hello')
print(reversed_with_delimiters(z) == 'here/world/:hello')'''

'''def can_polindr(s,k):

    for i in range(len(s)):
        for j in range(k):
            tmp = s[:i] + s[i+1:]
            l=len(tmp)//2
            if tmp[:l] == tmp[-1:-l-1:-1]:
                return (tmp, True)
    return (False)

'''
'''

def can_polindr(s,k):
    l = len(s) // 2
    if s[:l] == s[-1:-l-1:-1]:
        return (True,s,'deleted letters = ', k)
    else:
        depth = k-1
        if depth < 0:
            return (False)
        else:
            for i in range(len(s)):
                tmp = s[:i] + s[i+1:]
                x = can_polindr(tmp,depth)
                if x:
                    return (x)
    return (False)'''


def can_polindr(s,k):
    #print(s)
    l = len(s) // 2
    if s[:l] == s[-1:-l-1:-1]:
        return (s,'left letters for removal = ', k)
    else:
        depth = k-1
        if depth < 0:
            return (False)
        else:
            for i in range(len(s)):
                tmp = s[:i] + s[i+1:]
                l = len(tmp) // 2
                if tmp[:l] == tmp[-1:-l - 1:-1]:
                    return(tmp,'left letters for removal = ', depth)


            else:
                for i in range(len(s)):
                    tmp = s[:i] + s[i + 1:]
                    x = can_polindr(tmp, depth)
                    if x:
                        return (x)
    return (False)


#x = "for racecar rof r"

#print (can_polindr(x,9))


def largest_path_down(arr):
    cols = len(arr)
    rows = len(arr[0])
    res = 0
    for i in range(1,cols):
        for j in range(rows):

            if (j>0 and j+1<rows):
                print(arr[i - 1][j])
                arr[i][j]+= max(arr[i-1][j-1:j+2])

            elif (j+1<rows):
                arr[i][j] += max(arr[i-1][j:j+2])
            elif(j>0):
                arr[i][j] += max(arr[i-1][j-1:j+1])

        print(arr)

    return (max(arr[-1]))


'''x =    [[0, 3, 1, 1],
        [3, 0, 0, 4],
        [100, 5, 3, 99]]

print(largest_path_down(x))'''


def nearest_points(arr,k):
    if len(arr)<=k:
        return(arr)
    points = []
    for i in arr:
        points.append([(i[0]**2+i[1])**(1/2),i] )
    return list(x[1] for x in sorted(points)[0:k])
#x = [(0, 0), (5, 4), (3, 1),(2,2), (10,3),(5,5)]
#print(nearest_points(x,5))


def flatten_nested_dicts(dic, parent=''):

    out_dict = {}
    #print (dic.items())
    for rkey,val in dic.items():
        key = parent + rkey
        if isinstance(val,dict):
            out_dict.update(flatten_nested_dicts(val,key+'.'))
        else:
            out_dict[key]=val
    return out_dict

'''
x = {
    "key": 3,
    "james":{"jeremy": 3, "May":{"flies":3}},
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8,
            "box": 7
        }
    }
}'''
#print(x.items())
#print(flatten_nested_dicts(x))


def rotate_n_by_n(arr):
    return(list(zip(*arr[::-1])))

'''numbers =[[1, 2, 3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]

print(*numbers[::-1])
print(rotate_n_by_n(numbers))
'''

def palindrome_least_split(s):
    out = []
    l = len(s)
    total_l = 0
    z = 0
    while total_l < l:
        i = len(s)
        while i>0:
            #print(i)
            test_string = s[0:i]
            #print(out)
            #print(test_string)
            test_len = len(test_string)
            y = test_len//2
            #print(test_string[:y],test_string[y:][::-1])
            if test_len%2 > 0:
                if test_string[:y+1]==test_string[y:][::-1]:
                   # print('111111111111111')
                    out.append(test_string)
                    total_l += test_len
                    s = s[i:]
                    i-=test_len
                else: i-=1
            elif test_string[:y]==test_string[y:][::-1]:
                #print('22222222222222222222')
                out.append(test_string)
                total_l += test_len
                s = s[i:]
                i -= test_len

            else: i-=1
    return (out)

#st = 'racecarannakayak'
#print(palindrome_least_split(st))


'''
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(arr):
            print(arr)
        flist.append(print_i(i))

    return flist

functions = make_functions()
for f in functions:
    try: f()
    except TypeError :
        pass


def stockBuySell(arr):
    n = len(arr)
    if n == 1:
        return 0
    count = 0
    sol=[]

    i = 0
    while (i<n-1):

        while ((i<n-1) and (arr[i+1]<=arr[i])):
            i+=1
        if (i==n-1):
            break

        interv = []
        interv.append(i+1)

        while((i<n) and (arr[i] >= arr[i-1])):
            i+=1

        interv.append(i-1)
        count+=1

    print (interv)


stockBuySell([1, 6, 2,5, 4, 10])

'''


def stocks_gains_with_fees(arr,fee):
    sum = 0
    n = len(arr)
    current = None
    for i in range(0,n):
        if not current or current> arr[i]:

            current = arr[i]
        else:
            sum_current = arr[i]-current-fee
            print(current, arr[i], sum_current)
            if  sum_current> 0:
                sum +=sum_current
                current = None

        print (current,sum)
    return sum


#stocks= [1, 3, 7, 8, 4, 10]
#print(stocks_gains_with_fees(stocks,2))

def doesEveryElementModToZero(arr):
    if len(arr) <=1:
        return True
    for i in arr:
        for j in arr:
            if i%j==0 or j%i==0:
                pass
            else:
                return False
    return True
def largestSubsetElements1(arr): #that every pair of elements i%j or j%i == 0
    largest = []
    i = 0
    j=2
    l = len(arr)
    while i<l:
        if doesEveryElementModToZero(arr[i:i+j]):
            print(arr[i:i+j])

            if len(arr[i:i+j]) > len(largest):
                largest = arr[i:i+j]
            j += 1
        else:
            i+=1
        if i==l-1 or arr==largest:
            break
        #print(i)
    return largest


s1 = [3, 5, 10, 20,100,300, 21]
s2 = [1, 3, 6, 24,144]
s3 = []
#s2 = [5,10,20]
#print(doesEveryElementModToZero(s2))
print(largestSubsetElements1(s2))