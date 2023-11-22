#ivedamas laikas valandos ir minutes. parasyti programa, kuri nustatytu koks laikas bus po
# 1 min
#pav 15 25 tai bus 15 26, bet jei ivedu 15 59 tai bus 16 00 ir jei ivedu 23 59 bus 0 0

val = int(input('iveskite val...'))
min = int(input('iveskite minutes...'))

#val = (15<=valanda<=16) or (23<=valanda<=0)
#min = (25<=minutes<=26) or (59<=minutes<=0)
#if valanda == 15 and minutes == 25:
 #   print('tai bus 15 val 26 min')
#lif valanda == 16:
 #   print('netaising val')
#else
min1 = min + 1
val1 = val + (min1//60)
min1 = min1 % 60
val1 = val1 % 24
print(f'po minutes bus {val1}:{min1}')
