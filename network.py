from matplotlib import pyplot as plt
import numpy as np

#Here is our input data [bitcoin price, video games sales]
data = [[415.16, 253, 2537.66], [672.48, 181.5,2705.605], 
[608.44, 234.3,2730],[968.23, 997,2764.293],
[1,079.75, 485, 2858], [2,504.28, 231, 2978],
[4,764.87, 168, 2978],[4,349.29, 316, 2997], 
[13,860.14, 1270, 2977]]

#If we used our algorithim today
today = [8,441.24, 500]

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivative_sigmoid(x):
    return x * (1 - x)

for i in range(len(data)):
    point = data[i]

#Training parameters
iterations = 50000
learning_rate = 0.01
costs = []

#Training loop
for i in range(iterations):

    w1 = np.random.randn()
    w2 = np.random.randn()
    b = np.random.randn()

    ri = np.random.randint(len(data))
    point = data[ri]
  
    z = point[0] * w1 + point[1] * w2 + b
    pred = sigmoid(z)

    target = point[2]
    cost = np.square(pred - target)

   
    
    dcost_pred = 2 * (pred - target)
    dpred_dz = derivative_sigmoid(z)
    dz_dwl = point[0]
    dz_dw2 = point[1]
    dz_db = 1

    dcost_dwz = dcost_pred * dpred_dz 

    dcost_dw1 = dcost_pred * dz_dwl
    dcost_dw2 = dcost_pred * dz_dw2
    dcost_db = dcost_dwz * dz_db
 
    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db

    plt.plot(costs)

prediction = sigmoid(today)
print(today)
