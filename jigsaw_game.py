set = []
for i in range (10):
    word = input()
    set.append(word)
words = []
repeated_words = []
soma = 0
for element in set:
    if ((element in words) and (element not in repeated_words)):
        repeated_words.append(element)
    elif (element not in words):
        words.append(element)
#desafio 1
print(f"As palavras sao:")
for each in words:
    if (each not in repeated_words):
        print(each)
        #desafio 2
        for letter in each:
            soma += 1
print(f"A soma do tamanho das palavras é: {soma}")
print("Estou impressionado, você me venceu, pode ir embora...")