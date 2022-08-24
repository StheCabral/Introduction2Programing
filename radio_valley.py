def find_source(transmission):
    dirty_sea = ["crcrcrcrcr", "uuuuuuuoooooo", "ooooooeeeeeeee"]
    foreign_aircraft = ["ppprrrrrooon", "tutututututututu", "eeeeeeeeoooooo"]
    for word in transmission:
        if (word in dirty_sea) and (word in foreign_aircraft):
            print("A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!")
        elif (word in dirty_sea):
            print("É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…")
        elif (word in foreign_aircraft):
            print("São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??")
        else:
            print("Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.")
            next = False
next = True
while (next):
    transmission = input().split(" ")
    find_source(transmission)