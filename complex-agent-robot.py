import matplotlib.pyplot as plt
import random
from tkinter import messagebox
from copy import copy, deepcopy


class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent


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

presentationMatrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# The robot always starts at matrix[1][1]
currLine = 1
currCol = 1
stack = [Node(1, 1)]
solution = [Node(1, 1)]
process_map = []


def isMapClean():
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if (matrix[i][j] == 2):
                return False
    return True


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
    global process_map
    global presentationMatrix
    process_map = deepcopy(matrix)
    presentationMatrix = deepcopy(matrix)


def has_position(x, y):
    if (matrix[x][y] == 1):
        return False
    return True


def floodfill():
    while (len(stack) != 0):
        node = stack.pop(0)
        x = node.get_x()
        y = node.get_y()

        if (has_position(x - 1, y)):
            new_node = Node(x - 1, y, node)
            if (process_map[x - 1][y] == 2):
                return new_node
            if (process_map[x - 1][y] != 4):
                stack.append(new_node)
                process_map[x - 1][y] = 4

        if (has_position(x, y - 1)):
            new_node = Node(x, y - 1, node)
            if (process_map[x][y - 1] == 2):
                return new_node
            if (process_map[x][y - 1] != 4):
                stack.append(new_node)
                process_map[x][y - 1] = 4

        if (has_position(x + 1, y)):
            new_node = Node(x + 1, y, node)
            if (process_map[x + 1][y] == 2):
                return new_node
            if (process_map[x + 1][y] != 4):
                stack.append(new_node)
                process_map[x + 1][y] = 4

        if (has_position(x, y + 1)):
            new_node = Node(x, y + 1, node)
            if (process_map[x][y + 1] == 2):
                return new_node
            if (process_map[x][y + 1] != 4):
                stack.append(new_node)
                process_map[x][y + 1] = 4


def main():
    global matrix
    createWorld(matrix)
    global process_map
    global stack
    global currCol
    global currLine

    while (not isMapClean()):
        path = floodfill()
        x = path.get_x()
        y = path.get_y()

        aux_list = []
        while (path.get_parent() is not None):
            process_map[path.get_x()][path.get_y()] = 3
            aux_list.append(path)
            path = path.get_parent()
        aux_list.reverse()
        solution.extend(aux_list)

        matrix[x][y] = 0
        stack = [Node(x, y)]
        process_map = deepcopy(matrix)

    for path in solution:
        currCol = path.get_y()
        currLine = path.get_x()
        renderMatrix(presentationMatrix)
        if (presentationMatrix[currLine][currCol] == 2):
          presentationMatrix[currLine][currCol] = 0
    print("Aecio Neves limpou tudo com %s pontos" % len(solution))
    messagebox.showinfo("Aecio NEVE", "Aecio Neves aspirou tudo com %s pontos" % len(solution))


if __name__ == "__main__":
    main()
