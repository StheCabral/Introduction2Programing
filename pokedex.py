running = True
pokedex = {} # {name : description, name: description...}
while (running):
    try:
        comand, name = input().split(" ")
        
        if (comand == "ADD"):
            if (name in pokedex.keys()):
                print("Pokémon já adicionado na Pokédex")
            else:
                description = input()
                pokedex[name] = description
                print("Pokémon adicionado com sucesso")
        elif (comand == "DESC"):
            if (name not in pokedex.keys()):
                print("Ainda não há registro desse Pokémon")
            else:
                print(pokedex[name])
    except EOFError:
        running = False