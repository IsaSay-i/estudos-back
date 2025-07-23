import os
os.system('cls' if os.name=="nt" else 'clear')

lista = [-9, 13, 21, 4, 0, 55, 1, -41] #8 números

print(lista)

for i in range(8):
    menor = i
    for j in range(i+1, 8):
        if lista[j] < lista[menor]:
            menor = j
    # temp = lista[i]
    # lista[i] = lista[menor]
    # lista[menor] = temp
    
    lista[i], lista[j] = lista[j], lista[i]
print(lista)