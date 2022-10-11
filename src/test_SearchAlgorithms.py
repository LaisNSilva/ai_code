from aicode.search.Graph import State
from aicode.search.SearchAlgorithms import *
from aicode.search.Graph import Node
from VacuumWorld import *
from U2 import U2
from collections import deque
import logging
logging.basicConfig(filename='search_algorithms.log', level=logging.DEBUG)
from aicode.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaProfundidadeIterativa

def test_BuscaLargura():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != 0

def test_BuscaLargura():
    Map.createArea()
    Map.createHeuristics()

    print('Busca por algoritmo Busca Largura: sair de l e chegar em h')
    state = Map('l', 0, 'l', 'h')
    algorithm = BuscaLargura()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    print((tf-ts))
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 2 and result.g == 5

def test_BuscaProfundidade():
    Map.createArea()
    Map.createHeuristics()

    print('Busca por algoritmo Busca Profundidade: sair de l e chegar em h -- em até 2 ações')
    state = Map('l', 0, 'l', 'h')
    algorithm = BuscaProfundidade()
    ts = time.time()
    result = algorithm.search(state,2)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 2 and result.g == 5

    print('Busca por algoritmo Busca Profundidade: sair de l e chegar em h -- em até 3 ações')
    state = Map('l', 0, 'l', 'h')
    algorithm = BuscaProfundidade()
    ts = time.time()
    result = algorithm.search(state,3)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 3 and result.g == 7

def test_BuscaAEstrela():
    Map.createArea()
    Map.createHeuristics()

    print('Busca por algoritmo Busca A*: sair de l e chegar em x')
    state = Map('l', 0, 'l', 'x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 4 and result.g == 7

    print('Busca por algoritmo Busca A*: sair de c e chegar em x')
    state = Map('c', 0, 'c', 'x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 6 and result.g == 14

def test_BuscaLargura():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if (result == None):
      print('Sem solução!')
    assert result.g != 0  and result.show_path() == " ; clean ; Move Left ; clean"

def test_BuscaProfundidade():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if (result == None):
      print('Sem solução!')
    assert result.g != 0 and result.show_path() == " ; clean ; clean ; clean ; clean ; clean ; clean ; clean ; clean ; Move Left ; clean"

def test_BuscaProfundidadeIterativa():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if (result == None):
      print('Sem solução!')
    assert result.g != 0 and result.show_path() == " ; clean ; Move Left ; clean"

def test_BuscaLargura():
    print('\nBusca em Largura')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print("custo",result.g)
    assert result.g >= 17

def test_BuscaProfundidade():
    print('\nBusca em Profundidade')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 20)
    print("custo",result.g)
    assert result.g > 17

def test_BuscaCustoUniforme():
    print('\nBusca de Custo Uniforme')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    print("custo",result.g)
    assert result.g <= 17

# teste para BuscaLargura
def testeBuscaLargura():
    state = VacuumWorld('right', False, True, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None and result.g == 2
    print(result.show_path())

# teste para BuscaProfundidade
def testeBuscaProfundidade():
    state = VacuumWorld('right', True, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 300)
    print(result.g)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != 0

def test_BuscaProfundidadeIterativa():
    state = VacuumWorld('right', False, False, '')
    assert result.g != None and result.g == 300
    print(result.show_path())

# teste para BuscaProfundidadeIterativa
def testeBuscaProfundidadeIterativa():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None and result.g == 3
    print(result.show_path())

def test_none_father_node():
    """
    Testing attributes of a none-father Node.
    Depth and Cost (g) should be 0!
    """
    file_map_path = "data/vacuum_simple_0.txt"
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, "")
    print("State: ", state)
    n = Node(state, None)
    assert (n.depth == 0) and (n.g == 0)

def test_BPI_node_parents():
    """
    Testing if BPI is creating only 2 Nodes.
    The node n1 should have n2 as a father
    The node n2 sould have None on fatther_node attribute!
    """
    print("\n#### BPI Node Parents ####")
    file_map_path = "data/vacuum_simple_1.txt"
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, "")
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    n1 = algorithm.search(state).father_node
    n2 = n1.father_node
    assert n2 == None

