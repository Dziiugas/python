def skaitomFaila():
    with open('duom8.txt', 'r', encoding='utf-8') as f:
        txt = f.readlines()
    return txt

# raktas : [1,8,8]
def varzybos ():
    dalyviai = dict()
    duomenys = skaitomFaila()
    for eil in duomenys:
        vardas, taskas = eil.split()[:2]
        #print(f'{vardas} surinko {taskas}')
        taskas = int(taskas)
        if vardas in dalyviai:
            dalyviai[vardas].append(taskas)
        else:
            dalyviai[vardas] = [taskas]
        return dalyviai
    #print(varzybos)

def spausdinti(rez):
    with open('rez8.txt','a',encoding='utf-8') as f:
        f.write('\n--------------\n')
        f.write('|vardas | suma| max\n')
        f.write('\n--------------\n')
        for vardas, suma, did in rez:
            f.write(f'|{vardas:8}|{suma:3}|{did:3}|\n')
def valyti():
    with open('rez8.txt','a',encoding='utf-8') as f:
        f.write('')
valyti()
dalyviai1 = varzybos()
rezultatai = [(v, sum(t),max(t)) for v, t in dalyviai1.items()]
spausdinti(sorted(rezultatai))
#spausdinti(sorted(rezultatai, key = lambda e: e[1], reverse=True))
spausdinti(sorted(rezultatai, key = lambda e: e[1]))
varzybos()