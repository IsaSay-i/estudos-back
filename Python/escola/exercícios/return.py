a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

# OBS: return finaliza as outras condições assim que uma condição se realizar
# se uma função precisar retornar mais de uma mensagem, faça uma lista/array e use append :p

def tamanho(a, b, c):
    msg = []

    if (b == c and c == a):
        msg.append("*São todos iguais")
    elif (b == c):
        msg.append("*B é igual a C")
    elif (a == c):
        msg.append("*A é igual a C")
    elif (a == b):
        msg.append("*A é igual a B")

    if (a > b and a > c ):
        msg.append("A é o maior valor")
    if (b > a and b > c ):
        msg.append("B é o maior valor")
    if (c > a and c > b ):
        msg.append("C é o maior valor")
    
    if (b > a and a > c  or  b < a and a < c):
        msg.append("A é o 2º maior valor")
    if (a > b and b > c  or  a < b and b < c):
        msg.append("B é o 2º maior valor")
    if (a > c and c > b  or  a < c and c < b):
        msg.append("C é o 2º maior valor")
    
    if (a < b and a < c ):
        msg.append("A é o menor valor")
    if (b < a and b < c ):
        msg.append("B é o menor valor")
    if (c < a and c < b ):
        msg.append("C é o menor valor")
    
    return msg

resultado = tamanho(a, b, c)

for mensagem in resultado:
    print(mensagem)
