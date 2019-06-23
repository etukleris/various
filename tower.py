def tower_builder(n, block_size):
    w, h = block_size
    first = w
    l = (w*(n-1))
    print(l)
    tower = []
    #tower = [' '*l + '*'*i + ' '*l for i in range(1,n*2,2)]
    for i in range(1,n+1):
        for _ in range(h):
            tower.append (' '*l + '*'*first + ' '*l)
        first = first + 2*w
        l -= w
    return (tower)
print(tower_builder(6,(2, 1)))
print(tower_builder(6,(2, 1)) == [
  '          **          ',
  '        ******        ',
  '      **********      ',
  '    **************    ',
  '  ******************  ',
  '**********************'
])