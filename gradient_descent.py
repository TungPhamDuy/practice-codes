import numpy as np
import math

def sigmoid(x):
    return 1/(1+math.e**(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

# Input data
x = np.array([0.1, 0.3])
# Target
y = 0.2
# Input to output weights
weights = np.array([-0.8, 0.5])
# The learning rate, eta in the weight step equation
learnrate = 0.5

# linear combination calculate in node:
h = x[0]*weights[0] + x[1]*weights[1]
# or h = np.dot(x,weights)

nn_output = sigmoid(h)
print("Neuron network output: ", nn_output)

# output error (y - y-hat)
y_hat = nn_output
error_output = y - y_hat
print("Error function output: ", error_output)

# output gradient descent
output_grad = sigmoid_prime(h)
print("Output gradient descent: ", output_grad)

# error term (lowercase delta)
error_term = error_output * output_grad
print("Error term: ",error_term)

# gradient descent step:
grad_step = [learnrate * error_term * x[0],
             learnrate * error_term * x[1]]
print("Gradient descent step: ", grad_step)



