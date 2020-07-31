x = int(input())

a = x // 365
x = x % 365

m = x // 30
x = x % 30

d = x

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))
