import random
numberCards = int(input("The number of cards: ")) # 3 <= numberCards <= 1000
valuestorage = []

#Input card value
for _ in range(numberCards):
    valueCards = int(input("The value of each cards: "))
    valuestorage.append(valueCards)

#Output result 
result = 0
while True:
    if len(valuestorage) == 2:
        break 
    randomCard = valuestorage[len(valuestorage)-2] # no idea 
    if randomCard != valuestorage[0] and randomCard != valuestorage[len(valuestorage)-1]:
        valuestorage.remove(randomCard)
        result += (randomCard*(valuestorage[len(valuestorage)-3] + valuestorage[len(valuestorage)-1])) #no idea
print(result)
    
#Choose biggest result (idk how to find it) :(
