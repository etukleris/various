l = [1, 5, 2, 6, 3, 1, 24, 7]
k = 3
out = []
for i in range(len(l)-k+1):
  out.append(max(l[i:i+k]))
print(out)
