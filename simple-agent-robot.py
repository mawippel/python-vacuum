import matplotlib.pyplot as plt
import random

def exibir(I):
    plt.imshow(I, 'gray')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]]

def createWorld(m):
    for mI in range(1, 5):
        for aI in range(1, 5):
            number = random.randint(0, 3)
            m[mI][aI] = 2 if number == 1 else 0
createWorld(matrix)

matrix[1][1] = 3

lineBefore = 1
columnBefore = 1

for i in range(1, len(matrix) - 1): #linhas

  if (i != lineBefore):
    matrix[lineBefore][columnBefore] = 0

  if ((i % 2) == 0): # par
    # for de costas
    for j in range(len(matrix[i]) - 2, 0, -1):
      matrix[i][columnBefore] = 0
      matrix[i][j] = 3
      columnBefore = j
      exibir(matrix)
  else: # impar
    # for de frente
    for j in range(1, len(matrix[i]) - 1):
      if (i == 1 and j == 1):
        continue
      matrix[i][columnBefore] = 0
      matrix[i][j] = 3
      columnBefore = j
      exibir(matrix)
  
  lineBefore = i
