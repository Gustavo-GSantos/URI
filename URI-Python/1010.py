p1 = input().split()
ca, qa, va = p1
p2 = input().split()
cb, qb, vb = p2

t = float(int(qa)*float(va) + int(qb)*float(vb))
print('VALOR A PAGAR: R$ {:.2f}'.format(t))
