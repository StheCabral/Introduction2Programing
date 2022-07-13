pedemoleque = input()
qtd_pm= int(input())
cocada = input()
qtd_cd = int(input())
maca = input()
qtd_maca = int(input())

total = qtd_pm + qtd_maca + qtd_cd
fat_pedemoleque = qtd_pm * 2
fat_cocada = qtd_cd * 5
fat_maca = qtd_maca * 3
fat_referencia = fat_pedemoleque
melhor_doce = pedemoleque
qtd_referencia = qtd_pm

if (total == 0):
    print("A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...")
else:
    if (fat_cocada > fat_referencia):
        fat_referencia = fat_cocada
        melhor_doce = cocada
        qtd_referencia = qtd_cd

    elif (fat_cocada == fat_referencia):

        if (qtd_cd > qtd_pm):
            fat_referencia = fat_cocada
            melhor_doce = cocada
            qtd_referencia = qtd_cd

    elif (fat_maca > fat_referencia):
        fat_referencia = fat_maca
        melhor_doce = maca
        qtd_referencia = qtd_maca

    elif (fat_maca == fat_referencia):

        if (qtd_maca > qtd_referencia):
            fat_referencia = fat_maca
            melhor_doce = maca
            qtd_referencia = qtd_maca

    print(f"Oxe! Você ganhou {fat_referencia} reais vendendo {melhor_doce}. O povo gostou, visse?!")
