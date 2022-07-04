numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 <= numero2:
    print(numero1, numero2)
else:
     print(numero2, numero1)
     
  
######
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
temp = 0

if (a > b):
    temp = a
    a = b
    b = temp
    print( "Os valores foram trocados: " + str(a) + ", " + str(b) )
else:
    print("Os valores continuaram os mesmos "  + str(a) + ", " + str(b) )
