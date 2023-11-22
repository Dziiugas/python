pav = input("prekiu skaicius")
d = input("kiek yra dideliu deziu...")
m = input("kiek yra mazu deziu...")

bigBoxAmount = (pav // d)
remainder = (pav % d)
smallBoxAmount = (remainder // m)
boxRemainder = (remainder % m)
print(f'dideliu deziu reikes {bigBoxAmount}, mazu reikes {smallBoxAmount}, liko nesupaku')