q_dia = int(input("Que dia é hoje? "))
q_mes = int(input("Qual mês (em número) é? "))
q_ano = int(input("Em que ano estamos? "))
bissexto = input("O ano é bissexto? (s/n)  ").strip().lower()

aniv_ano = int(input("Em que ano você nasceu? "))
aniv_mes = int(input("Em que mês você nasceu? "))
aniv_dia = int(input("Em que dia você nasceu? "))

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dias_mes_b = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = 0
if q_mes > 1:
    if (bissexto == "n"):
        for i in range(q_mes - 1): 
            mes += dias_mes[i]
    else:
        for i in range(q_mes - 1): 
            mes += dias_mes_b[i]
else:
    mes = 0
    
dia = q_dia - 1
idade = q_ano - aniv_ano - 1

ano_b = 0
for anos in range(aniv_ano, q_ano):
    if anos % 100 != 0 and anos % 4 == 0 or anos % 400 == 0:
        ano_b += 1

ano_final = ano_b*366 + (idade - ano_b)*365 
dias_total = dia + mes + ano_final

print(f"Você tem {dias_total} dias COMPLETOS de vida! \o/")