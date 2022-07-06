# input é q quantidade de packs de ferro que o personagem possui, um pack corresponde a 64 unindades de ferro (P >= 3), essa quantidade será dividida igualmente para 3 vilas e o resto descartado
P = 0
while (P < 3):
    P = int(input())

V = (P // 3) #quantidade de packs para cada vila
F = (P % 3) #packs descartados
print(V)
print(F)