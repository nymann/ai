import logging

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
    pass


if __name__ == '__main__':
    main()
