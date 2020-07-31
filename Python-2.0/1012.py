r = input().split()
a, b, c = r

tri = float(a) * float(c) / 2
cir = (float(c)**2) * 3.14159
tra = ((float(a)+float(b)) * float(c)) / 2
qua = float(b)**2
ret = float(a) * float(b)

print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(cir))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))
