def rocks():
    tip = int(((120 - time) + total_tip)/2)
    return tip

def foot_massage():
    if (total_tip % 2 == 0):
        tip = (total_tip % 7)*6
    else:
        tip = (total_tip % 7)**2
    return tip

def meal():
    if (total_tip % 10 == 0):
        tip = 5
    else:
        while (total_tip % 10 != 0):
            tip = 1
    return tip

def complete_massage():
    tip = 0
    tip_digits = str(total_tip)
    for digit in tip_digits:
        tip += int(digit)
    return tip


time = 120
total_tip = 10
services = ['pedras', 'pes', 'refeicao', 'completa']
while (total_tip < 50 or time > 0):
    service = input()
    if (service not in services):
        time -= 5
        print(f"O cliente fez voce perder tempo, voce ainda possui {total_tip} gorjetas.")
    else:
        if (service == "pedras"):
            service_name = "Pedras Quentes"
            tip = rocks()
            time -= 20
            total_tip += tip
        elif (service == "pes"):
            service_name = "Massagem nos Pes"
            tip = foot_massage()
            total_tip += tip
            time -= 30
        elif (service == "refeicao"):
            service_name = "Servir Refeicao"
            tip = meal()
            total_tip += tip
            time -= 15
        elif (service == "completa"):
            service_name = "Massagem Completa"
            tip = complete_massage()
            total_tip += tip
            time -= 60
        print(f"Voce concluiu o servico de {service_name} e agora possui {total_tip} gorjetas.")
else:
    if (total_tip >= 50):
        print(f"Você acumulou {total_tip} gorjetas, com essa quantidade voce conseguira comprar sua passagem de saida e salvar seus pais.")
    else:
        print("Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.")

