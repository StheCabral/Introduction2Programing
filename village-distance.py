X = int(input())
Z = int(input())
 
H = ((X - 34)**2 + (Z - 220)**2) ** (1/2)
K = ((X - 0)**2 + (Z - 0)**2) ** (1/2)
S = ((X - 140)**2 + (Z - 456)**2) ** (1/2)

print(f"Distancia para Hogsmeade: {H:.2f}")
print(f"Distancia para Kakariko: {K:.2f}")
print(f"Distancia para Solitude: {S:.2f}")