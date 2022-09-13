from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa, BuscaCustoUniforme
from aicode.search.Graph import State

class ProblemSpecification(State):

    def __init__(self, cid_fim, cid_atual, custo, op):
        #self.cid_inicio = cid_inicio
        self.cid_fim = cid_fim
        self.cid_atual = cid_atual
        self.custo = custo
        self.operator = op
        
    
    def sucessors(self):
        sucessors = []
        mapa = self.createArea()
        for t in mapa[self.cid_atual]:
            sucessors.append(ProblemSpecification(self.cid_fim, t[1], self.custo+t[0], f'Da cidade {self.cid_atual} para {t[1]}, custo atual {self.custo+t[0]}'))

        return sucessors
    
    def is_goal(self):
        if self.cid_atual == self.cid_fim:
            return True
        return False
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

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
        None

    #@staticmethod
    def createArea(self):
        #
        # TODO mover a definicao do mapa de uma forma hard-coded para para leitura
        # a partir de um arquivo, similar ao que é feito no metodo createHeuristics()
        # 
        Mapa = {
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
        return Mapa



def main():
    print('Busca em profundidade iterativa')
    #cid_inicio = 'o'
    cid_fim = 'i'
    cid_atual = 'o'
    custo = 0
    state = ProblemSpecification(cid_fim, cid_atual, custo, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    print('Busca Custo Uniforme')
    #cid_inicio = 'o'
    cid_fim = 'i'
    cid_atual = 'o'
    custo = 0
    state = ProblemSpecification(cid_fim, cid_atual, custo, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()