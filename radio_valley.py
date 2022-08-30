def find_source1 (transmission):
    insect_count = 0
    insect = False
    dirty_sea = ["crcrcrcrcr", "uuuuuuuoooooo", "ooooooeeeeeeee"]
    for word in dirty_sea:
        if (word in transmission):
            insect_count += 1
    if (insect_count > 0):
        insect = True
    return insect
def find_source2 (transmission):
    foreing_count = 0
    foreing = False
    foreign_aircraft = ["ppprrrrrooon", "tutututututututu", "eeeeeeeeoooooo"]
    for word in foreign_aircraft:
        if (word in transmission):
            foreing_count += 1 
    if (foreing_count > 0):
        foreing = True
    return foreing
            
next = True
while (next):
    transmission = input().split(" ")
    insect = find_source1(transmission)
    foreing = find_source2(transmission)
    if (insect and foreing):
        print("A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!")
    elif (insect):
        print("É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…")
    elif (foreing):
        print("São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??")
    else:
        print("Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.")
        next = False
