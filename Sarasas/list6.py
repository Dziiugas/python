#petriuko pazymiai, suvedame, atspausdiname, apskaiciuojame vidurki,mamai rodom didesnius uz 3, tetciui didesnius uz 5
#gavom uzsakyma visai klasei

mama = 4
teti = 6
def k(vardas):
    kiek = int(input(f'kiek {vardas} turi pazymiu'))
    return kiek
def gautipazymius(kiek,vardas):
    paz = []
    i = 0
    while i<kiek:
        p = int(input(f'iveskite {vardas} {i+1}-aji pazyma..'))
        if 1<=p<=10:
            paz.append(p)
            i += 1
        else:
            print('blogas ivedimas')
    return paz
#pazymius grazinanti funkcija
def vidurkis(paz):
    if len(paz) == 0:
        return 0
    else:
        return sum(paz) / len(paz)
#vidurkis
def tevams(paz, kriterija):
    tevpaz = []
    for i in paz:
        if i >= kriterija:
            tevpaz.append(i)
    return tevpaz
#tevu  pazymiai
def rezultatas(vardas):
    paz = gautipazymius(k(vardas), vardas)
    pazM = tevams(paz, mama)
    pazT = tevams(paz, teti)
    print(f'{vardas} pazymiai yra {paz}, vidurkis{vidurkis(paz)}')
    print(f'{vardas} mamai pazymiai yra {paz}, vidurkis{vidurkis(pazM)}')
    print(f'{vardas} pazymiai teciui yra {paz}, vidurkis{vidurkis(pazT)}')
#rezultatas
klase = ['Petras','Antanas','Jonas','Stasys','Maryte','Ona']

for i in klase:
    rezultatas(i)
#rezultatas('petras')
#rezultatas('Ona')
#kiekp = k('Petras')
#kieks = k('Stasys')
#pazpetr = gautipazymius(kiekp, 'Petras')
#vidp = vidurkis(pazpetr)
#pazpetmamai = tevams(pazpetr, mama)
#pazpettetis = tevams(pazpetr,teti)
#print(pazpetmamai)
#vidpetmam = vidurkis(pazpetmamai)
#print(vidpetmam)