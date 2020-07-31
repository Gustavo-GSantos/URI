nums = input().split()
hi, mi, hf, mf = nums
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if hi < hf:
    h = hf - hi
    if mf > mi:
        m = mf - mi
    if mi > mf:
        h -= 1
        m = 60 - (mi - mf)
    if mi == mf:
        m = 0
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h -= 1
        m = 60 - (mi - mf)
    if mi == mf:
        m = 0
if hi == hf:
    if mi < mf:
        h = 0
        m = mf - mi
    if mi > mf:
        h = 23
        m = 60 - (mi - mf)
    if mi == mf:
        h = 24
        m = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))
