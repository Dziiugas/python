#ivedami du skaiciai parasyti programa su funkcijomis siu skaiciu apskaiciuoti
#modifikuoti 12 + 15 = 27
def ivedimas(txt):
    sk = int(input(f'{txt} = '))
    return sk

#a = ivedimas('pirmas')
#print (a)
#b = ivedimas('antras')
#print (b)

def sumavimas():
    sk1 = ivedimas('pirmas') 
    sk2 = ivedimas('antras')
    suma = sk1 + sk2
    return suma, sk1, sk2 
    #suma =  ivedimas('pirmas') + ivedimas ('antras')
    #return suma
def rezultatas():

    #print(sumavimas())  
    #rez = sumavimas()
    rez, a, b = sumavimas()
    print(f'{a} + {b} = {rez} ')

    #print(rez)
    #print(rezultatas)
  


rezultatas()