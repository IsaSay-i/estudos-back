import os
os.system("clear")

cities = ["Vitória", "Belo Horizonte", "Rio de Janeiro", "São Paulo"]
distances = [
    [0, 524, 521, 882],
    [524, 0, 434, 586],
    [521, 434, 0, 429],
    [882, 586, 429, 0]  ]

origin = int(input("Escolha sua cidade de Origem:\n0) Vitória\n1) Belo Horizonte\n2) Rio de Janeiro\n3) São Paulo\n: "))
destiny = int(input("\nEscolha sua cidade de Destino:\n0) Vitória\n1) Belo Horizonte\n2) Rio de Janeiro\n3) São Paulo\n: "))

print(f"\nDe {cities[origin]} para {cities[destiny]}\nDistância: {distances[origin][destiny]} km")

diagonal = 0
tri_sup = 0
tri_inf = 0

for i in range(4):
    for j in range(4):
        if i < j:
            tri_sup += distances[i][j]
        elif i > j:
            tri_inf += distances[i][j]
        else:
            diagonal += distances[i][j]
            
print(f"\nDiagonal: {diagonal}\nTriangulo Superior: {tri_sup}\nTriangulo Inferior: {tri_inf}")