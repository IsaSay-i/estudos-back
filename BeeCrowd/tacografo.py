# Entrada: numéro inteiro N -> quantidade de entradas
#          variaveis para calcular os intervalos (T(tempo) = 10 horas, V(velocidade média)= 0km/h)

i = int(input())
soma = 0
for j in range(i):
    v, t = map(int ,input().split())
    soma += v * t
print(soma)