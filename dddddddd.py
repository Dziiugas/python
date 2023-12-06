def ivedimas(txt):
    sk = int(input(txt + '='))
    return sk
def rasom1(txt):
    with open('data6.txt','a',encoding='utf-8') as f:
        f.write(txt + '\n')
kiek = int(input('kiek skaiciu norime sumuoti'))
rasom1(f'vartotojas ives {kiek} skaiciu')
sum = 0
list1 = []
for i in range(1, kiek+1):
    sk = ivedimas(f'sk{1} ')
    list1.append(sk)
    rasom1(f'sk{i} = {sk}')
    sum += sk
rasom1(f'skaiciu suma = {sum}')