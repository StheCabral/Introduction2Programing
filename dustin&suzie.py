length = int(input())
matriz = []
biggest_sum_line = -1
biggest_sum_column = -1
biggest_sum_diagonal = -1
for i in range (length):
    line = input().split(" ")
    for k in range (len(line)):
        line[k] = int(line[k])
    matriz.append(line)
#Percorrendo a matriz
for i in range (length):
    for j in range (length):
        # Analisando os pares das linhas
        if (j < (length - 1)): # so ir até a penúltima coluna
            sum_line = matriz[i][j] + matriz[i][j+1]
            if (sum_line > biggest_sum_line):
                biggest_sum_line = sum_line
                password_line = str(matriz[i][j]) + str(matriz[i][j + 1])  
        #Analisando a diagonal principal
        if ((j < (length - 1)) and (i < (length - 1))): #só ir até a penúltima posição da diagonal
            if (i == j):
                sum_diagonal = matriz[i][j] + matriz[i + 1][j + 1]
                if (sum_diagonal > biggest_sum_diagonal):
                    biggest_sum_diagonal = sum_diagonal
                    password_diagonal = str(matriz[i][j]) + str(matriz[i + 1][j + 1])
 # Analisando colunas
for j in range (length):
    for i in range (length):
        if (i < (length - 1)): # só ir até  penúltima linha
            sum_column = matriz[i][j] + matriz[i + 1][j]
            if (sum_column > biggest_sum_column):
                biggest_sum_column = sum_column
                password_column = str(matriz[i][j]) + str(matriz[i + 1][j])
# Formando a senha
password = password_line + password_column + password_diagonal
print(f"Falei que era fácil Dustinzinho...\nPegando todas os números que formam as combinações dos pares de cada sentido temos...\nPassword: {password}")