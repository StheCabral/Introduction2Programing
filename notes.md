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

# Cheat sheet

### Placeholder em python
```
name = "Marcos"
print(f"Oi, {name}")
```
