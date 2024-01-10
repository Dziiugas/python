aibeA = {1,2,3,4,5}
aibeB = {1,2,3,4,5,7,8,11}
aibeC = {12,13,14,15}
aibeD = {1,2,5,6}
#ar poaibis
print(aibeA.issubset(aibeB))

#ar virsaibis

print(aibeB.issuperset(aibeA))

#ar visi skirtingi
print(aibeC.isdisjoint(aibeB))

#aibiu sajunga

aibeE = aibeA.union(aibeD)
print(aibeE)

#aibiu sankirta

aibeF = aibeD.intersection(aibeA)
print(aibeF)

#aibiu skirtumas
aibeG = aibeA.difference(aibeD)
aibeG1 = aibeA.difference_update(aibeD)
print(aibeG)
print(aibeG1)

aibeG2 = aibeC.symmetric_difference(aibeD)
print(aibeG2)
aibeG3 = aibeC.union(aibeD)