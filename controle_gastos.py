X = int(input())

if ((X != 20) and (17 <= X <= 26)):
    if (X % 2 == 0):
        print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")
    else:
        print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
else:
    print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")