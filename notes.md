# Aula 1
## Conceitos
### Algortitmo
Começa como uma ideia, um plano, traduzido num conjunto ordenado de passos executáveis, não ambíguos, definindo um processo que tem um término
* A ordem dos passos é muito importante
* Ações bem definidas, sem ambiguidades, suficiente para serem seguidas

### Análise de Requisitos
Primeiro entender bem o problema e depois pensar e planejar a solução para não cair no loop de tentativa-erro na resolução do problema. (Na resolução das listas, em caso da questão não estar clara, não tentar adivinhar e falar com os monitores

### Pseudo-algoritmo
Próximo da lingaugem humana, apenas descrever os passos executados, criado com objetivos didáticos
ex.:
```
leia x
compute y como (x * 2)
imprima y
```

### Variável
Espaço de memória que armazena valores, nomes significativos e que respeitem as regras (em python é legal fazer tudo minúsculo, dividir as palavras com - e não usar números no começo)

### Tipo
Um conjunto de valores equipado com um cojunto de operações ex.: string(", a, b, c, +), integer(1, 2, 3, -, *) etc
* Fortemente tipado
* Fracamente tipado

### Expressões
* **Ordem de precedência**: ordem de prioridade quanto as operações numéricas a serem realizadas, podemos sobrescrever a ordem natural de precedência usando paranteses
* **Numéricas**: - + * / %  
* **Lógicas**: == =! >= <=
 
### Estruturas de Controle
* **Sequência**: comandos excecutados um após o outro
* **Seleção**: escolhe entre dois possíveis caminhos
*  **Repetição**: executar a mesma operação várias vezes


***
# Aula 3 - Tipos Primitivos
## Tipos Primitivos em Python
Aqueles que já vem na linguagem
* Tipos Estáticos: define em tempo de compilação, aquela variável só pode armazenar esse tipo
  *   Vantagem: evita problemas em sistemas mais complexos
* Tipos dinâmicos: o tipo da variável é definida durante a atribuição, podendo mudar ao atribuirmos um valor de tipo diferente
  * Vantagem & problema: não há preocupação com o tipo da variável

### Tipos Numérios
* integers (int()): números inteiros
* float (float()): números reais



### Manipulação de strings
* \n : em strings, quebra a linha
* \t : em strings, dá um espaço grande
* \\' : em strings, permite que as aspas apareçam sem encerrar a mensagem
* \+ : concatena, tudo no argumenta precisa ser string

***
# Aula 5 - Laços de Repetição

## While
Enquanto certa condição for verdade o bloco de código dentro do `while` será executada

* depois dele pode vir um `else`que executará o bloco de código dentro dele caso a condição seja falsa, como se fosse uma "última execução" que acontecerá quando finalmente a condição for falsa

### Exemplo
```
while (true):
 print("Está condiço é verdade")
else:
 print("Está condição é falsa")
```
### Exemplo
```
Código que execute uma operação de multiplicação a partir de múltiplas somas

op1 = int(input("Digite o primeiro fator: "))
op2 = int(input("Digite o segundo fator: "))

while (op2 > 0): 
 resultador += op1
 op2 -= 1
else:
 print(f"O resultado foi {resultado}")
```
## Range
* Conhecimento de Listas Necessário

Função criada para gerar listas, parametros:
* start: onde começa, default é 0 - opcional
* stop: onde termina - obrigatório
* step: de quanto em quanto, default é 1 - opcional

### Exemplo
```
list(range(2,5,1))

resulta em: [2, 3, 4]
```

## For

Laço de repetição com número de repetições definidas
* Também aceita aquele mesmo `else` do while

```
for i in range(start, stop, step):
 print(i)
```
### Comando `for` com dois índices
Esse código vai gerar multiplicações entre os elementos dos pares ordenados
```
for i, j in [(1,5). (2, 6), (3,7)]
 print(i * j)
else:
 print("fim")
```
### Comando `zip` para gerar tuplas
```
               x         y
ij = zip(range(1,4), range(5, 8))
list(ij)
```
esse código vai gerar uma tupla cujo primeiro elemento do par ordenado varia de 1 a 4, e o segundo elemento varia de 5 a 8, gerando a seguinte sequência:
[(1,5), (2,6 ), (3,7)]

### Outras formas de fazer
```
for i, j in zip([1,2, 3], [5,6,7])
 print(i * j)
else:
 print("fim")
```
# Aula 6- Listas
Estruturas feitas para guardar dados em cadeia
## Funções
* `len(lista)`: retorna o tamanho da lista
* Pode ser percorrida pelo `for`
* `lista.append(elemento)`: adiciona um elemento no final da lista
* `lista.index(elemento)`: retorna o índice daquele elemento na lista
 *  também podemos usar `lista.index(elemento, x)` em que x é o índice de partido
* `lista.sort()` : ordena a lista em ordem crescente
  * `lista.sort(reverse = True)` : ordena na ordem descrescente
* `sorted(lista)`: retorna outra lista ordenada sem modificar a original
* `lista.insert(index, valor)`: adiciona valor na posição index
* `lista.remove(valor)`: remove a primeira ocorrência de valor
* `lista.pop(index)`: remove o elemento de posição index da lista e retorna o valor removido (numa variável)
* `lista.replace(replaced, replacer)`: troca o valor replaced por um valor replacer
* É possível concatenar listas ex.:
```
lista1 = [1, 2]
lista2 = [3, 4]
lista1 + lista2 = [1, 2, 3, 4]
```
## Acessar por índices:
 `lista[0]` : primeiro elemento da lista
 `lista[-1]`: último elemento da lista (se tem 4 elementos, começaria no -4 por exemplo)
 ### Slicing
 Para acessar uma região da lista
 `lista[início:fim]`
 ex.:
 `lista[0:2]` Pega os elementos de índice 0 a 2
 `lista[:3]`  Admite que começa do 0 até o 3
 `lista[3:]`  Pega todos os elementos a partir do 3
 
 * `chr(x)`: retorna o caractere que representa o numero x na tabela ascii
 * `ord("x")`: retorna o numero que representa o caractere x na tabela ascii

 # Aula 7 - Recursão
 
 A capacidade que uma função tem de ser definida em termos de si própria, para ocorrer ela chama ela mesma em sequência
 Existem algoritmos inerentemente recursivos como um produto fatorial ou a sequência de fibonacci

### Estrutura da função recursiva
Dividimos a função em pelo menos duas partes:
1. Caso base
Aqui não temos recursão ainda, é mais cru
2. Passo indutivo
Chama o caso base para acontecer

* Recursão é útil para manipular alguma estruturas de dados como pilhas, árvores e listas ligadas

# Aula 8 - Tuplas e Dicionários

## Tuplas
São formas estruturadas de armazenar dados
* São estáticas, não se modificam
* Definição: `tupla1 = ("oi", "exemplo")`
* É possível iterar usando `for`, também funciona `len()`
* tupla de um elemnto: `tupla_unitaria = (2,)`

## Dicionários
Permite armazenar uma coleção de valores e qualifica eles através de chaves, permitindo que eles sejam acessados através desses valores
 ```
 meu_dicionario = {'nome': '''sthe''', 'idade': '''19 anos'''}
 print(meu_dicionario['nome'])
 ```
 * Pode adicionar elementos assim: `meu_dicionario['fone'] = 88888-8888` estamos criando uma chave se ela não existir ou atualizando
 * `meu_dicionario.update({'fone': '88888-8888'`}): o update pode adicionar ou modificar vários valores ao mesmo tempo
 * `del meu_dicionario['idade']`: remove um campo
 * `.pop` também funciona aqui `idade = meu_dicionario.pop('idade)`
 ### Comandos Básicos 
 * `len(dicionário)`: numero de campos armazenados
 * `dicionario.keys()`: retorna as chaves
 * `dicionario.values()`: retorna os valores
 * `dicionario.items ()`: retorna os pares chave-valor

