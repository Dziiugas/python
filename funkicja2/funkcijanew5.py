# *args

sar1 = [4,8,9,7,9]
sar2 = [5,8,9,-1,25,8,7,9]

def lyginiuSuma(*args):
    suma = 0
    for i in args:
        if i % 2 == 0:
            suma += i
    
    return suma

#print(lyginiuSuma(sar1, sar2))
print(lyginiuSuma(5,8,7,7,9,8,4,7,5,2,12))
print(lyginiuSuma(*sar1, *sar2))