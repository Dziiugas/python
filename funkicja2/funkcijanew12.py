# LEGB
txt = 'Globali sritis'
def fun1():
    txt='enclosing sritis'
    def fun2():
        txt = 'lokali sritis'
        print(f'fun2 = {txt}')
    fun2()
    print(f'fun1 = {txt}')

fun1()
print(f'virsus = {txt}')