import os
os.system('cls' if os.name=="nt" else 'clear')

Vet = []
VetDes = []
i = 0
soma = 0

for i in range(10):
    x = int(input(f"Digite o {i+1} número: "))
    Vet.append(x)
media = sum(Vet)/10

for j in range(10):
    x = abs(Vet[j] - media)
    VetDes.append(x)
mediaDes = sum(VetDes)/10

print("\nVet: ", Vet)
print("Vet Des: ", VetDes)
print(f"Média: {media:.2f}")
print(f"Média Desviada: {mediaDes:.2f}")