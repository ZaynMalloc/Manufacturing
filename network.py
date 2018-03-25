from matplotlib import pyplot as plt
import numpy as np

#Here is our input data [bitcoin price, video games sales]
bitcoin_price_video_game_data = [[367.13,157], [436.61, 292.2], [415.16, 253], [449.33, 142], [531.8, 138],
[672.48, 181.5], [625.88, 142], [572.33, 179], [608.44, 234.3], [697.37, 216], [742.01, 723.8],
[968.23, 997], [967.67, 127], [1,190.89, 204], [1,079.75, 485], [1,349.19, 195],
[2,328.91, 147], [2,504.28, 231], [2,873.83, 182], [4,764.87, 168],
[4,349.29, 316], [4,353.05, 238], [9,916.54, 1147], [13,860.14, 1270]]

shippment = [2537.66, 2705.605, 2730, 2764.293, 2858, 2978, 2997, 2977]

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

#Scatter Data
'''
for i in range(len(bitcoin_price_video_game_data)):
    point = bitcoin_price_video_game_data[i]
    plt.scatter(point[0], point[1])
    plt.show()
'''
#Training loop
for i in range(1,1000):
    ri = np.random.randint(len(bitcoin_price_video_game_data))
    point = bitcoin_price_video_game_data[ri]

    z = bitcoin_price_video_game_data[0] * w1 + bitcoin_price_video_game_data[1] * w2 + b
    pred = sigmoid(z)

    target = point[2]
    cost = np.square(pred - target)


    print(point)
    print(cost)

