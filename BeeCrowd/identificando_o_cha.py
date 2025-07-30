import os

T = int(input("Escolha o tipo de chá para iniciar o jogo\n1- Chá Branco\n2- Chá Verde\n3- Chá Preto\n4- Chá de Ervas\n: "))
tea_types = ["Chá Branco", "Chá Verde", "Chá preto", "Chá de ervas"]
choices = []
counter = 0

for i in range(1, 6):
    os.system("cls" if os.name=="nt" else "clear")
    choice = int(input("\nInsira o tipo de chá:\n1- Chá Branco\n2- Chá Verde\n3- Chá Preto\n4- Chá de Ervas\n: "))
    choices.append(choice)
print("\nResultados: ", end="")
for answer in choices:
    if answer == T: counter += 1
    print(answer, end=" - ")
print(f"\nRespota: {tea_types[T-1]}")
print("Acerto(s): ",counter)