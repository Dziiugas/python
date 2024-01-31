with open('dom1.txt','r', encoding='utf-8') as f:
    txtList = f.readlines()

print(txtList)
komanda = {}
for txt in txtList:
    mas = txt.split(':')
    taskai = mas[1].replace(',','')
    komanda[mas[0]] = int(taskai)
print(komanda)