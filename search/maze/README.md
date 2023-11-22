Primeiramente, vamos dar uma breve introdução ao algoritmo de busca. Imagine que temos que criar um algortimo que resolva um quebra-cabeça de 15 números, então recebemos um estado inicial contendo o estado no qual o problema vai começar:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/141662f0-3213-4fc7-ad15-0e8cd66dd4a5/bbee75a6-4cef-4036-96d6-182eb9d310e2/Untitled.png)

Esse é o nosso estado inicial, o agente é quem recebe esse estado. Agora, vamos mostrar dizer ao algoritmo qual é o estado desejado:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/141662f0-3213-4fc7-ad15-0e8cd66dd4a5/06c74523-aa71-424b-b302-922c03a008a8/Untitled.png)

Esse é o estado que nosso algoritmo deve chegar. O nosso desafio é fazer o agente sair do estado inicial até o final. Mas, como fazemos isso?

---

A primeira coisa que o agente deve fazer é analisar quais são as ações possíveis, no nosso exemplo, o agente pode mover o 12 para baixo ou o 15 para a direita. Essas duas ações vão gerar dois novos estados que são filhos do estado anterior. Cada novo estado realizar o mesmo processo, assim teremos 4 novos estados. Com isso, estamos formando um grafo de árvore:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/141662f0-3213-4fc7-ad15-0e8cd66dd4a5/9e701c60-46d6-4211-8212-2717035cfed8/Untitled.png)

---

Com essa estrutura em mãos, vamos fazer com que cada folha desenvolva as ações possíveis. 

- Nós: cada nó na árvore possui algumas informações essenciais para achar a solução do problema:
    - Um estado, ou melhor, o estado atual;
    - Seu nó pai, ou seja, aquele que o gerou;
    - A ação que foi aplicada nele;
    - O custo para chegar até o estado atual.

Com essas informações em mãos, podemos obter o resultado. Primeiro, comparamos se o estado atual do nó é o estado desejado, caso seja, analisamos o custo e o comparamos com outros nós que chegaram até o estado desejado, para obtermos a solução mais eficiente. Além disso, conseguimos rastrear os passos até o estado inicial, você pergunta: Como? A resposta é simples, pegamos a ação que o nó pai realizou para chegar até o estado, armazenamos em uma pilha, pegamos o nó pai e fazemos o mesmo, armazenamos a sua ação na pilha e vamos para o seu pai. Fazemos isso até chegar no estado inicial. Assim, teremos o passo a passo na ordem correta para ir do estado inicial até o estado final. 

Com isso, temos uma noção básica de como esse algoritmo funciona, o próximo passo é implementarmos um algoritmo de busca, passando pelo passo a passo.