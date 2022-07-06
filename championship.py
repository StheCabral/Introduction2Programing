A = int(input())
L = int(input())
P = int(input())
H = int(input())


S = ((A + L + abs(A - L)) / 2)
T = ((S + P + abs(S - P)) / 2)

print(int(T * H))