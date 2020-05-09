import logging

import numpy

from basic_image_classification.neural_net.neural_network import NeuralNetwork
from basic_image_classification.neural_net.training_data import TEST_IMAGES, TEST_LABELS, CLASS_NAMES

NEURAL_NETWORK = NeuralNetwork()
LOGGER = logging.getLogger(__name__)


def main():
    train()
    solve()


def train():
    NEURAL_NETWORK.train(epochs=10)


def solve():
    img = (numpy.expand_dims(TEST_IMAGES[10], 0))
    print(f"Testing image ({img.shape}).")
    result = NEURAL_NETWORK.solve(img)
    print(f"Prediction: {result}, actual: {CLASS_NAMES[TEST_LABELS[10]]}")


if __name__ == '__main__':
    main()
