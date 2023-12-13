duom_sar = ['duom1.txt','duom2.txt','duom 3.txt','duom4.txt']
duom_klaida = []
duom_info = []

for byla in duom_sar:
    try:
        f = open(byla, 'r', encoding='utf-8')
        duom_info.append(f.read())
    except Exception as ex:
        duom_klaida.append(byla)
        print(ex)

print(f'klaidingi failai {duom_klaida}')
print(f'duomenys :{duom_info}')