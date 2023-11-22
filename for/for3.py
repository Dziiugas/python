#atspausdinti visus skaicius nuo 1 iki n. jei patenka 13 jo nespausdinti
n = int(input('n=...'))
for i in range (1,n):
    if i == 13:
        continue
    print(i, end=(' , '))
else :
    print('\nciklas uzbaigtas')
print('kiti skainai....')