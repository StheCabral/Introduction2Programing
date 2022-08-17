cin = [["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"]]
v_i = int(input())
v _j = int(input())
z_i = int(input())
z_j = int(input())
c_i = int(input())
c_j = int(input())
p_i = int(input())
p_j = int(input())
#Colocando CRACHÁ no lugar
cin[c_i][c_j] = "C"
#Colocando VOCÊ no lugar
cin[v_i][v_j] = "V"
#Colocando ZUMBI no lugar
cin[z_i][z_j] = "Z"
#Colocando PORTA no lugar
cin[p_i][p_j] = "P"

