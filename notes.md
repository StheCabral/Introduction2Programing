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
# Aula 3 
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
