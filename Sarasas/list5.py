m = [5,8,9,7,9,4,-1,5,-5,8,9,7,4,4]
def rastididziausia(sarasas):
    did = sarasas[0]
    for i in range(1,len(sarasas)):
        if did < sarasas[i]:
            did = sarasas[i]
    return did
d = rastididziausia(m)
print(d)
didelis = max(m)
print(m.count(rastididziausia(m)))
print(m.index(rastididziausia(m)))
print(m)
m.remove(m[4])
print(m)
print(m.pop(m[0]))

