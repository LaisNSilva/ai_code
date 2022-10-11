from aicode.search.SearchAlgorithms import BuscaGananciosa, sortFunction, BuscaCustoUniforme,BuscaLargura, BuscaProfundidade, BuscaProfundidadeIterativa
from VacuumWorld import VacuumWorld

def test_buscaLargura():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    assert result.show_path() == " ; clean ; Move Left ; clean"

def test_buscaLargura2():
    state = VacuumWorld('left', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    assert result.show_path() == " ; Move Right ; clean ; Move Left ; clean"

def test_buscaProfundidade():
    state = VacuumWorld('left', False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state,4)
    assert result.show_path() == " ; clean ; Move Right ; clean ; Move Left"
