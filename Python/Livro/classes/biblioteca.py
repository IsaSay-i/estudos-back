data = {
    "Alice": {"age": 28, "occupation": "Engenheira de Dados"},
    "Bruno": {"age": 35, "occupation": "Analista de Sistemas"},
    "Carla": {"age": 24, "occupation": "Desenvolvedora Back-End"}
}

def handle_data(times):
    times = times
    for i in range(times):
        nome = input(f"\nInsira o nome {i+1}: ").title()
        idade = int(input(f"Insira a idade {i+1}: "))
        cargo = input(f"Insira o cargo {i+1}: ").title()
        print()
        data.update({ nome: {"age": idade, "occupation":cargo}})
        
def show_data():
    for name, info in data.items():
        print(f"{name} - Idade: {info["age"]}, Cargo: {info["occupation"]}")
    
handle_data(1)
show_data()
