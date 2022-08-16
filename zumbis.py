bottles = int(input()) #frascos disponíveis
total_elements = int(input())
lab = [] # [[sodio, 1500], [bromio, 300], [prata, 400]]
is_there_cure = False
for i in range (total_elements): # criando uma lista com sublistas contendo o elemento e sua quantidade
    element = input().split(" ")
    lab.append(element)
for j in range (len(lab)): # percorrendo a lista de sublistas
    soma = int(lab[j][1]) # quero que comece de um dado numero
    i = int(j + 1)
    while ((soma < bottles) and (i < len(lab))): # esse dado número vai sendo somando com seus próx
        amount = int(lab[i][1])
        soma += amount
        i += 1
    else: # caso a soma ultrapasse o que queremos ou não haja mais próximo
        if (soma == bottles): #verificando se chegou
            is_there_cure = True
            start = j #guargando o começo e fim da sublista
            end = i
            j = len(lab)
if (is_there_cure):
    elements_in_cure = lab[start:end]
    elements_names = []
    for element in elements_in_cure: #formantando a saída
        elements_names.append(element[0])
    names = (" ").join(elements_names)
    print(f"Vencemos a batalha e a humanidade foi restaurada! {names} foram usados para deszumbificar")
else:
    print("Estou sentido algo estranho... será que também vou virar zumbi?")