try:
    f = open('data2.txt','w')
    f.write('bet kasssssss ')
    f.write('bet kasss ')
finally:
    f.close()


with open('data2.txt', 'a',encoding='utf-8') as f1:
    f1.write('tradadada ')
print('tradads ')