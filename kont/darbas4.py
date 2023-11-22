n = int(input('n= '))
sk = 0
suma = 0
for i in range(n):
    sk = sk * 10 + 7
    print(sk)
sk += sk
print(f'suma {sk}')