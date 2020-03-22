from random import choice
from numpy import array, dot, random

import numpy as np 

# MCNeurons for And gate
w = random.rand(2)
w[1] =1
w[0] =1

training_data = [
    (array([0, 0]), 0),
    (array([0, 1]), 0),
    (array([1, 0]), 0),
    (array([1, 1]), 1)
]
step_fuction = lambda x: 0 if x<2 else 1 # step function with threshold of 2 anythin b

for x, _ in training_data:
    result = dot(x, w)

    print("{}: {} -> {}".format(x[:2], result, step_fuction(result)))

# MCNeurons for OR gate
print("\r")
training_data = [
    (array([0, 0]), 0),
    (array([0, 1]), 1),
    (array([1, 0]), 1),
    (array([1, 1]), 1)
]
step_fuction = lambda x: 0 if x<1 else 1 # step function with threshold of 1 anythin be

for x, _ in training_data:
    result = dot(x, w)

    print("{}: {} -> {}".format(x[:2], result, step_fuction(result)))

print("\r")
# neuron can be modified to implement multiple boolean function in one code

step_fuction = lambda x: 0 if x < 50 else 1 # step fuction with threshold of 0.5 anything be

training_data = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 0),
    (array([1, 0, 1]), 0),
    (array([1, 1, 1]), 1)
]
w = random.rand(3)

b = 1 # initializing bias term
errors = []
eta = 0.1 # learning rate griding linear expression 
n = 10000 # nitration 

for i in range(n):
    x, expected = choice(training_data)
    # w = np.append(w, b)
    result = dot(w, x)
    error = expected - step_fuction(result) # irrspective of what threshold we set the all
    errors.append(error) # that is the beauty of bias , The "AND pattern "
    w += eta * error * x

for x, _ in training_data:
    result = dot(x, w)

    print("{}: {} -> {}".format(x[:3], result, step_fuction(result)))
  
    print(w)
# All those neurons are not work with XOR gate and not find expected output its give us diff answer

