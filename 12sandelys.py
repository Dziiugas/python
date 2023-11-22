# sandelyje turime p prekiu. Jas reikia supakuoti i dvieju tipu dezes d , m
# i didele deze telpa d prekiu, o i maza m prekiu
#kiek reikes dideliu deziu ir kiek reikes mazu deziu ir kiek prekiu nesupakuotu
# pvz. p = 259, d=10, m=5
# ats dideliu reikes 25, mazu 1 ir liks nesupakuota 4 prekes
p = int(input('Iveskite kiek yra P...'))
d = int(input('Iveskite kiek yra dideliu deziu...'))
m = int(input('iveskite kiek yra mazu deziu...'))
kiekD = p // d
likutis = p % d
kiekM = likutis // m
kiekliko = likutis % m
print(f'dideliu deziu reikes {kiekD}, mazu reikes {kiekM}, liko nesupakuota {kiekliko}')