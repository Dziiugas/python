# ivedamas bet koks skaicius rasti to skaiciaus skaimenu suma...

sk = int(input('sk = '))
suma = 0
kopija = sk
while sk > 0:
    x1 = sk % 10
    sk = sk // 10 # sk //= 10
    suma += x1
print(f'skaiciaus {kopija} skaitmenu suma = {suma}')
