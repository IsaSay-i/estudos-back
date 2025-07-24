import os
os.system("clear")

talvez_uma_matriz = [ [ ["Pão", 2, 0],
                        [3, "Queijo", 6],
                        [0, 1, "Tomate"]],
                     
                      [ ["Uva", 2, 0],
                        [3, "Morango", 6],
                        [0, 1, "Framboesa"]]
                    ]
print(talvez_uma_matriz[1][1][0])
talvez_uma_matriz[1][1][0] = "mudado"
print(talvez_uma_matriz[1][1][0])

# for barra in talvez_uma_matriz:
#     print(barra)
    # for num in barra:
    #     print(num)