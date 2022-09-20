from aicode.search.SearchAlgorithms import BuscaGananciosa, BuscaCustoUniforme, BuscaProfundidadeIterativa
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.SearchAlgorithms import BuscaCustoUniforme
from aicode.search.SearchAlgorithms import BuscaGananciosa
from aicode.search.SearchAlgorithms import AEstrela
from aicode.search.Graph import State
import time
import networkx as nx
import csv

class Map(State):

    # def __init__(self, cid_fim, cid_atual, custo, op):
    #     #self.cid_inicio = cid_inicio
        
    #     self.cid_fim = cid_fim
    #     self.cid_atual = cid_atual
    #     self.custo = custo
    #     self.operator = op
        
    
    # def sucessors(self):
    #     sucessors = []
    #     for t in Map.area[self.cid_atual]:
    #         sucessors.append(Map(self.cid_fim, t[1], t[0], f'Da cidade {self.cid_atual} para {t[1]}, custo atual {self.custo+t[0]}'))

    def __init__(self, city, cost, op, goal):
        self.city = city
        self.cost_value = cost
        self.operator = op
        self.goal = goal
    
    def sucessors(self):
        sucessors = []
        neighbors = Map.area[self.city]
        for next_city in neighbors:
            sucessors.append(Map(next_city[1], next_city[0], next_city[1], self.goal))
        return sucessors
    
    def is_goal(self):
        if self.cid_atual == self.cid_fim:
            return True
        return False
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        # return self.custo

        #return the cost to get at city "city"
        return self.cost_value
    
    def print(self):
        #
        # Usado para imprimir a solução encontrada. 
        # O PATH do estado inicial até o final.
        return str(self.operator)
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return str(self.cid_atual)

    def h(self):
        # dado a minha cidadde atual, qual é a estimativa para chegar no objetivo
        # Map.g
        return int(Map.g.edges[self.cid_atual, self.cid_fim]['distance'])
        return self.city
        #return self.city+"#"+str(self.cost())

    # def h(self):
    #     return int(Map.g.edges[self.city,self.goal]['distance'])
    #     #return random.randint(1,10)
    #     #return 1

    @staticmethod
    def createArea():
        #
        # TODO mover a definicao do mapa de uma forma hard-coded para para leitura
        # a partir de um arquivo, similar ao que é feito no metodo createHeuristics()
        # 
        Map.area = {
            'a':[(3,'b'),(6,'c')],
            'b':[(3,'a'),(3,'h'),(3,'k')],
            'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
            'd':[(3,'c'),(1,'f'),(1,'e')],
            'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
            'f':[(1,'g'),(1,'e'),(1,'d')],
            'g':[(2,'c'),(1,'f'),(2,'h')],
            'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
            'i':[(2,'e'),(2,'h')],
            'l':[(1,'k')],
            'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
            'm':[(2,'n'),(1,'x'),(14,'e')],
            'n':[(2,'m'),(3,'k')],
            'o':[(2,'c')],
            'p':[(2,'c')],
            'x':[(1,'m')]
            }

    @staticmethod
    def createHeuristics():
        #
        # O arquvo MapHeuristics.csv considera apenas os objetivos "o" e "x"
        # TODO modificar o arquivo para considerar todas as cidades. talvez modificar
        # a estrutura do arquivo considerando uma estrutura otimizada
        #
        Map.g = nx.Graph()
        f = csv.reader(open("data/MapHeuristics.csv","r"))
        for row in f: 
            Map.g.add_edge(row[0],row[1], distance = row[2])


def main():

    Map.createArea()
    Map.createHeuristics()
    
    cid_fim = 'x'
    cid_atual = 'i'
    custo = 0

    print('Busca em profundidade iterativa')
    #cid_inicio = 'o'
    cid_fim = 'x'
    cid_atual = 'i'
    custo = 0
    state = Map(cid_fim, cid_atual, custo, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    print('Busca Custo Uniforme')
    #cid_inicio = 'o'
    
    
    state = Map(cid_fim, cid_atual, custo, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    print(f'Busca por algoritmo A*: sair de {cid_atual} e chegar em {cid_fim}')
    state = Map(cid_fim, cid_atual, custo, '')
    algorithm = AEstrela()
    #algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    

if __name__ == '__main__':
    main()
