previous_call = "none"

while (call != "Boa noite"):
    call = input()
    if (previous_call == "toc-toc-toc" and call == "Penny"):
        i +=1
        print(i)
    elif (call =! "toc-toc-toc" and call!= "Penny"):
        print("Não pode entrar, se identifique!!!")

else:
    print("Boa noite Penny")
    
####################################################
line = None
while (line != "Boa noite"):
    for i in range (1, 7):
        line = input()
        if (line == "toc-toc-toc"):
            previous_line = line
        elif (previous_line == "toc-toc-toc" and line == "Penny"):
            print(i/2)
            previous_line = None
        elif (line != "toc-toc-toc" and line != "Penny" and line != "Boa noite"): 
            i = 1
            print("Não pode entrar, se identifique!!!") 
    else: 
       print("Pode entrar Sheldon")    
else:
    print("Boa noite Penny")
