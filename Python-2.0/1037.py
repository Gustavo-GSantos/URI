n1 = float(input())

if n1 < 0 or n1 > 100:
    print('Fora de intervalo')
elif 0 <= n1 <= 25:
    print('Intervalo [0,25]')
elif 25 < n1 <= 50:
    print('Intervalo (25,50]')
elif 50 < n1 <= 75:
    print('Intervalo (50,75]')
elif 75 < n1 <= 100:
    print('Intervalo (75,100]')
