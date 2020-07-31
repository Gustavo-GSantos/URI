d1 = int(input())
ddd = [61, 71, 11, 21, 32, 19, 27, 31]
ddds = {61:'Brasilia', 71:'Salvador', 11:'Sao Paulo', 21:'Rio de Janeiro', 32:'Juiz de Fora', 19:'Campinas', 27:'Vitoria', 31:'Belo Horizonte'}
if d1 not in ddd:
    print('DDD nao cadastrado')
else:
    print(ddds[d1])
