nums = input().split()
i, f = nums
i = int(i)
f = int(f)

if i >= f:
    r = (24 - i) + f
elif i < f:
    r = f - i

print('O JOGO DUROU {} HORA(S)'.format(r))
