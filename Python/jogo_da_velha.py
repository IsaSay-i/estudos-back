import os
os.system("clear" if os.name=="posix" else "cls")
    
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "] ]

def mostrar_tabuleiro():
    for barra in tabuleiro:
        print()
        for casa in barra:
            print("|", casa ,end="|")
    print()

