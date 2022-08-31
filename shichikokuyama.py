def matching_syllables (word):
    how_many_matchs = 0
    for syllable in hospital_syllable:
        if ((syllable in word) and (syllable not in matching_list)):
            how_many_matchs += 1
            matching_list.append(syllable)
    return how_many_matchs

def whole_word_in (word):
    word_temp = word
    sylables= []
    whole_word = False
    list_letters = []
    for letter in word_temp:
        list_letters.append(letter)
        if (letter in "aeiou"):
            i = list_letters.index(letter)
            list_letters[i] = letter + "/"
    word_with_separator = ("").join(list_letters)
    sylables = word_with_separator.split("/")
    sylables.remove("")

    if (how_many_matchs == len(sylables)):
        if word_temp in hospital_name:
            whole_word = True
    return whole_word

def detach(word):
    word_temp = word
    detached_word = []
    detached_word_temp = []
    list_letters = []
    
    for letter in word_temp:
        list_letters.append(letter)
        if (letter in "aeiou"):
            i = list_letters.index(letter)
            list_letters[i] = letter + "/"
    word_with_separator = ("").join(list_letters)
    detached_word_temp = word_with_separator.split("/")
    for syllable in detached_word_temp:
        if (syllable in matching_list and syllable not in matching_list2):
            matching_list2.append(syllable)
            detached_word.append(syllable)
    return detached_word
# code
hospital_syllable = ["shi", "chi", "ko", "ku", "ya", "ma"]
hospital_name = "shichikokuyama"
matching_list = []
matching_list2 = []
while (len(matching_list) < 6):
    word = input()
    how_many_matchs = matching_syllables(word)
    if (how_many_matchs == 0):
        print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")
    elif (how_many_matchs == 1):
        print(f"Lembrei! A sílaba {matching_list[-1]} está no nome do hospital. Obrigada, Totoro!")
    elif (how_many_matchs > 1):
        whole_word = whole_word_in(word)
        if (whole_word):
           print(f"A palavra {word} está toda no nome do hospital. Acertou em cheio, Totoro!")
        else:
            detached_word = detach(word)
            if (how_many_matchs == 2):
                    print(f"Lembrei! As sílabas: {detached_word[0]}, {detached_word[1]} estão no nome do hospital. Obrigada, Totoro!")
            elif (how_many_matchs== 3):
                    print(f"Lembrei! As sílabas: {detached_word[0]}, {detached_word[1]}, {detached_word[2]} estão no nome do hospital. Obrigada, Totoro!")
            elif (how_many_matchs == 4):
                    print(f"Lembrei! As sílabas: {detached_word[0]}, {detached_word[1]}, {detached_word[2]}, {detached_word[3]} estão no nome do hospital. Obrigada, Totoro!")
            elif (how_many_matchs == 5):
                    print(f"Lembrei! As sílabas: {detached_word[0]}, {detached_word[1]}, {detached_word[2]}, {detached_word[3]}, {detached_word[4]} estão no nome do hospital. Obrigada, Totoro!")
            elif (how_many_matchs == 6):
                    print(f"Lembrei! As sílabas: {detached_word[0]}, {detached_word[1]}, {detached_word[2]}, {detached_word[3]}, {detached_word[4]}, {detached_word[5]} estão no nome do hospital. Obrigada, Totoro!")
else:
    print("Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!")
