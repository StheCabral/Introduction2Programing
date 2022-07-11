F1 = int(input())
F2 = int(input())
A1 = input()
A2 = input()
P1 = float(input())
P2 = float(input())

if (F1 > F2):
    print("Aang venceu o combate!")
elif (F1 < F2):
    print("Aang perdeu o combate e agora esta preso na fortaleza da nacao do fogo.")
elif (F1 == F2):
    if (A1 != A2):
        if (A1 == "Lento"):
            print("Aang perdeu o combate e agora esta preso na fortaleza da nacao do fogo.")
        elif (A1 == "Rapido"):
            print("Aang venceu o combate!")
    elif (A1 == A2):
        if (P1 >= P2):
            print("Aang venceu o combate!")
        elif (P1 < P2):
            print("Aang perdeu o combate e agora esta preso na fortaleza da nacao do fogo.")