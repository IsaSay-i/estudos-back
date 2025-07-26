import os

from numpy import fix
os.system("clear" if os.name=="posix" else "cls")
    
class Jogo:
    jogadores = []
    fim = False
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
    def verificar(cls):
        
        for jogador in cls.jogadores:
            def encerrar():
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
        print("JOGO DA VELHA")
        for jogador in cls.jogadores:
            print(f"Jogador {jogador["numero"]}: {jogador["simbolo"]}")
            
        while cls.fim == False:
            for jogador in cls.jogadores:
                Jogo.mostrar_tabuleiro()
                            
                col = int(input(f"\nJogador {jogador["numero"]}({jogador["simbolo"]}): Insira a coluna onde deseja marcar\n: "))
                bar = int(input(f"Jogador {jogador["numero"]}({jogador["simbolo"]}): Insira a barra onde deseja marcar\n: "))
                cls.tabuleiro[bar][col] = jogador["simbolo"]
                
                Jogo.verificar()
                if cls.fim == True: break
        
Jogo("x")
Jogo.iniciar()