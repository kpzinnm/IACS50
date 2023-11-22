## Introdução

Primeiramente, vamos dar uma breve introdução ao algoritmo de busca. Imagine que temos que criar um algoritmo que resolva um quebra-cabeça de 15 números, então recebemos um estado inicial contendo o estado no qual o problema vai começar:

![image](https://github.com/kpzinnm/IACS50/assets/100965133/881f33e2-adf7-40cf-9c82-1025f426468e)


Esse é o nosso estado inicial, o agente é quem recebe esse estado. Agora, vamos mostrar dizer ao algoritmo qual é o estado desejado:

![image](https://github.com/kpzinnm/IACS50/assets/100965133/7c4e8ac5-427a-4fac-8a7e-f36dec466bd4)

O desafio que esse tipo de algoritmo se propõe a resolver é, a partir de um estado inicial que nos é dado, como chegar a um estado final que conhecemos. No nosso exemplo, como podemos mecher as peças até o quebra-cabeça chegar no estado desejado.

Esse algoritmo parece besta e com pouca aplicabilidade, mas vamos usar outros exemplo:

![image](https://github.com/kpzinnm/IACS50/assets/100965133/77a74f8f-f981-4893-9a65-7971a01a98cc)

Para resolver esse labirinto, temos o estado inicial, que é onde nosso boneco está e o estado final que é a saída. Podemos aplicar um algoritmo de busca para achar o melhor caminho até a saída.

![image](https://github.com/kpzinnm/IACS50/assets/100965133/5cfa3ce1-a0fd-49c7-a5a1-8b94351803ab)


Outro exemplo interessante é o google maps, podemos aplicar algum tipo de algoritmo de busca para achar o melhor caminho para ir do ponto de partida(estado inicial) até o destino(estado desejado)

---

## Terminologia
Vamos falar sobre algumas entidades e estruturas que estão presentes no nosso algoritmo, para entendermos melhor seu funcionamento.

- Agente(agent): uma entidade que consegue perceber e atuar sobre o seu ambiente. No quebra cabeça pode ser a pessoa.

- Estado(state): São as configurações que o ambiente pode tomar
    
![image](https://github.com/kpzinnm/IACS50/assets/100965133/83a4e968-0c9f-4a6c-8f1c-bbaa4411fcbb)

    
Esses são três estados dentro do nosso contexto. Existem dois estados com destaque, o ****************inicial**************** e ************final.************
    
- Estado inicial(initial state): é o ponto de partida do nosso algoritmo, é desse estado que começamos a tomar as decisões para resolver o nosso problema.
- Estado final(final state): Esse é o estado que queremos chegar, como podemos partir do inicial até o final é o propósito desse algoritmo.
    
- Ação(action): Ações são ações ou modificações que podemos fazer em um estado, podemos entendê-las como funções que recebem um estado (action(S)) e retorna um conjunto de ações que podemos fazer naquele estado. Por exemplo:
    
![image](https://github.com/kpzinnm/IACS50/assets/100965133/9a3e855b-f8d0-4327-a7ca-ea9a6cce910e)

    
Caso a ação receba esse estado, o conjunto de ações que ele retornaria na saída seria: 1-baixo, 10-esquerda, 15-cima e 6-direita. Note que o conjunto de ações que a ação retorna depende do estado que ela recebe, um estado diferente retornaria um conjunto de ações diferentes.
    
- Modelo de transição(Transition model): Assim como as ações, vamos entende-lo como uma função que recebe dois parâmetros:
    
    transitionModel(S, A)
    
    - S: Um estado.
    - A: uma ação.
    
    O resultado dessa função é um novo estado Z, que é o resultado da aplicação da ação A no estado S.
    
![image](https://github.com/kpzinnm/IACS50/assets/100965133/6b5ce2a5-c882-41c8-ad50-3df70ca4a9a7)

    

- Espaço de estados(state space): O conjunto de todos os estados alcançáveis com base em um estado inicial.
    
![image](https://github.com/kpzinnm/IACS50/assets/100965133/e241ef15-0f54-408e-bb68-10298253a9d2)

    
Outra forma de visualização é por meio de um grafo, geralmente em formato de árvore, onde as arestas podem ou não ter peso. Caso as arestas tenham peso, a velocidade do algoritmo depende do peso das arestas, em um contexto que ação diferentes possuem a mesma performance, que é o caso do nosso exemplo, então levamos em conta apenas a quantidade de arestas (modelo de transição) que leva para ir do estado inicial até o desejado.
    
![image](https://github.com/kpzinnm/IACS50/assets/100965133/d65c83bb-6867-499c-bec9-4d0951b3cf81)

    

- Teste de meta(goal test): Esse teste verifica se o estado atual é o desejado, a partir desse teste que nosso algoritmo acaba.

- Custo de caminho(path cost): Um numero associado ao custo de um passeio no grafo, indo do estado inicial até o desejado. Esse custo pode ser avaliado por meio da quantidade de arestas que passamos ou pelo produto das arestas com seu respectivo peso, a depender do problema.

Em linhas gerais, esses são os termos que devemos conhecer, pois usaremos eles para entender o funcionamento do nosso algoritmo.

### Solução

A solução se dá por uma sequência de ações que conduz de um estado inicial até o estado desejado, entretanto, as vezes não queremos apenas um solução, mas uma solução ótima. Uma solução ótima é aquela que nos conduz do estado inicial até o desejado com o menor custo. 

## Funcionamento do algoritmo

Primeiramente, precisamos de uma estrutura de dados apropriada para lidar com os dados, para isso vamos usar nós.

### Nós

O nó é uma estrutura de dados que vamos usar para gerenciar os dados para a resolução do nosso problema:

- Nó pai: armazena o nó pai, ou seja, o nó que deu origem a ele.
- Ação: a ação que foi aplicada no estado pai.
- Estado atual: armazena o estado atual, que nada mais é que o estado resultante da aplicação da ação no estado pai.
- Custo do caminho: armazena o custo do estado inicial até o estado atual.

Com essas informações em mãos, realizamos o goal test no nó e caso a verificação seja verdadeira, podemos avaliar o custo que esse caminho tomou além de conseguirmos fazer um caminho de volta, isso é possível, pois temos a ação que gerou o nó atual e o seu nó pai com sua respectiva ação.

### Fronteira

Com os nós, temos uma estrutura capaz de armazenar informações sobre os estados, entretanto, precisamos de algo que gerencie os nós. Que a partir desses nós, consiga resolver nosso problema, isso é a fronteira.

O trabalho da fronteira é gerenciar os nós para chegar ao resultado, ela faz isso de forma simplificada, realizando alguns passos.

Primeiro, imagine a fronteira como uma estrutura de dados genérica para armazenar nós.

- Se a fronteira estiver vazia, todos os passos foram feitos, assim caso não tenha achado nenhum caminho significa que não existe solução para o problema.
- Remova um nó da fronteira.
- Faça o goal test, caso não seja o estado desejado.
- Expanda o nó, ou seja, realize as ações e adicione os nós resultantes na fronteira.

Esse simples passo a passo, “resolve” o problema para a gente, pelo menos problemas simples.

**Exemplo:** Com base no grafo a baixo, vamos realizar uma operação de sair do nó A até o E.

![image](https://github.com/kpzinnm/IACS50/assets/100965133/3615845c-bc0c-4dc9-9e49-db67c1d319c2)


****Fronteira: [A]****

Vamos remover o nó A, da fronteira e expandi-lo. Assim o resultado da operação é

********Fronteira: [B]********

Vamos remover o nó B, realizar o goal test, como ele falhou vamos expandi-lo.

********************************Fronteira: [C, D]********************************

Bem, a estratégia que iremos usar para remover determina como o algoritmo ira fazer a busca, então vamos deixar para falar disso depois.

Por hora, vamos remover o C e fazer um goal test, como ele irá falhar vamos expandi-lo

**********************************Fronteira: [E, D]**********************************

Agora, vamos remover o E e realizar o goal test, assim CATAPIMBA!! O nó E passou no goal test, chegamos ao resultado esperado.

Esse é um exemplo bem simples da utilização de uma fronteira, mas note uma coisa, se o grafo fosse bidirecional, podia entrar em um loop.

![image](https://github.com/kpzinnm/IACS50/assets/100965133/e8b3229f-36e0-401a-abad-48fc79f33589)

Nesse caso, poderia ficar preso em um loop onde a fronteira visita o nó A e depois o B, ficando presa nesse loop.

Para resolvermos esse problema, faremos o seguinte. Usaremos uma estrutura de dados auxiliar para armazenar o nós já visitados. Assim, quando formos adicionar um novo nó a fronteira, vamos verificar se ele não está na fronteira e na lista de nós já visitados, caso não esteja em nenhuma das duas, podemos adicionar o nó a fronteira.

************************Tipos de busca:************************

Falamos anteriormente que a ordem em que removemos os Nós faz diferença na busca, chegou o momento em que devemos falar sobre isso. Temos dois tipos de buscas básicas, essas duas estrategias são marcadas pelo tipo de estrutura usamos na fronteira, vamos falar sobre.

- Busca em profundidade:
    
    Essa estratégia pilhas para construir a fronteira, assim, o último a entrar é o último a sair. Essa estratégia faz com que a busca explore um caminho completamente, indo cada vez mais fundo até chegar nas folhas.
    
 ![1 bOxDNmWX_nL4W4qB-ey0VQ](https://github.com/kpzinnm/IACS50/assets/100965133/279838dc-4c96-48fa-8e45-ef8b55e3469f)

    
Essa estratégia possibilita achar o melhor caminho o mais rápido possível, isso se tivermos sorte. Entretanto, é muito possível cairmos no pior caso.
    
- Busca em largura:
    
    Essa estratégia, usa uma fila para construir a fronteira, onde o primeiro a entrar é o primeiro a sair. Assim, exploramos todos os caminhos possíveis, antes de irmos mais fundo no grafo. 
    
![Breadth-First-Search-Algorithm](https://github.com/kpzinnm/IACS50/assets/100965133/e7bd9853-f87b-4fa0-aa17-a28634d84109)

    
Com essa estratégia, dificilmente vamos resolver o problema no menor caso possível. Mas com ela, podemos resolver a maioria dos problemas em um tempo média, ou seja, dificilmente cai no pior caso.

---
Creditos a CS50's Introduction to Artificial Intelligence with Python, por HarvardX CS50AI
