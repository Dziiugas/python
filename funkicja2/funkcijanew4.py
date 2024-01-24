def datosFormatas(*, diena, menuo:str) -> str:
    return f'dabar yra {menuo} men. {diena} diena'

print(datosFormatas(diena = 13, menuo = 'spalis'))
print(datosFormatas('rugsejis', 1))