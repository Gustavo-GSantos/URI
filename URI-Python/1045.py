nums = input().split()
n1, n2, n3 = nums
lista = [float(n1), float(n2), float(n3)]
s = sorted(lista, reverse = True)
a = s[0]
b = s[1]
c = s[2]

if a >= b+c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2 + c**2):
        print('TRIANGULO RETANGULO')
    elif a**2 > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < (b**2 + c**2):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b != c or a == c != b or b == c != a:
        print('TRIANGULO ISOSCELES')
