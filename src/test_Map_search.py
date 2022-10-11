from sre_parse import State
from aicode.search.SearchAlgorithms import BuscaLargura, AEstrela, BuscaProfundidade
from Map import Map


def test_AEstrela():

    Map.createArea()
    Map.createHeuristics()

    state = Map('i', 0, 'i', 'x')
    algorithm = AEstrela()
    result = algorithm.search(state)


    assert(result.show_path() == "i ; e ; m ; x")

def test_BuscaLargura():

    Map.createArea()
    Map.createHeuristics()

    state = Map('i', 0, 'i', 'x')
    algorithm = BuscaLargura()
    result = algorithm.search(state)


    assert(result.show_path() == "i ; e ; m ; x")

def test_BuscaProfundidade():

    Map.createArea()
    Map.createHeuristics()

    state = Map('i', 0, 'i', 'x')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)


    assert(result.show_path() == "i ; h ; k ; b ; k ; b ; k ; n ; m ; x")