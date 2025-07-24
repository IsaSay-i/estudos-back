import os
os.system("clear")

matriz = [
    [2, 89, 7],
    [5, 12, 9],
    [-12, 72, 33]
]

somaCol = 0
somaBar = 0

for x in range(3):
    for y in range(3):
        somaCol += matriz[y][x]
        somaBar += matriz[x][y]
    print(f"Soma da coluna {x+1}: {somaCol}")
    print(f"Soma da barra {x+1}: {somaBar}\n")
    somaCol = 0
    somaBar = 0