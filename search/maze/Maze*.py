"""
Vamos agora fazer a implementação do algoritmo A* search, aplicando no contexto no Maze
A modificação que faremos é a implementação de uma função heurística que leva em consideração
a distância do estado atual até o estado destino e a quantidade de passos que ele precisou para chegar
até o estado atual. Com essa estrategia, vamos tentar otimizar o processo da busca pelo melhor caminho.
"""
class Node():
    def __init__(self, state, action, parent, distance, steps):
        self.state = state
        self.action = action
        self.parent = parent
        self.distance = distance
        self.steps = steps
        self.heuristic = distance + steps

    def __eq__(self, other):
        if(isinstance(other, Node)):
            return self.state == other.state
        return False

class Maze():
    def __init__(self, filename):
        with open(filename,'r') as arquivo:
            conteudo = arquivo.read()

        self.conteudo = conteudo.split('\n')
        self.height = len(self.conteudo) 
        self.width = len(self.conteudo[0])
        self.finalState = (0,0)
        self.initialState = (0,0)  
       
       # Define o ponto inicial e final
        for i in range(self.height):
            for j in range(self.width):
                if(self.conteudo[i][j] == 'B'):
                    self.finalState = (i,j)
                elif(self.conteudo[i][j] == 'A'):
                    self.initialState = (i,j)

    def getInitialState(self):
        return self.initialState
    
    def getFinalState(self):
        return self.finalState
    
class Frontier():

    def __init__(self, filename):
        self.maze = Maze(filename=filename)
        self.frontier = []
        self.exploreSet = []
    
        if(len(self.frontier) == 0 and len(self.exploreSet) == 0):
            state = self.maze.getInitialState()
            self.add(self.create_Node(state=state, action="None", parent="None"))

    # Adiciona um nó na fronteira
    def add(self, node):
        if(node not in self.frontier and node.state not in self.exploreSet):
            self.frontier.append(node)
    
    # Remove e retorna o ultimo elemento a entrar da fronteira, estamos usando a estrategia
    # de busca em profundidade
    def remove(self):
        node = min(self.frontier, key=lambda x: x.heuristic)
        self.frontier.remove(node)
        self.exploreSet.append(node.state)
        return node
    
    # Cria um nó
    def create_Node(self, state, action, parent): 
        steps = 0
        if(parent != "None"):
            steps = parent.steps+1
        node = Node(state=state, action=action, parent=parent, distance=self.heuristic(state), steps=steps)
        #node.steps = parent.steps+1
        return node
    
    # Define o conjunto de acoes que podem ser feitas a partir de um nó
    def actions(self, node):
        y, x = node.state
        candidates = [
            ("UP", (y+1,x)),
            ("DOWN", (y-1,x)),
            ("LEFT", (y,x-1)),
            ("RIGHT", (y,x+1))
        ]

        set_actions = []

        for action, (r,c) in candidates:
            if((r >= 0 and r < self.maze.height and c >= 0 and c < self.maze.width) and (self.maze.conteudo[r][c] == " " or self.maze.conteudo[r][c] == "B")):
                set_actions.append(self.create_Node((r,c),(action,(r,c)),node))

        return set_actions
 
    def goal_Test(self, node):
        if(self.maze.finalState == node.state):
            return True
        
    def heuristic(self, state):
        heuristic = abs(state[0]-self.maze.finalState[0])+abs(state[1]-self.maze.finalState[1])
        print(heuristic)
        return heuristic


    def empty(self):
        return len(self.frontier) == 0
    
    def path_maze(self, node):
        
        while(not node.__eq__(self.maze.initialState)):
            linha = list(self.maze.conteudo[node.state[0]])
            if (linha[node.state[1]] != "A" and linha[node.state[1]] != "B"):
                linha[node.state[1]] = "█"
            self.maze.conteudo[node.state[0]] = "".join(linha)
            node = node.parent

        for i in self.maze.conteudo:
            print(i)
    

class main():
    def __init__(self, filename):
        self.frontier = Frontier(filename=filename)

    def run_frontier(self):
        while(not self.frontier.empty()):
            # remove um nó da fronteira
            node = self.frontier.remove()
            #verifica se o nó retirado é o estado desejado
            if(self.frontier.goal_Test(node)):
                self.frontier.path_maze(node)
                break
            # expande o nó e adiciona os novos na fronteira
            set_actions = self.frontier.actions(node)
            for i in set_actions:
                self.frontier.add(i)
        
    

# Coloque o labirinto
m = main(filename='mazes/maze6.txt')
m.run_frontier()    
    
