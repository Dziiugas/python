#koks "veikiantis" p 1<=p<=10
#koks "neveikiantis" p 

def ivedimas():
    p = int(input('p= '))
    if not(1<=p<=10):
        print('netinkamas balas')
        return ivedimas()
    else:
        return p
 


#p = int(input('p= '))
#if not (1<=p<=10) :
 #   print(f'{p} "neveikiantis"pazymys')
 #   p = int(input('p= '))
#else :
 #   print(f'{p} "veikiantis"pazymys')

paz = ivedimas()
print(paz)