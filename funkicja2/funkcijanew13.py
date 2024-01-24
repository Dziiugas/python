

sk = 5
def fun1():
    global sk
    sk +=1
    def fun2():
        global sk
        sk += 5
        print(f'fun2 = {sk}')
    fun2()
    print(f'fun1 = {sk}')

fun1()
print(f'virsus = {sk}')

for i in range (5):
    a = i
    print(i)


print(i)
print(a)