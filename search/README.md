Primeiramente, vamos dar uma breve introdução ao algoritmo de busca. Imagine que temos que criar um algortimo que resolva um quebra-cabeça de 15 números, então recebemos um estado inicial contendo o estado no qual o problema vai começar:

![image](https://github.com/kpzinnm/IACS50/assets/100965133/a7deb717-4db7-4bb9-b74a-45c83a9abb05)


Esse é o nosso estado inicial, o agente é quem recebe esse estado. Agora, vamos mostrar dizer ao algoritmo qual é o estado desejado:

![Captura de tela de 2023-10-23 09-29-24](https://github.com/kpzinnm/IACS50/assets/100965133/be75eaac-b48d-4be4-b08f-ba974fd80676)

Esse é o estado que nosso algoritmo deve chegar. O nosso desafio é fazer o agente sair do estado inicial até o final. Mas, como fazemos isso?

---

A primeira coisa que o agente deve fazer é analisar quais são as ações possíveis, no nosso exemplo, o agente pode mover o 12 para baixo ou o 15 para a direita. Essas duas ações vão gerar dois novos estados que são filhos do estado anterior. Cada novo estado realizar o mesmo processo, assim teremos 4 novos estados. Com isso, estamos formando um grafo de árvore:

![Captura de tela de 2023-10-23 09-35-34](https://github.com/kpzinnm/IACS50/assets/100965133/aa3380bf-575b-4bae-8a86-cce43428109b)

---

Com essa estrutura em mãos, vamos fazer com que cada folha desenvolva as ações possíveis. 

- Nós: cada nó na árvore possui algumas informações essenciais para achar a solução do problema:
    - Um estado, ou melhor, o estado atual;
    - Seu nó pai, ou seja, aquele que o gerou;
    - A ação que foi aplicada nele;
    - O custo para chegar até o estado atual.

Com essas informações em mãos, podemos obter o resultado. Primeiro, comparamos se o estado atual do nó é o estado desejado, caso seja, analisamos o custo e o comparamos com outros nós que chegaram até o estado desejado, para obtermos a solução mais eficiente. Além disso, conseguimos rastrear os passos até o estado inicial, você pergunta: Como? A resposta é simples, pegamos a ação que o nó pai realizou para chegar até o estado, armazenamos em uma pilha, pegamos o nó pai e fazemos o mesmo, armazenamos a sua ação na pilha e vamos para o seu pai. Fazemos isso até chegar no estado inicial. Assim, teremos o passo a passo na ordem correta para ir do estado inicial até o estado final. 

Com isso, temos uma noção básica de como esse algoritmo funciona, o próximo passo é implementarmos um algoritmo de busca, passando pelo passo a passo.
