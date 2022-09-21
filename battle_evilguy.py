# Definindo dados do Adversário
enemy_name = input()
enemys = {'Vingador': 30, 'Tiamat': 20, 'Vingador das Sombras': 14}
if (enemy_name in enemys.keys()):
    enemmy_life = enemys[enemy_name]
else:
    enemmy_life = 9
rounds = int(input())
weapons = {'Chifre': 2, 'Cajado': 4, 'Espada': 6, 'Grande espada': 8, 'Dardo': 12}
armors = {'Armadura pesada': 0, 'Armadura media': 1, 'Armadura leve': 3}
characters = {
    'Bobby': {'weapon': 'Grande espada','armor': 'Armadura media'},
    'Diana': {'weapon': 'Dardo', 'armor': 'Armadura leve'},
    'Eric': {'weapon': 'Grande espada', 'armor': 'Armadura pesada'},
    'Hank': {'weapon': 'Espada', 'armor': 'Armadura media'},
    'Presto': {'weapon': 'Cajado', 'armor': 'Armadura leve'},
    'Sheila': {'weapon': 'Espada', 'armor': 'Armadura leve'},
    'Uni': {'weapon': 'Chifre', 'armor': 'Armadura leve'} 
    }
mestre = False
while (rounds > 0 and enemmy_life > 0):
    person = input()
    if (person == 'Mestre dos Magos'):
        mestre = True
        enemmy_life = 0
    else:
        weapon = characters[person]['weapon']
        armor = characters[person]['armor']
        rounds -= armors[armor] + 1
        enemmy_life -= weapons[weapon]
else:
    if (mestre):
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
    else:
        if (enemmy_life <= 0):
            print(f'{person} executou o ultimo golpe em {enemy_name}, estamos livres!')
        elif (enemmy_life > 0):
            print(f'Oh nao, {enemy_name} e muito forte, este e o fim!')