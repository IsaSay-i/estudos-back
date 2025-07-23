import os
os.system('cls' if os.name=="nt" else 'clear')

lista = [-9, 13, 21, 4, 0, 55, 1, -41] #8 números

print(lista)

for i in range(8):
    for j in range(1, 8-i):
        if lista[j-1] > lista[j]:
            temp = lista[j-1]
            lista[j-1] = lista[j]
            lista[j] = temp

print(lista)