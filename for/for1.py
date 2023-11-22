txt = 'man ą ė į š ų ū č ę labai patinka rytais anksti keltis ir eiti i mokykla'
lt = ('ąčęėįšųū')
kiek = 1
for i in txt:
    if i in lt:
        kiek += 1 #kiek = kiek + 1
print(f'sakinyje "{txt}" yra {kiek} zodziai')
