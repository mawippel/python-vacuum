import matplotlib.pyplot as plt

def exibir(I):
    plt.imshow(I, 'gray')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

matrix = [[1,2,3], 
          [1,2,3], 
          [1,2,3]]

while True:
  exibir(matrix)
