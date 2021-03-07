import numpy as np
import time

start = time.time()

def sigmoid(x):
    return 1 / (1 * np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


iterations = 1000

tr_inputs = np.array([[0,0,1],
                    [1,1,1],
                    [1,0,1],
                    [0,1,1]])

tr_outputs = np.array([[0,1,0,0]]).T

np.random.seed(1)

weights = 2 * np.random.random((3,1)) - 1

print("Random synaptic weights: ")
print(weights)

for iteration in range(iterations):

    input_layer = tr_inputs

    outputs = sigmoid(np.dot(input_layer, weights))

    error = tr_outputs - outputs

    adjustments = error * sigmoid_derivative(outputs)

    weights += np.dot(input_layer.T, adjustments)

print("Synaptic weights after training:")
print(weights)

print("Output after training")
print(outputs)

end = time.time()
print("Finished",iterations,"iterations after:",end - start,"seconds")
