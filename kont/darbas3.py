m = int(input('skaicius..'))
daugiklis = 10
suma = 0
for i in range(1, m + 1):
    daugikliskitas = daugiklis
    while daugikliskitas > 0:
        daugikliskitas //= 10
        sep = daugikliskitas * 7
        suma += sep
    daugiklis *= 10
print(f'suma {suma}')