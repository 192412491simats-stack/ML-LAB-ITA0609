from math import exp

# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + exp(-x))

# Derivative of Sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Input Data (XOR)
X = [[0,0],[0,1],[1,0],[1,1]]
Y = [0,1,1,0]

# Initialize Weights
w1 = 0.5
w2 = -0.5
w3 = 0.3
w4 = 0.8
w5 = -0.7
w6 = 0.2

learning_rate = 0.5

# Training
for epoch in range(5000):

    for i in range(len(X)):

        x1 = X[i][0]
        x2 = X[i][1]
        target = Y[i]

        # Forward Pass
        h1 = sigmoid(x1*w1 + x2*w2)
        h2 = sigmoid(x1*w3 + x2*w4)

        output = sigmoid(h1*w5 + h2*w6)

        # Error
        error = target - output

        # Backpropagation
        d_output = error * sigmoid_derivative(output)

        d_h1 = d_output * w5 * sigmoid_derivative(h1)
        d_h2 = d_output * w6 * sigmoid_derivative(h2)

        # Update Output Weights
        w5 += learning_rate * d_output * h1
        w6 += learning_rate * d_output * h2

        # Update Hidden Weights
        w1 += learning_rate * d_h1 * x1
        w2 += learning_rate * d_h1 * x2
        w3 += learning_rate * d_h2 * x1
        w4 += learning_rate * d_h2 * x2

# Testing
print("Testing Neural Network")

for i in range(len(X)):
    x1 = X[i][0]
    x2 = X[i][1]

    h1 = sigmoid(x1*w1 + x2*w2)
    h2 = sigmoid(x1*w3 + x2*w4)

    output = sigmoid(h1*w5 + h2*w6)

    print(X[i], "Output =", round(output,3))
