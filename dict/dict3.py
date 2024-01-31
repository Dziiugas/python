prekes = {
    'duona' : 1.25,
    'vanduo' : 0.69,
    'konservai': 2.45,
    'vaisvandeniai': 1.58,
    'mesa': 7.25,
    'zuvis' : 8.25
 }

def perkam():
    suma = 0
    while True:
        vienaPreke = input('ka pirksime? prekiu sarasa')
        if vienaPreke == 'end':
            #jei ivedu bloga prekes pavadinima raso tokios prekes nera
            break
        suma += prekes[vienaPreke]
    return suma
print(perkam())