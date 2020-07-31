nums = input().split()
a, b, c = nums
a = float(a)
b = float(b)
c = float(c)

if a < b+c and b < a+c and c < a+b:
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {}'.format(((a+b)/2)*c))
