prekes = {
    'duona' : 1.25,
    'vanduo' : 0.69,
    'konservai': 2.45,
    'vaisvandeniai': 1.58,
    'mesa': 7.25
 }

print(type(prekes))
print(prekes)

draugai = dict(Tomas = 28, Tadas = 32, Jonas = 51, Stasys = 45)
print(type(draugai))
print(draugai)
priesai = dict.fromkeys(['Vytautas','Kestas','Rimas'], [])
print(type(priesai))
print(priesai)

kainaMesa = prekes['mesa']
print(kainaMesa)
print(prekes.get('vitaminai'))
print(prekes.get('duona'))
print(prekes.get('vitaminai','deja sios prekes neturim'))
print(prekes.get('duona','deja sios prekes neturim'))

prekes['pienas'] = 1.56
print(prekes)

del prekes['vanduo']
print(prekes)
prekiuSar = prekes.keys()
print(type(prekiuSar))
print(prekiuSar)
prekiuSar = list(prekes.keys())
print(prekiuSar)
sutvarkytas = sorted(prekes.keys())
print(sutvarkytas)

#ar yra preke
print('zuvis' in prekes)
print('duona' not in prekes)

kainos = prekes.values()
print(kainos)

for k, v in prekes.items():
    print(f'preke {k} kainuoja {v} eur.')

sarasoKopija = prekes.copy()
print(sarasoKopija)
kazkas = prekes.items()
print(kazkas)

prekes.pop('mesa')
print(prekes)

print(len(prekes))
print(prekes.popitem())
print(prekes)

prekes.setdefault('Pica')
print(prekes)