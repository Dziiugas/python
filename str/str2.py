txt = 'Mano batai buvo du, bet kaskas atsitiko nerandu'

print(len(txt))
print(txt[len(txt)-1])
print(txt[-1])

kiekZodziu = txt.count(' ')+1
print(kiekZodziu)

print(txt.capitalize())
print(txt.upper())
print(txt.lower())
print(txt.islower())
print(txt.isupper())
print(txt.find('a'))
print(txt.find('a',5,15))
print(txt.find('ch',5,15))
t='123abc456'
print(t.isalnum())
t1='abcd'
print(t1.isalpha())
print(t.isspace())
t2 = ' '
t2 = t.strip(' ')
print(t2)

t3 = ' man patinka kaskas'
print(t3.replace('kaskas','buti namuose'))
print(ord(''))
print(chr(261))