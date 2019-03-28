import matplotlib.pyplot as plt

def exibir(I):
    plt.imshow(I, 'gray')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 2, 0, 1],
    [1, 0, 2, 0, 0, 1], 
    [1, 0, 2, 0, 0, 1], 
    [1, 0, 2, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]]

while True:
  exibir(matrix)
