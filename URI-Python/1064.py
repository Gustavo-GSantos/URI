p = 0
s = 0
for c in range(6):
    n1 = float(input())
    if n1 > 0:
        p += 1
        s += n1
print('{} valores positivos'.format(p))
print('{:.1f}'.format(s/p))
