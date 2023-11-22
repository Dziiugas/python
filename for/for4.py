#petriuko pazymiai ir vidurkis
n = int(input('kiek turi pazymiu...'))
suma = 0
for i in range(1, n+1):
    paz = int(input(f'iveskite {i}-aji pazymi...'))
    if 1<=paz<=10:
        suma = suma + paz
    else:
        print('blogas')
        i = i - 1
vid = suma / n
print(f'jo vidurkis {vid}')
