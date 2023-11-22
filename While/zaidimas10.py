#(a - akmuo, z - zirkles, p - popierius)
#zaidejas ir kompiuteris
import random
z = int(input('popierius, akmuo, zirkles'))
bot = random.choice(['popierius','akmuo','zirkles'])
if z>=bot:
    print('laimi')
elif z==bot:
    print('tie')
else:
    print('nelaimi')
