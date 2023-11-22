# ivedamas bet koks skaicius rasti to skaiciaus skaimenu suma...

def atvir (skaicius):
    atv = 0
    while skaicius > 0:
        x1 = skaicius % 10
        skaicius //= 10
        atv = atv * 10 + x1
    return atv


sk = int(input('sk = '))
sumakita = atvir(sk)
print(f'skaiciaus {sk} skaitmenu atvir = {sumakita}')
