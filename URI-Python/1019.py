t = int(input())
s = 0
h = 0
while True:
    m = t // 60
    t = t % 60
    if m >= 60:
        h = m // 60
        m = m % 60
    if t < 60:
        s = t
        t = 0
    if t == 0:
        break
print('{}:{}:{}'.format(h, m, s))
