sar1 = [2, 4,-5,6,-8,4,7,5]
sar2 = [-1,-2,4,3,2.5,-2,5]
sarnul = []
for x in sar1:
    for y in sar2:
        sumanul = x + 2*y
        if sumanul == 0:
            sarnul.append([x,y])
print(sarnul)

sar0 = [[x,y] for x in sar1 for y in sar2 if x+2*y == 0]
print(sar0)