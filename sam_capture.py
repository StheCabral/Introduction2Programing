names = input().split(",")
clues = [ "Não encontrei nada no primeiro suspeito", "O último da lista está limpo",
 "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita",
   "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:",
    "Acho que temos mais uma opção a ser analisada…" ]
while (len(names) != 1):
    dean = input()
    index = 0
    if (dean == clues[0]):
        names.remove(names[0])
    elif (dean == clues[1]):
       names.remove(names[-1])
    elif (dean == clues[2]):
        if (len(names) % 2 == 0):
            index = int((len(names) / 2))
            names.remove(names[index])
        else:
            index = int((len(names) // 2))
            names.remove(names[index])
    elif (dean == clues[3]):
        index = int(input())
        names.remove(names[index])
    elif (dean == clues[4]):
        new_suspect = input()
        names.append(new_suspect)
    else:
        print("Isso não estava no combinado, a lista vai permanecer do mesmo jeito")
else:
    print(f"Acho que encontramos o suspeito. O seu nome é {names[0]}, vamos salvar o Sam!")