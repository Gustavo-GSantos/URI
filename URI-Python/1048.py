sal = float(input())

if 0 <= sal <= 400:
    print('Novo salario: {:.2f}'.format(sal + (sal*0.15)))
    print('Reajuste ganho: {:.2f}'.format(sal*0.15))
    print('Em percentual: 15 %')
if 400 < sal <= 800:
    print('Novo salario: {:.2f}'.format(sal + (sal*0.12)))
    print('Reajuste ganho: {:.2f}'.format(sal*0.12))
    print('Em percentual: 12 %')
if 800 < sal <= 1200:
    print('Novo salario: {:.2f}'.format(sal + (sal*0.10)))
    print('Reajuste ganho: {:.2f}'.format(sal*0.10))
    print('Em percentual: 10 %')
if 1200 < sal <= 2000:
    print('Novo salario: {:.2f}'.format(sal + (sal*0.07)))
    print('Reajuste ganho: {:.2f}'.format(sal*0.07))
    print('Em percentual: 7 %')
if 2000 < sal:
    print('Novo salario: {:.2f}'.format(sal + (sal*0.04)))
    print('Reajuste ganho: {:.2f}'.format(sal*0.04))
    print('Em percentual: 4 %')
