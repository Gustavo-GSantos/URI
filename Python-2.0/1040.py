n = input().split()
n1, n2, n3, n4 = n
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media1 = (n1*2 + n2*3 + n3*4 + n4*1) / 10
print('Media: {:.1f}'.format(media1))
if media1 >= 7:
    print('Aluno aprovado.')
elif media1 < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nf = float(input())
    print('Nota do exame: {:.1f}'.format(nf))
    media2 = (media1+nf)/2
    if media2 >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media2))
