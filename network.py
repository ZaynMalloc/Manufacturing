from matplotlib import pyplot as plt
import numpy as np

bitcoin_price = [157, 292.2, 253, 142, 138, 181.5, 142, 179, 234.3, 216, 723.8, 997, 127, 204, 485, 195, 147, 231, 182, 168,
316, 238, 1147, 1270]

shippment = [2537.66, 2705.605, 2730, 2764.293, 2858, 2978, 2997, 2977]

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.rand()

T = np.linspace(-5,5,10)
Y1 = sigmoid(T)
Y2 = sigmoid(T)
plt.plot(T, Y1, c='r')
plt.plot(T, Y2, c='b')
plt.show()

#Training loop

for i in range(1,1000):
    ri = np.random.randint(len(bitcoin_price))
    point = bitcoin_price[ri]
    print(point)
