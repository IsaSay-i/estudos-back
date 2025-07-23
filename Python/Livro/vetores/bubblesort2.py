import os
os.system('cls' if os.name=="nt" else 'clear')

lista = []
item = 0

while True:
    try:
        item = input("Insira algum número (Insira nada e pressione Enter para parar)\n: ")
        if item == "":
            break
        lista.append(float(item))
        
    except ValueError:
        print("Tem que ser um valor numérico.")

print()
for num in lista:
    print(num, end="; ")

for i in range(len(lista)):
    for j in range(1, len(lista)-i):
        if lista[j-1] > lista[j]:
            # temp = lista[j-1]
            # lista[j-1] = lista[j]
            # lista[j] = temp
            lista[j-1], lista[j] = lista[j], lista[j-1]

print("Lista vazia.") if len(lista)==0 else print()
for num in lista:
    print(num, end="; ")