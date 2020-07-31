a1 = str(input())
a2 = str(input())
a3 = str(input())

if a1 == 'vertebrado' and a2 == 'ave' and a3 == 'carnivoro':
    a = 'aguia'
if a1 == 'vertebrado' and a2 == 'ave' and a3 == 'onivoro':
    a = 'pomba'
if a1 == 'vertebrado' and a2 == 'mamifero' and a3 == 'onivoro':
    a = 'homem'
if a1 == 'vertebrado' and a2 == 'mamifero' and a3 == 'herbivoro':
    a = 'vaca'
if a1 == 'invertebrado' and a2 == 'inseto' and a3 == 'hematofago':
    a = 'pulga'
if a1 == 'invertebrado' and a2 == 'inseto' and a3 == 'herbivoro':
    a = 'lagarta'
if a1 == 'invertebrado' and a2 == 'anelideo' and a3 == 'hematofago':
    a = 'sanguessuga'
if a1 == 'invertebrado' and a2 == 'anelideo' and a3 == 'onivoro':
    a = 'minhoca'

print(a)
