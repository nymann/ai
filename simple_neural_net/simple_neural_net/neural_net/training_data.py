from numpy import array

# The training set, with 4 examples consisting of 3
# input values and 1 output value
TRAINING_INPUTS = array([[0, 0, 1],
                         [1, 1, 1],
                         [1, 0, 1],
                         [0, 1, 1]])

TRAINING_OUTPUTS = array([[0, 1, 1, 0]]).T
