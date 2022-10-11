from aicode.search.SearchAlgorithms import BuscaLargura
from aicode.search.SearchAlgorithms import BuscaProfundidade
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from VacuumWorldGeneric import *

def test_largura_simple_1_path():
    print("\n#### Largura Simples 1 ####")
    file_map_path = "data/vacuum_simple_1.txt"
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, "")
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f"Solução = {result.show_path()}")
    print("\n")
    assert result.show_path() == " ; limpar"

def test_largura_simple_2_path():
    print("\n#### Largura Simples 2 Path ####")
    file_map_path = "data/vacuum_simple_2.txt"
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, "")
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f"Solução = {result.show_path()}")
    print("\n")
    assert result.show_path() == " ; dir ; dir ; baixo ; limpar"

def test_largura_simple_3_path():
    print("\n#### Largura Simples 3 ####")


file_map_path = "data/vacuum_simple_3.txt"
lin = 0
col = 0
mapa = convert_file_to_map(file_map_path)
print(mapa)
state = VacuumWorldGeneric(mapa, lin, col, "")
algorithm = BuscaLargura()
result = algorithm.search(state)
print(f"Solução = {result.show_path()}")
print("\n")
assert (
    result.show_path()
    == " ; dir ; dir ; baixo ; limpar ; dir ; limpar ; baixo ; limpar"
)

def test_largura_simple_0():
    print('\n#### Largura Simples 0 ####')
    file_map_path = 'data/vacuum_simple_0.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.show_path() == ""

def test_largura_simple_1():
    print('\n#### Largura Simples 1 ####')
    file_map_path = 'data/vacuum_simple_1.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    #assert result.show_path() == " ; limpar"
    assert result.g == 1

def test_largura_simple_2():
    print('\n#### Largura Simples 2 ####')
    file_map_path = 'data/vacuum_simple_2.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 4

def test_largura_simple_3():
    print('\n#### Largura Simples 3 ####')
    file_map_path = 'data/vacuum_simple_3.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 8

def test_largura_simple_4():
    print('\n#### Largura Simples 4 ####')
    file_map_path = 'data/vacuum_simple_4.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 10

def test_largura_simple_6():
    print('\n#### Largura Simples 6 ####')
    file_map_path = 'data/vacuum_simple_6.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 23

def test_largura_simple_7():
    print('\n#### Largura Simples 7 ####')
    file_map_path = 'data/vacuum_simple_7.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 16

def test_largura_simple_8():
    print('\n#### Largura Simples 8 ####')
    file_map_path = 'data/vacuum_simple_8.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14

def test_largura_simple_9():
    print('\n#### Largura Simples 9 ####')
    file_map_path = 'data/vacuum_simple_9.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 15

def test_largura_simple_10():
    print('\n#### Largura Simples 10 ####')
    file_map_path = 'data/vacuum_simple_10.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 5

def test_largura_simple_11():
    print('\n#### Largura Simples 11 ####')
    file_map_path = 'data/vacuum_simple_11.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14



#
# Para executar um script como um todo talvez você tenha que comentar este teste.
#
# def test_largura_simple_5():
#     print('\n#### Largura Simples 5 ####')
#     file_map_path = 'data/vacuum_simple_5.txt'
#     lin = 0
#     col = 0
#     mapa = convert_file_to_map(file_map_path)
#     print(mapa)
#     state = VacuumWorldGeneric(mapa, lin, col, '')
#     algorithm = BuscaLargura()
#     print('Se prepara que este vai demorar! Vale a pena monitorar o consumo de memória!!!')
#     result = algorithm.search(state)
#     print(f'Solução = {result.show_path()}')
#     print('\n')
#     assert result.g == 10

#
# Profundidade
#

def test_profundidade_simple_0():
    print('\n#### profundidade Simples 0 ####')
    file_map_path = 'data/vacuum_simple_0.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 25)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.show_path() == ""

def test_profundidade_simple_1():
    print('\n#### profundidade Simples 1 ####')
    file_map_path = 'data/vacuum_simple_1.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 25)
    print(f'Solução = {result.show_path()}')
    print('\n')
    #assert result.show_path() == " ; limpar"

def test_profundidade_simple_2():
    print('\n#### profundidade Simples 2 ####')
    file_map_path = 'data/vacuum_simple_2.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 25)
    print(f'Solução = {result.show_path()}')
    print('\n')
    #assert result.g == 24

