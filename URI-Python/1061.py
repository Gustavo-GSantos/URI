dia_i = input().split()
hora_i = input().split()
dia_f = input().split()
hora_f = input().split()
di, df = int(dia_i[1]), int(dia_f[1])
hi, mi, si = int(hora_i[0]), int(hora_i[2]), int(hora_i[4])
hf, mf, sf = int(hora_f[0]), int(hora_f[2]), int(hora_f[4])

ms = 60
hs = ms * 60
ds = hs * 24
i = si + mi*ms + hi*hs + di*ds
f = sf + mf*ms + hf*hs + df*ds

if i < f:
    tot = f - i
    dias = int(tot/ds)
    tot = tot % ds
    horas = int(tot/hs)
    tot = tot % hs
    minutos = int(tot/ms)
    tot = tot % ms
    segundos = tot
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
