from sre_parse import State
from aicode.search.SearchAlgorithms import BuscaLargura
from Map import Map



def test_partida_eq_chegada():

    state = Map('i', 0, 'x', 'i')
    assert(state.is_goal())

def test_partida_dif_chegada():

    state = Map('i', 0, 'x', 'b')
    assert(not state.is_goal())

def test_custo_0():

    state = Map('a', 0, 'a', 'x')
    assert(state.cost() == 0)

def test_custo_1():

    state = Map('a', 1, 'a', 'x')
    assert(state.cost() == 1)


def test_sucessores_a():

    Map.createArea()
    Map.createHeuristics()

    state = Map('a', 1, 'a', 'x')
    target = [
        Map('b', 3, 'b' , 'x'),
        Map('c', 6, 'c' , 'x'),
    ]

    sucessors = state.sucessors()

    for i in range(len(sucessors)):
        assert(sucessors[i].print() == target[i].print())

def test_sucessores_c():

    Map.createArea()
    Map.createHeuristics()

    state = Map('c', 1, 'c', 'x')
    target = [
        Map('a', 6, 'a', 'x'),
        Map('g', 2, 'g', 'x'),
        Map('d', 3, 'd', 'x'),
        Map('o', 2, 'o', 'x'),
        Map('p', 2, 'p', 'x'),
    ]
    
    sucessors = state.sucessors()

    for i in range(len(sucessors)):
        assert(sucessors[i].print() == target[i].print())