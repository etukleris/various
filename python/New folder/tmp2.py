a = 5
b = set("3 6 5 4".split())
c = 4
d = set("2 7 9 6".split())
q = b.difference(d)
p = d.difference(b)

print ('\n'.join(sorted(q.union(p))))
