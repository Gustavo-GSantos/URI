e = input().split()
co, qua = e
co = int(co)
qua = int(qua)

lista = [0, 4.00, 4.50, 5.00, 2.00, 1.50]

tot = lista[co] * qua
print('Total: R$ {:.2f}'.format(tot))
