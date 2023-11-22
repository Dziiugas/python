txt = '52, 65, 85, 7, 41, 65, -55, -64, -51, 64, 89, 62'
#is txt eilutes gauti lyginiu skaiciu sarasa
sk = [int(i) for i in txt.split(', ')if int(i)% 2==0]
print(sk)