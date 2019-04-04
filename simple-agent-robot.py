import matplotlib.pyplot as plt
import random

def exibir(I):
    plt.imshow(I, 'gray')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

# 0 -> clean
# 1 -> wall
# 2 -> dirt
matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# Actions Matrix -> represents the action for each position
# Actions = up (0), down (1), left (2), right (3), clean(4), end (5)
actionsMatrix = [
    [9, 9, 9, 9, 9, 9],
    [9, 1, 3, 1, 5, 9],
    [9, 1, 0, 1, 0, 9], 
    [9, 1, 0, 1, 0, 9], 
    [9, 3, 0, 3, 0, 9],
    [9, 9, 9, 9, 9, 9]
]

# The robot always starts at matrix[1][1]
currLine = 1
currCol = 1

def createWorld(m):
    for mI in range(1, 5):
        for aI in range(1, 5):
            number = random.randint(0, 3)
            m[mI][aI] = 2 if number == 1 else 0

def findNextAction(x, y):
  return actionsMatrix[x][y]

# decides which action will be done
# Actions = up (0), down (1), left (2), right (3), clean(4)
def agenteReativoSimples(x, y):
  if (matrix[x][y] == 2): # if it's dirty, return the clean action
    return 4
  return findNextAction(x, y)


def main():
  createWorld(matrix)
  global currLine
  global currCol
  while True:
    action = agenteReativoSimples(currLine, currCol)
    if (action == 0): # go up
      print("up")
      currLine = currLine - 1 # remove 1 line
    elif (action == 1): # go down
      print("down")
      currLine = currLine + 1
    elif (action == 2): # go left
      print("left")
      currCol = currCol - 1
    elif (action == 3): # go right
      print("right")
      currCol = currCol + 1
    elif (action == 4): # clean
      print("clean")
      matrix[currLine][currCol] = 0
    else:
      print("end")
      break

  for i in range(1, len(matrix) - 1):
    for j in range(i, len(matrix[i]) - 1):
      print(matrix[i][j]) # verifies if the matrix is empty
  



if __name__ == "__main__":
  main()

'''
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
'''