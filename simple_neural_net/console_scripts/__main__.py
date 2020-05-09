import logging

from numpy import array

from neural_net.neural_network import NeuralNetwork
from neural_net.training_data import TRAINING_INPUTS, TRAINING_OUTPUTS

NEURAL_NETWORK = NeuralNetwork()
LOGGER = logging.getLogger(__name__)


def main():
    train()
    solve()


def train():
    NEURAL_NETWORK.train(TRAINING_INPUTS, TRAINING_OUTPUTS, 10000)


def solve():
    a = int(input("Input 1: "))
    b = int(input("Input 2: "))
    c = int(input("Input 3: "))
    LOGGER.debug("Solving with input: {a=%d, b=%d, c=%d}" % (a, b, c))
    result = NEURAL_NETWORK.solve(array([a, b, c]))
    print(int(round(result[0])))


if __name__ == '__main__':
    main()
