import os
os.system("clear" if os.name=="posix" else "cls")
    
class Jogo:
    jogadores = []
    fim = False
    casas_vazias = 9
    tabuleiro = [
        [" ","  1  "," 2  "," 3"],
        [1, " ", " ", " "],
        [2, " ", " ", " "],
        [3, " ", " ", " "] ] 
    
    def __init__(self, simbolo):
        self.simbolo = simbolo
        
        self.jogadores.append({"numero": 1, "simbolo": self.simbolo})
        self.jogadores.append({"numero": 2, "simbolo": "x" if self.simbolo == "o" else "o"})
        
    @classmethod
    def mostrar_tabuleiro(cls):
        for i, barra in enumerate(cls.tabuleiro):
            print()
            for j, casa in enumerate(barra):
                if i > 0 and j > 0:
                    print("|", casa, end=" |")
                else:
                    print(casa, end=" ")
        print()
        
    @classmethod
    def validar_colbar(cls, colbar):
        cls.colbar = colbar
        if colbar < 1 or colbar > 3:
            print("O número precisa ser de 1 a 3")
            return False
        else: return True
        
    @classmethod
    def validar_casa(cls, col, bar):
        cls.col = col
        cls.bar = bar
        if cls.tabuleiro[bar][col] in ["x", "o"]:
            print("Esta casa não pode ser marcada.")
            return False
        else: return True
            
    @classmethod
    def identificar(cls):
        for jogador in cls.jogadores:
            def encerrar():
                Jogo.mostrar_tabuleiro()
                print(f"\nJogador {jogador["numero"]}({jogador["simbolo"]}) Venceu!")
                cls.fim = True

            # Checando barra
            for i, barra in enumerate(cls.tabuleiro):
                if barra == [i, jogador["simbolo"], jogador["simbolo"], jogador["simbolo"]]:
                    encerrar()
            # Checando coluna
            for i in range(1, 4):
                if [cls.tabuleiro[j][i] for j in range(1, 4)] == [jogador["simbolo"]]* 3:
                    encerrar()
            # Checando diagonal
                if [cls.tabuleiro[i][i]] == jogador["simbolo"] * 3:
                    encerrar()
            # Checando diagonal reversa
            if (
                cls.tabuleiro[1][3] == jogador["simbolo"] and
                cls.tabuleiro[2][2] == jogador["simbolo"] and
                cls.tabuleiro[3][1] == jogador["simbolo"]
            ): encerrar()
            
    @classmethod
    def iniciar(cls):
        os.system("clear" if os.name=="posix" else "cls")
        print("JOGO DA VELHA")
        for jogador in cls.jogadores:
            print(f"Jogador {jogador["numero"]}: {jogador["simbolo"]}")
            
        while not cls.fim:
            for jogador in cls.jogadores:
                if cls.fim: break
                Jogo.mostrar_tabuleiro()
                while True:
                    col = int(input(f"\nJogador {jogador["numero"]}({jogador["simbolo"]}): Insira a coluna onde deseja marcar\n: "))
                    while not Jogo.validar_colbar(col): col = int(input(f"\nJogador {jogador["numero"]}({jogador["simbolo"]}): Insira a coluna onde deseja marcar\n: "))

                    bar = int(input(f"Jogador {jogador["numero"]}({jogador["simbolo"]}): Insira a barra onde deseja marcar\n: "))
                    while not Jogo.validar_colbar(bar): bar = int(input(f"Jogador {jogador["numero"]}({jogador["simbolo"]}): Insira a barra onde deseja marcar\n: "))
                    if Jogo.validar_casa(col, bar): break
                    
                cls.tabuleiro[bar][col] = jogador["simbolo"]
                cls.casas_vazias = cls.casas_vazias - 1
                
                Jogo.identificar()
                if cls.casas_vazias == 0:
                    print("oops, EMPATE!")
                    cls.fim = True
                    
if __name__ == "__main__":
    while True:  
        escolha = input("Escolha 'x' ou 'o': ").lower()
        if escolha not in ["x", "o"]: print("Você precisa escolher 'x' ou 'o'\n")
        else: break
    Jogo(escolha)
    Jogo.iniciar()