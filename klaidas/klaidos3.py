#apskaiciuoti rez = 100 / sk
ciklasVeikia = True
while ciklasVeikia:
    try :
        sk = int(input('iveskite skaiciu'))
        rez = 100 / sk
        ciklasVeikia = False
    except Exception as ex:
        print(f'kaskas blogai..{ex}')
    else:
        print('panasu kad viskas gerai')
    finally:
        print('man dzin ar viskas buvo gerai.')
        
print(f'sk = {rez}')
