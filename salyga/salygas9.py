# minus begalybes iki 0 netinkamas balas
# nuo 1 iki 3 blogas
# nuo 4 iki 6 patenkinimas
# nuo 7 iki 9 geras
# 10 labai geras
# nuo 11 iki +begalibes netinkamas balas

ivertinimas = int(input('ivertinimas '))

blogas = (ivertinimas>=1 and ivertinimas<=3)
patenkinimas = (ivertinimas>=4 and ivertinimas<=6)
geras = (ivertinimas>=7 and ivertinimas<=9)
labaigeras = (ivertinimas==10)
netinkamasbalas = (ivertinimas>=11)

if blogas:
    print('blogas vertinimas')
if patenkinimas:
    print('patenkinimas vertinimas')
if geras:
    print('geras vertinimas')
if labaigeras:
    print('labai geras')
if netinkamasbalas:
    print('netinkamas')
