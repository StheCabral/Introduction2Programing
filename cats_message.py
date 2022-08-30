def decode (code):
    code_list = code.split(" ")
    fail = False
    message_temp = ""
    for number in code_list:
        i = code_list.index(number)
        code_list[i] = int(number)
        number = code_list[i]
        #traduzindo para ascii (int -> int certo)
        if (number >= 50 and number <= 99): # é uma letra maiscúla
            if (number <= 75): #primeiro intervalo
                number_ascii = number + 15
            elif (number >= 76): #segundo intervalo
                number_ascii = number - 11
        elif (number >= 0 and number <= 49): # é uma letra minúscula
            if (number <= 25): #primeiro intervalo
                number_ascii = number + 97
            elif (number >= 26 and number <= 49): #segundo intervalo
                number_ascii = number + 71
        elif (number == 100):
            number_ascii = 32
        elif (number < 0 or number > 100):
            fail = True
        #traduzindo da ascii (int -> char)
        message_temp = message_temp + (chr(number_ascii))
    # mensagem final
    if (fail):
        message_decoded = "Infelizmente os números nao dizem nada"
    else: 
        message_decoded = message_temp
    return message_decoded
#input
code = input()
message_decoded = decode(code)
# output
print(message_decoded)