def test_profundidade_simple_3():
    print('\n#### profundidade Simples 3 ####')
    file_map_path = 'data/vacuum_simple_3.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 25)
    print(f'Solução = {result.show_path()}')
    print('\n')
    #assert result.g == 25

def test_profundidade_simple_4():
    print('\n#### profundidade Simples 4 ####')
    file_map_path = 'data/vacuum_simple_4.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 25)
    print(f'Solução = {result.show_path()}')
    print('\n')
    #assert result.g == 25

def test_profundidade_simple_5():
    print('\n#### profundidade Simples 5 ####')
    file_map_path = 'data/vacuum_simple_5.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    print('Se prepara que este vai demorar! Vale a pena monitorar o consumo de memória!!!')
    result = algorithm.search(state, 25)
    print(f'Solução = {result.show_path()}')
    print('\n')
    #assert result.g == 25

def test_profundidade_simple_6():
    print('\n#### Profundidade Simples 6 ####')
    file_map_path = 'data/vacuum_simple_6.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 23

def test_profundidade_simple_7():
    print('\n#### Profundidade Simples 7 ####')
    file_map_path = 'data/vacuum_simple_7.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 16

def test_profundidade_simple_8():
    print('\n#### Largura Simples 8 ####')
    file_map_path = 'data/vacuum_simple_8.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14

def test_profundidade_simple_9():
    print('\n#### Largura Simples 9 ####')
    file_map_path = 'data/vacuum_simple_9.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 15

def test_profundidade_simple_10():      
    print('\n#### Largura Simples 10 ####')
    file_map_path = 'data/vacuum_simple_10.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 5

def test_profundidade_simple_11():
    print('\n#### Largura Simples 11 ####')
    file_map_path = 'data/vacuum_simple_11.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14


def test_profundidade_xadrez():
    print('\n#### profundidade Xadrez ####')
    file_map_path = 'data/vacuum_xadrez.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    print('Se prepara que este vai demorar! Vale a pena monitorar o consumo de memória!!!')
    result = algorithm.search(state, 25)
    print(f'Solução = {result.show_path()}')
    print(f"G = {result.g}")
    print('\n')
    assert result.g == 25

def test_profundidade_corners():
    print('\n#### profundidade Corners ####')
    file_map_path = 'data/vacuum_corners.txt'
    lin = 1
    col = 2
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidade()
    print('Se prepara que este vai demorar! Vale a pena monitorar o consumo de memória!!!')
    result = algorithm.search(state, 15)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 15


#
# BPI
#

def test_BPI_simple_0():
    print('\n#### BPI Simples 0 ####')
    file_map_path = 'data/vacuum_simple_0.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.show_path() == ""

def test_BPI_simple_1():
    print('\n#### BPI Simples 1 ####')
    file_map_path = 'data/vacuum_simple_1.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    #assert result.show_path() == " ; limpar"
    assert result.g == 1

def test_BPI_simple_2():
    print('\n#### BPI Simples 2 ####')
    file_map_path = 'data/vacuum_simple_2.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 4

def test_BPI_simple_3():
    print('\n#### BPI Simples 3 ####')
    file_map_path = 'data/vacuum_simple_3.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 8

def test_BPI_simple_4():
    print('\n#### BPI Simples 4 ####')
    file_map_path = 'data/vacuum_simple_4.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 10

def test_BPI_simple_5():
    print('\n#### BPI Simples 5 ####')
    file_map_path = 'data/vacuum_simple_5.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    print('Se prepara que este vai demorar! Vale a pena monitorar o consumo de memória!!!')
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 15

def test_BPI_simple_6():
    print('\n#### BPI Simples 6 ####')
    file_map_path = 'data/vacuum_simple_6.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 23

def test_BPI_simple_7():
    print('\n#### BPI Simples 7 ####')
    file_map_path = 'data/vacuum_simple_7.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 16

def test_BPI_simple_8():
    print('\n#### BPI Simples 8 ####')
    file_map_path = 'data/vacuum_simple_8.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14

def test_BPI_simple_9():
    print('\n#### BPI Simples 9 ####')
    file_map_path = 'data/vacuum_simple_9.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 15

def test_BPI_simple_10():
    print('\n#### BPI Simples 10 ####')
    file_map_path = 'data/vacuum_simple_10.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 5

def test_BPI_simple_11():
    print('\n#### BPI Simples 11 ####')
    file_map_path = 'data/vacuum_simple_11.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')
    assert result.g == 14