#try :
#    sk = int(input('iveskite skaiciu'))
#except ValueError:
#    print('blogai ivesti duomenys..')
while True:
    try :
        sk = int(input('iveskite skaiciu'))
        break
    except ValueError as ex:
        print(f'blogai ivesti duomenys...Klaida {ex}')
        
print(f'sk = {sk}')
