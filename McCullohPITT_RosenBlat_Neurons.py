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
step_fuction = lambda x: 0 if x<1 else 1 # step function with threshold of 1 anythin b

for x, _ in training_data:
    result = dot(x, w)

    print("{}: {} -> {}".format(x[:2], result, step_fuction(result)))
