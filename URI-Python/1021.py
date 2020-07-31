valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    q1 = int(valor / nota)
    print('{:.0f} nota(s) de R$ {:.2f}'.format(q1, nota))
    valor -= q1 * nota
print('MOEDAS:')
for moeda in moedas:
    q2 = int(round(valor, 2) / moeda)
    print('{:.0f} moeda(s) de R$ {:.2f}'.format(q2, moeda))
    valor -= q2 * moeda
