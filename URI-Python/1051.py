sal = float(input())

if 0 <= sal <= 2000:
    print('Isento')
if 2000 < sal <= 3000:
    sal -= 2000
    print('R$ {:.2f}'.format(sal*0.08))
if 3000 < sal <= 4500:
    sal -= 3000
    print('R$ {:.2f}'.format((sal*0.18) + 1000*0.08))
if 4500 < sal:
    sal -= 4500
    print('R$ {:.2f}'.format(sal*0.28 + 350))
