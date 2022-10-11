#Quando quiser saber o caminho, passar a flag -s para o pytest
#pytest -s src/test_Map.py

from aicode.search.SearchAlgorithms import AEstrela
import time 
from Map import *

Map.createArea()
Map.createHeuristics()

def test_menor_caminho_d_ate_o():    
    state = Map('f', 0, 'f', 'o')      
    algorithm = AEstrela()
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

def test_is_goal_retorna_corretamente_0():
    print('\n#### Test metodo is_goal retorna corretamente 0 ####')
    state = Map('i', 0, 'i', 'x')
    assert state.is_goal() == False

def test_is_goal_retorna_corretamente_1():
    print('\n#### Test metodo is_goal retorna corretamente 1 ####')
    state = Map('i', 0, 'i', 'i')
    assert state.is_goal() == True

def test_successors_retorna_corretamente():
    print('\n#### Test metodo successors retorna sucessores corretamente ####')
    state = Map('i', 0, 'i', 'x').sucessors()
    expected_values = [
        {'city': 'e', 'cost_value': 2, 'operator': 'e', 'goal': 'x'},
        {'city': 'h', 'cost_value': 2, 'operator': 'h', 'goal': 'x'}
    ]
    for i in range(len(expected_values)):
        assert expected_values[i] == state[i].__dict__

def test_algoritmo_encontra_solucao_existente():
    print('\n#### Teste algoritmo encontra solucao que existe ####')
    state = Map('i', 0, 'i', 'x')
    algorithm = AEstrela()
    res = algorithm.search(state)
    assert res != None

def test_algoritmo_encontra_melhor_solucao_possivel_a_o():
    print('\n#### Teste algoritmo encontra solucao de a para o ####')
    state = Map('a', 0, 'a', 'o')
    algorithm = AEstrela()
    res = algorithm.search(state)
    assert res.g == 8

def test_algoritmo_encontra_melhor_solucao_possivel_n_x():
    print('\n#### Teste algoritmo encontra solucao de n para x ####')
    state = Map('n', 0, 'n', 'x')
    algorithm = AEstrela()
    res = algorithm.search(state)
    assert res.g == 3

def test_a_x():
    state = Map('a',0, 'a','x')
    algorithm = AEstrela()
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
    assert result.g == 12
    print(result.show_path())
    
def test_menor_caminho_n_ate_x():
    state = Map('n', 0, 'n', 'x')
    algorithm = AEstrela()
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
    assert result.g == 5
    print(result.show_path())

def test_menor_caminho_e_ate_x():
    state = Map('e', 0, 'e', 'x')     
    algorithm = AEstrela()
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
    assert result.g == 3
    print(result.show_path()) 

def test_b_x():
    state = Map('b',0, 'b','x')
    algorithm = AEstrela()
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
    assert result.g == 9
    print(result.show_path())

def test_menor_caminho_l_ate_o():
    state = Map('l', 0, 'l', 'o')
    algorithm = AEstrela()
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
    assert result.g == 14
    print(result.show_path())

def test_menor_caminho_k_ate_o():
    state = Map('k', 0, 'k', 'o')   #primeiro,0,primeiro,ultimo
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
    assert result.g == 11
    print(result.show_path())

def test_c_o():
    state = Map('c',0, 'c','o')
    algorithm = AEstrela()
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
    assert result.g == 10
    print(result.show_path())
    assert result.g == 2

def test_menor_caminho_x_ate_o():
    state = Map('x', 0, 'x', 'o')
    algorithm = AEstrela()
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
    assert result.g == 16
    print(result.show_path())

