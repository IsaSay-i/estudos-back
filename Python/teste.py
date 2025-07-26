x = 0

print(x)

for i in range(3):
    if True or True or True:
        x += 1
    # x será 1 (incrementado só uma vez)

    # x = 0
    # if True:
    #     x += 1
    # if True:
    #     x += 1
    # if True:
    #     x += 1
    # x será 3 (incrementado três vezes)

    # x = 0
    # if True:
    #     x += 1
    # elif True:
    #     x += 1
    # elif True:
    #     x += 1
    # x será 1 (incrementado só uma vez)

print(x)