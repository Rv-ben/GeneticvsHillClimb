# This is a chest board with 1 queen per row 
# This is part of the n-queens problem



"""
[2,4,5,1,5,3]

|-x----|
|---x--|
|----x-|
|x-----|
|----x-|
|--x---|
"""

import random

class board:

    n_queens = 0
    fitness  = 0
    boardArray = []

    def __init__(self,n):
        self.boardArray = random.sample(range(1,n+1),n)
        self.n_queens = n 
        self.calcFitness()

    def setNQueens(self, n):
        self.n_queens = n
    
    def setEncodedArray(self, array):
        self.boardArray =  array

    def getNQuenns(self):
        return self.n_queens

    def getEncodedArray(self):
        return self.boardArray

    def getFitness(self):
        return self.fitness

    def calcFitness(self):
        
        count = 0
        array = self.boardArray

        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if(array[i] + (j-i) == array[j]): # j-i = 0,1,2,...
                    count = count + 1
                if(array[i] - (j-i) == array[j]):
                    count = count + 1
                if(array[j] == array[i]):
                    count = count +1

        self.fitness = count

    def show(self):
        
        array = self.boardArray

        for i in range(0,len(array)):
            for j in range(1,len(array)+1):
                
                if(j == array[i]):
                    print("X",end='')
                else:
                    print("-",end='')
            print()

        print("Fitness: "+str(self.fitness))



x = board(6)
print(x.getEncodedArray())
x.show()