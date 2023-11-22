#petriuko pazymiai ir vidurkis
def ivedimas (nr):
    paz = int(input(f'iveskite{nr}-aji pazymi...'))
    if 1<=paz<=10:
        return paz
    else:
        print('blogas pazymys..')
        return ivedimas(nr)


n = int(input('kiek turi pazymiu...'))
#did = kelintas = 0
for i in range(1, n+1):
    p = ivedimas(i)
    if i == 1:
        did = p
        kelintas = i
    elif did < p:
        did = p
        kelintas = i

print(f'jo didziausias pazymys  {did}. jis yra {kelintas}')
