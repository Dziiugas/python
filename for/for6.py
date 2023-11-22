# atspausdinti visus penkiazenklius skaicius, kuriu skaitmenu suma = skaitmenu sandauga
# suskaiciuoti kiek ju yra...
# 10000 iki 99999
kiek = 0

for i in range(10000,100000):
    suma = 0
    sd = 1
    sk = i
    for j in range (5):
        x1 = sk % 10
        sk = sk // 10
    #x1 = i // 10000
    #x2 = i // 1000 % 10
    #x3 = i // 100 % 10
    #x4 = i // 10 % 10
    #x5 = i  % 10
        sd = sd*x1
        suma = suma + x1
    if suma == sd:
        print(i, end=(' , '))
        kiek+=1
print(f'ju yra {kiek}')

