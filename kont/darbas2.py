k = 0
m = int(input('zmoniu biletas..'))
n = int(input('zmoniu biletas..'))
for i in range (m,n):
    suma = 0
    sd = 1
    sk = i
    for j in range (2):
        x1 = sk % 100
        sk = sk // 10
        sd = sd*x1
        suma = suma + x1
    if suma == sd:
        print(i, end=(' , '))
        k+=1
print(i, end=(' , '))
k+=1
print(f'bus {k} zmoniu')