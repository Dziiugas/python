#suprogramoti skaiciuotuva +,-,*,/,^ = kelimas laipsniu, & - saknies traukimas

p1 = int(input('skaicius..'))
v1 = input('mygtukas..')
p2 = int(input('skaicius..'))

match v1:
    case '+':
        (p1 + p2)
        print(f'{p1} {v1} {p2} = {p1 + p2}')
    case '-':
        (p1 - p2)
        print(f'{p1} {v1} {p2} = {p1 - p2}')
    case '*':
        (p1 * p2)
        print(f'{p1} {v1} {p2} = {p1 * p2}')
    case '/':
        (p1 / p2)
        print(f'{p1} {v1} {p2} = {p1 / p2}')
    case '^':
        (p1 ^ p2)
        print(f'{p1} {v1} {p2} = {p1 ^ p2}')


    



    