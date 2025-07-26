class Cachorro:
    info = []
    
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        
        Cachorro.info.append({"nome": self.nome, "idade": self.idade, "raca": self.raca})
        
    @classmethod
    def exibir_info(cls):
        print("Informações:")
        for item in cls.info:
            print(f"Nome: {item["nome"]}\nIdade: {item["idade"]}\nRaça: {item["raca"]}\n")
        
    @classmethod
    def latir(cls):
        for item in cls.info:
            print(f"{item["nome"]}: AuAu!")

for i in range(2):
    nome = input(f"\nNome do cachorro {i+1}: ")
    idade = input(f"Idade do cachorro {i+1}: ")
    raca = input(f"Raça do cachorro {i+1}: ")

    Cachorro(nome, idade, raca)
    
Cachorro.exibir_info()
Cachorro.latir()