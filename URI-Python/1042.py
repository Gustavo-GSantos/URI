nums = input().split()
a, b, c = nums
lista = []
lista.append(int(a))
lista.append(int(b))
lista.append(int(c))
s = sorted(lista)

for i in range(3):
    print(s[i])
print()
for i2 in range(3):
    print(lista[i2])
