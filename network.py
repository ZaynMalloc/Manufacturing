from matplotlib import pyplot as plt
import numpy as np

#Here is our original data. The format is: [bitcoin price, video games sales]
'''
data = [[415.16, 253, 2537.66], [672.48, 181.5,2705.605], 
[608.44, 234.3,2730],[968.23, 997,2764.293],
[1079.75, 485, 2858], [2504.28, 231, 2978],
[4764.87, 168, 2978],[4349.29, 316, 2997], 
[13860.14, 1270, 2977]]
'''

#Here is our data with a logarithm. The format is: [log(bitcoin price), log(video games sales)]

data = [[2.62, 2.40, 3.40], [2.83, 2.26, 3.43], 
[2.78, 2.37, 3.44],[2.99, 3.00, 3.44],
[3.03, 2.69, 3.46], [3.40, 2.36, 3.47],
[3.68, 2.23, 3.47],[3.63, 2.5, 3.47], 
[4.14, 3.1, 3.48]]


#We are going to make a prediction if bitcoin cost 8441.24 and there were 500 million video game sales
today = [3.93, 2.70]

#Activation function
def activation_function(data_point, w1, w2, b):
    return data_point[0] * w1 + data_point[1] * w2 + b

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivative_sigmoid(x):
    return x * (1 - x)

#Training 
def train(desired_prediction):
    #Get random weights
    w1 = np.random.randn()
    w2 = np.random.randn()
    b = np.random.randn()
    
    #Set parameters for the number of iterations and learning rate
    iterations = 250000
    learning_rate = 0.00005

    #Create an array to track costs
    costs = [] 
    
    for i in range(iterations):
        # Generate a random number and get a data point
        ri = np.random.randint(len(data))
        point = data[ri]

        #Once a random data point is choosen we calulate the activation function
        z = point[0] * w1 + point[1] * w2 + b

        #Set prediction by using the sigmoid function
        pred = sigmoid(z)
        
        #The target is the 2nd element (Shippments)
        target = point[2]
        
        #Calculate cost
        cost = np.square(pred - target)
        
        # print the cost over all data points every 1k iters
        if i % 100 == 0:
            c = 0
            for j in range(len(data)):
                p = data[j]
                p_pred = sigmoid(w1 * p[0] + w2 * p[1] + b)
                c += np.square(p_pred - p[2])
            costs.append(c)
        
        dcost_dpred = 2 * (pred - target)
        dpred_dz = derivative_sigmoid(z)
        

        dz_dw1 = point[0]
        dz_dw2 = point[1]
        dz_db = 1
        
        dcost_dz = dcost_dpred * dpred_dz
        
        dcost_dw1 = dcost_dz * dz_dw1
        dcost_dw2 = dcost_dz * dz_dw2
        dcost_db = dcost_dz * dz_db
        
        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        b = b - learning_rate * dcost_db
    
    print()
    print('Costs, weights, and bias')
    print(costs)
    print(w1)
    print(w2)
    print(b)
    print()
    print('Prediction')
    print(activation_function(desired_prediction, w1, w2, b))

#Train and plot
train(today)