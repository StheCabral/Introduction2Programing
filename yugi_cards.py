total_cards = int(input())
all_cards = []
# criando uma lista de objetos ex.: [{name: oi, idade: 12}, {name: ola, idade 16}]
for i in range (total_cards):
    card_temp= input().split(" ")
    defense = card_temp.pop(-1)
    attack = card_temp.pop(-1)
    name = (" ").join(card_temp)
    card = {'name': name, 'attack': attack, 'defense': defense}
    all_cards.append(card)
#criando listas com todos os attacks e todas as defesas
all_attacks = []
all_defenses = []
for i in range (total_cards):
    all_attacks.append(int(all_cards[i]['attack']))
    all_defenses.append(int(all_cards[i]['defense']))
# tirando o máx de cada uma e pegandi a posição de cada um na lista
max_attack = max(all_attacks)
index_attack = all_attacks.index(max_attack)
max_defense = max(all_defenses)
index_defense = all_defenses.index(max_defense)
# usando um tupla para sintetizar as respostas
winner = ( all_cards[index_attack]['name'], all_cards[index_attack]['attack'],  all_cards[index_defense]['name'], all_cards[index_defense]['defense'], all_cards[index_defense]['defense'])
print(f"Carta com maior poder de ataque: {(winner[0])}\nAtaque: {(winner[1])}\n\nCarta com maior poder de defesa: {(winner[2])}\nDefesa: {(winner[3])}")