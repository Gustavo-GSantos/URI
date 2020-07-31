n = int(input())
print(n)
for c in [100, 50, 20, 10, 5, 2, 1]:
    q = n // c
    n = n % c
    if q >= 0:
        print('{} nota(s) de R$ {},00'.format(q, c))
