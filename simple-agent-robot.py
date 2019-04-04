import matplotlib.pyplot as plt
import random


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

def renderMatrix(matrix):
    plt.imshow(matrix, 'pink')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(0.5)
    plt.clf()

def createWorld(m):
    for mI in range(1, 5):
        for aI in range(1, 5):
            number = random.randint(0, 3)
            m[mI][aI] = 2 if number == 1 else 0
    renderMatrix(matrix)

def findNextAction(x, y):
  return actionsMatrix[x][y]

# decides which action will be done
# Actions = up (0), down (1), left (2), right (3), clean(4)
def simpleAgentRobot(x, y):
  if (matrix[x][y] == 2): # if it's dirty, return the clean action
    return 4
  return findNextAction(x, y)


def main():
  createWorld(matrix)
  global currLine
  global currCol
  while True:
    action = simpleAgentRobot(currLine, currCol)
    if (action == 0): # go up
      print("up")
      currLine = currLine - 1 # remove 1 line
      renderMatrix(matrix)
    elif (action == 1): # go down
      print("down")
      currLine = currLine + 1
      renderMatrix(matrix)
    elif (action == 2): # go left
      print("left")
      currCol = currCol - 1
      renderMatrix(matrix)
    elif (action == 3): # go right
      print("right")
      currCol = currCol + 1
      renderMatrix(matrix)
    elif (action == 4): # clean
      print("clean")
      matrix[currLine][currCol] = 0
      renderMatrix(matrix)
    else:
      print("end")
      break

  for i in range(1, len(matrix) - 1):
    for j in range(i, len(matrix[i]) - 1):
      print(matrix[i][j]) # verifies if the matrix is empty
  



if __name__ == "__main__":
  main()
