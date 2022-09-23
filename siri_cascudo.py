ingredients = {
    'trigo': {'storage': 5, 'price': 3},

    'fermento': {'storage': 5, 'price': 2},

    'manteiga': {'storage': 5, 'price': 6},

    'batata': {'storage': 5, 'price': 4},

    'arroz': {'storage': 5, 'price': 3},

    'siri': {'storage': 5, 'price': 8},

    'pao': {'storage': 5, 'price': 2},

    'tomate': {'storage': 5, 'price': 2},

    'alface': {'storage': 5, 'price': 1},

    'picles': {'storage': 5, 'price': 3},

    'queijo': {'storage': 5, 'price': 5},

    'ovos': {'storage': 5, 'price': 2}
}
current_recipes = { 
    'hamburguer de siri': { 'recipe': ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'), 'price': 24},
    'pizza de siri': { 'recipe': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'), 'price': 42 },
    'siri frito': { 'recipe': ('siri', 'manteiga'), 'price': 15 },
    'siri a parmegiana': { 'recipe': ('siri', 'trigo', 'ovos', 'queijo', 'tomate'), 'price': 24 }
}
order_control = {'hamburguer de siri': 0, 'pizza de siri': 0, 'siri frito': 0, 'siri a parmegiana': 0}
cash = 40
open = True
while (open):
    try:
        order = input()
        if (order in (current_recipes.keys())):
            order_control[order] += 1
            # Atualizando o estoque depois do preparo e comprando mais se necessário
            for ingredient in current_recipes[order]['recipe']:
                if (ingredients[ingredient]['storage'] > 0):
                    ingredients[ingredient]['storage'] -= 1
                else:
                    ingredients[ingredient]['storage'] += 3
                    cash -= (ingredients[ingredient]['price']) * 4
            cash += current_recipes[order]['price']
            order_control[order] += 1
            print(f'{order} saindo...')
        elif (order in (order_control.keys())):
            order_control[order] += 1
            if (order_control[order] > 2):
                order_control[order] -= 2
                new_order = input().split(" ")
                current_recipes[order] = {'recipe': (), 'price': 5}
                current_recipes[order]['recipe'] = tuple(new_order)
                # Precificando nova receita
                for ingredient in current_recipes[order]['recipe']:
                    current_recipes[order]['price'] += ingredients[ingredient]['price']
                print(f'Atendendo demandas, {order} é a mais nova adição ao cardápio do Siri Cascudo.')
            else:
                print(f'{order} ainda não é uma opção disponível.')
        else:
            order_control[order] = 1
            print(f'{order} ainda não é uma opção disponível.')
    except EOFError:
        open = False
        print("##### Fim do expediente #####")
        print(f'O lucro obtido no dia de hoje foi de R${cash - 40}.')
        most_ordered_value = max(order_control.values())
        for key in (order_control.keys()):
            if (order_control[key] == most_ordered_value):
                most_ordered_name = key
        if (most_ordered_name == 'hamburguer de siri'):
            print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
        else:
            print(f'{most_ordered_name} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')

