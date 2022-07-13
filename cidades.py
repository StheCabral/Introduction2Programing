cidade1 = input()
nota1 = float(input())
distancia1 = int(input())
cidade2 = input()
nota2 = float(input())
distancia2 = int(input())
cidade3 = input()
nota3 = float(input())
distancia3 = int(input())


if (nota1 < 4 and nota2 < 4 and nota3 < 4):
    print("Nota mínima não atingida")
else:
    if (nota1 > nota2):
         choosen_city = cidade1
         nota_ref = nota1
         dist_ref = distancia1
    elif (nota2 > nota1):
         choosen_city = cidade2
         nota_ref = nota2
         dist_ref = distancia2
    else:
          if(distancia1 < distancia2):
               choosen_city = cidade1
               nota_ref = nota1
               dist_ref = distancia1
          else:
               choosen_city = cidade2
               nota_ref = nota2
               dist_ref = distancia2fllat

     
    if (nota3 > nota_ref):
      choosen_city = cidade3
    elif (nota3 == nota_ref):
        if(distancia3 < dist_ref):
           choosen_city = cidade3

    print(f"{choosen_city}")