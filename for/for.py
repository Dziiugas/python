txt = 'man labai patinka rytais anksti keltis ir eiti i mokykla'
kiek = 1
for i in txt:
    print(i)
    if i == ' ':
        kiek += 1 #kiek = kiek + 1
print(f'sakinyje "{txt}" yra {kiek} zodziai')
