x = input().split()
a, b, c = x

maiorab = (int(a) + int(b) + abs(int(a) - int(b)))/2
m = (int(c) + int(maiorab) + abs(int(c) - int(maiorab)))/2
m = int(m)
print('{} eh o maior'.format(m))
