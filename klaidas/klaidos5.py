import sys
duom_sar = ['duom1.txt','duom2.txt','duom 3.txt','duom4.txt']
duom_klaida = []
duom_info = []

try:
    for byla in duom_sar:
        try:
            f = open(byla, 'r', encoding='utf-8')
            duom_info.append(f.read())
        except Exception as ex:
            duom_klaida.append(byla)
            sys.exit()
finally:
    f = open('logo.txt','w',encoding='utf-8')
    for i in duom_info:
        f.write(i)
        f.write('\n')
    f.write(str(duom_klaida))
    f.close() 

