m = [5, 8, 9, 7, 9, 4, -1]
print(m)
print(type(m))
use =['jonas',18, 1.78, True,[8, 9, 10, 5, 7]]
print(use[0])
print(use[4])
print(use[4][1])
suma = 0
kiek = 0
for i in m:
    suma += i
    kiek += 1
print(suma)
print(kiek)
kiekis = len(m)
print(kiekis)
for i in range(len(m)):
    print(f'm[{i}] = {m[i]}')