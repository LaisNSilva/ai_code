#
# Implements a solution for N-queens problem, where N could 
# be any number between 4 and 10.
#

from aicode.search.CSPAlgorithms import SubidaMontanha
from aicode.search.CSPAlgorithms import SubidaMontanhaEstocastico
from aicode.search.Graph import State
import numpy as np
import random
import time

class N_QueensProblem(State):

    def __init__(self, size, board):
        self.size = size
        self.board = board

    def env(self):
        return self.board
    
    def sucessors(self):
        sucessores = []
        for i in range(0,self.size):
            for j in range(0,self.size):
                if(self.board[i][j] == 1):
                    #move up
                    if((i - 1) >=0 and self.board[i-1][j] == 0):
                        temp = self.board.copy()
                        temp[i][j] = 0
                        temp[i-1][j] = 1
                        sucessores.append(N_QueensProblem(self.size, temp))
                    #move down
                    if((i + 1) < self.size and self.board[i+1][j] == 0):
                        temp = self.board.copy()
                        temp[i][j] = 0
                        temp[i+1][j] = 1
                        sucessores.append(N_QueensProblem(self.size, temp))
                    #move left
                    #if((j - 1) >=0 and self.board[i][j-1] == 0):
                    #    temp = self.board.copy()
                    #    temp[i][j] = 0
                    #    temp[i][j-1] = 1
                    #    sucessores.append(N_QueensProblem(self.size, temp))
                    #move right
                    #if((j + 1) < self.size and self.board[i][j+1] == 0):
                    #    temp = self.board.copy()
                    #    temp[i][j] = 0
                    #    temp[i][j+1] = 1
                    #    sucessores.append(N_QueensProblem(self.size, temp))
        return sucessores
                      
    def is_goal(self):
        if self.h() == 0:
            return True
        return False
    
    def description(self):
        return "Queens Problem"
    
    def cost(self):
        return 1

    def print(self):
        pass
    
    def h(self):
        #TODO
        r = 0
        # checar linhas, colunas e diagonais
        # linhas
        for l in self.board:
            c = l.count(1)
            if c > 1:
                r+= c

        #colunas
        for i in range(len(self.board[0])): #quantidade de colunas
            c_col = 0
            for l in self.board:
                if l[i]==1:
                    c_col+=1
            if c_col>1:
                r+=c_col

        #diagonais
        diag_prin = np.diag(self.board)
        c = diag_prin.count(1)
        if c > 1:
            r+= c
        for i in range(len(self.board[0])-2):
            d = np.diag(self.board, i)
            c = d.count(1)
            if c > 1:
                r+= c
            d = np.diag(self.board, -i)
            c = d.count(1)
            if c > 1:
                r+= c

        diag_prin = np.fliplr(self.board).diag()
        c = diag_prin.count(1)
        for i in range(len(self.board[0])-2):
            d = np.fliplr(self.board).diag(i)
            c = d.count(1)
            if c > 1:
                r+= c
            d = np.fliplr(self.board).diag(-i)
            c = d.count(1)
            if c > 1:
                r+= c
        return r

    def randomState(self):
        self.board = self.generateBoard()
        while not self.validBoard():
            self.board = self.generateBoard()

    def generateBoard(self):
        board = np.zeros( (self.size,self.size) )
        for i in range(0,self.size):
            line = random.randrange(0, self.size)
            #column = random.randrange(0, self.size)
            board[line,i] = 1
        return board

    def validBoard(self):
        if np.sum(self.board) != self.size:
            return False
        return True

def main():
    N = int(input("Digite o tamanho do tabuleiro (4-10): "))
    state = N_QueensProblem(size = N, board = None)
    state.randomState()
    algorithm = SubidaMontanhaEstocastico()
    print("Initial state with h = "+str(state.h()))
    start = time.time()
    result = algorithm.search(state)
    end = time.time()
    if result != None:
        print(result.env())
        print('Final state with h = '+str(result.h()))
        print('Duration in seconds = '+str(end-start))
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()