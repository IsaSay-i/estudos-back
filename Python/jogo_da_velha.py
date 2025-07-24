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

class Jogador:
    def __init__(self):
        self.numero = 0
        self.simbolo = ""
        self.simbolos_validos = ["x", "o"]
        self.jogadores = []

        escolha = ""
        while escolha not in self.simbolos_validos:
            escolha = input("Jogador 1\nEscolha o seu símbolo: (x|o)\n: ").lower()
            if escolha not in self.simbolos_validos:
                print("\nInválido! Selecione 'x' ou 'o'\n")
            else:
                self.jogadores.append({"numero": 1, "simbolo": escolha})
                self.jogadores.append({
                    "numero": 2,
                    "simbolo": "x" if self.jogadores[0]["simbolo"] == "o" else "o"
                })

        for i in range(2):
            print(f"Jogador {self.jogadores[i][self.numero]}: {self.jogadores[i][self.simbolo]}")

            
Jogador()