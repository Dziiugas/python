aibeA = {1,2,3,4,5}
aibeB = {1,2,3,4,5,7,8,11}
aibeC = {12,13,14,15}
aibeD = {1,2,5,6}

#klaida jei elementas neegzistuoja
aibeA.remove(1)
print(aibeA)

aibeA.discard(2)
print(aibeA)

#grazina salinama reiksme
kazkas = aibeA.pop()
print(kazkas)
print(aibeA)

aibeC.clear()
print(aibeC)