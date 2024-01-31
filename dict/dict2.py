auto_geras = {
    'Marke' : 'opel',
    'Kaina' : 2500,
    'turis' : 1.4,
    'dauztas' : False
}

auto_blogas = {
    'dauztas' : False,
    'turis' : 1.4,
    'kaina' : 2500,
    'marke' : 'opel'
}

print(auto_geras == auto_blogas)

daugiau_info = {
    'raida': 254874,
    'spalva': 'kibiro',
    'kaina': 3500
}

auto_geras.update(daugiau_info)
print(auto_geras)

kitas_auto = auto_blogas|daugiau_info
print(kitas_auto)
print(auto_geras.keys())
print(auto_blogas.values())
print(auto_geras.items())