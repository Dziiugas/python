# ivedamas skaicius 12, atspausdinti jo daliklius
# 1 2 3 4 6 12 ju yra 6
# 1 13 ju yra 2
n = int(input('skaicius..'))
sk = 1
suma = 0
while n >= sk:
    
    if n % sk == 0:
     print(sk, end=(' , '))
     suma = suma + 1
    sk = sk + 1
print('ju yra ', suma)


