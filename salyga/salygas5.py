# ivedami du skaicia surasti didziausia ir maziausia nenauodojant min ir max
a = int(input('a= ...'))
b = int(input('b= ...'))

def isvedimas(did,maz):
    print(f'{did} daugiau uz{maz}')
    return did, maz
if a > b:
    isvedimas(a, b)
    #did = a
   # maz = b
    #print(f'{did} didziausia, o {maz} maziausia...')
elif a < b:
    isvedimas(b, a)
    #did = b
    #maz = a
    #print(f'{did} didziausia, o {maz} maziausia...')
else:
    print('skaiciai lygus')