### Iteração
```
for valor in dicionario.values()
for chave, valor in dicionario.items()
for chave in dicionarios.keys()
```

# Aula 8 - Exceções
Tratar os possíveis erros que podem acontecer dentro do código
* Ao usar um `try` é necessário pelo menos um `except`
* Podem ser usados n `excepts` para cada try
* `else` e `finally` são opcionais
* tem como criar suas próprias exceções
```
try:

(código da atividade)

except(tipo de erro):
(código de tratamento)

except:
(outro código de tratamento)

else:
(código para ser executado caso não ocorra nenhuma falha)

finally:
(vai executar no final independentemente se ocorrerem erros)
```
[mais sobre isso aqui](https://www.youtube.com/watch?v=EohsuSgkTQM&t=88s)

# Aula 9 - Módulos e Pacotes
* **Módulo**: é um arquivo .py que contém os conceitos principais do código (variáveis, classes constantes) e trata de um aspecto do programa. ex.: Módulo sobre a Biblioteca da Faculdade, Módulo sobre o Registro de Alunos
* **Pacote**: diretório que contém vários módulos associados a alguma visão (preocupação) do sistema ex.: um pacote relacionado â interface, outro à lógica central do sistema e outro sobre o banco de dados
* os pacotes utilizam uns aos outros através da importação 

* Os nomes de varáveis, funções ou constantes são únicos de cada módulo, portanto não há problema de ter duas funções com nomes iguais se tiverem em módulos diferentes, nem se tiverem sendo importadas no mesmo lugar
* Sintaxe para importação de funções:
  `from pacote import módulo` e `nome_modulo.nome_importação`
* Para importar todos os módulos: `from repositorio import *` mas é preciso incluir no arquivo __init__.py do repositório o seguinte `__all__ = [nomes dos módulos a serem importados quando *]`
* criando um alias: `from repositorio import base_dados as bd` posso chamar esse módulo como 'bd' agora
* Para diferenciar funções tbm é possível importar usando todo o path. ex.: `import interface.celular.interface_matricular`
### Main
É necessário ter um arquivo prinipal que chama os demais pacotes e módulos e tbm um lugar para que esse programa seja excutado com chamado. ex.:
```
def main():
   (codigoo prinicial de excução do programa)
   
 if __name__ == '__main__':
     main()
```
***
# Cheat sheet

### Placeholder em python
```
name = "Marcos"
print(f"Oi, {name}")
```

