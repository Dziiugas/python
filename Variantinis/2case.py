diena = int(input('kokia savaites diena...'))
viskasok = True
match diena:
    case 1 | 2 | 3 | 4 | 5 :
        txt = 'darbo diena'
    case 6 | 7 :
        txt = 'savaitgalis'
    case _:
        print('blogai ivesti duomenys')
        viskasok = False

if viskasok :
    print(f'{diena} - {txt}')