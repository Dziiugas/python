kort = (5,8,9,7,9,4)

kort1 = 5,8,9,7,9,4,5
print(type(kort1))
kort2 = (2,) #aprasyti tuple su 1 elementu
list = [5,8,9,7]
kort4 = tuple(list)

print(type(kort4))

for i in kort1:
    print(i)

print(kort1.count(5))
print(kort1.index(5))

k = (5,8,9)
g = k
k += (5,9)
print(id(g))
print(id(k))
print(k)
print(len(k))