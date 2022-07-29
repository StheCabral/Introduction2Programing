contador = 0
line = None
while (line != "Boa noite"):
        line = input()
        if (line == "toc-toc-toc" or line == "Penny" or line == "Boa noite"): 
            if (line == "toc-toc-toc"):
                previous_line = line
            elif (line == "Penny"):
                if (previous_line == "toc-toc-toc"):
                    contador += 1
                    print(contador)
                    previous_line = None
                if (contador == 3):
                    print("Pode entrar Sheldon")
                    contador = 0
        else:   
            contador = 0 
            print("Não pode entrar, se identifique!!!")  
else:
    print("Boa noite Penny")
