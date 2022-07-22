temperature = 30
hungry = True
internet = 0
action = None
while (action != "parar"):
    action = input()
    #verificando se o comando está fora dos listados
    if ((action != "ir para o grad") and (action !="sair para a rua") and (action !="comer uma quentinha") and (action !="conectar no wifi") and (action != "parar")):
        print("Entrada inválida")

    if (action == "ir para o grad"):
        temperature -= 5
        internet += 300
    elif (action == "sair para a rua"):
        temperature += 5
    elif (action == "comer uma quentinha"):
        hungry = False
    elif (action == "conectar no wifi"):
        internet += 100

if (temperature >= 30):
    print("A temperatura aqui não está agradável")
else:
    print("Agora sim, está aconchegante")
if (hungry):
    print("Meu corpo precisa de comida")
if (internet < 100):
    print("Essa conexão está horrível")

if (not(hungry) and (temperature <= 25) and (internet >= 300)):
    print("Finalmente um lugar preciso para mim!")