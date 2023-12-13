import math

class TrikampioKlaidos(Exception):
    'vienas is trikampion klaidu..'

def trikampioplotas(a,b,c):
    if a<=0 or b<=0 or c<=0:
        raise TrikampioKlaidos('krastines turi buti didesnis uz 0')
    p=(a+b+c)/2
    s= math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
tr1 = trikampioplotas(5,8,4)
print(tr1)
try:
    tr2 = trikampioplotas(-2,10,10)
except TrikampioKlaidos as ex:
    print(ex)
else:
    print(tr2)