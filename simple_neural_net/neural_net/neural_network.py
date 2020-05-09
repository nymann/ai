import pickle

from numpy import random, dot, exp


class NeuralNetwork:

    def __init__(self):
        # Set synaptic weights to a 3x1 matrix,
        # with values from -1 to 1 and mean 0
        try:
            with open("synaptic_weights.p", "rb") as file:
                self.synaptic_weights = pickle.load(file)
        except OSError:
            # Seed the random number generator
            random.seed(1)
            self.synaptic_weights = 2 * random.random((3, 1)) - 1

    @staticmethod
    def sigmoid_derivative(x):
        """
        The derivative of the sigmoid function used to
        calculate necessary weight adjustments
        """
        return x * (1 - x)

    @staticmethod
    def sigmoid(x):
        """
        Takes in weighted sum of the inputs and normalizes
        them through between 0 and 1 through a sigmoid function
        """
        return 1 / (1 + exp(-x))

    def train(self, training_inputs, training_outputs, training_iterations):
        """
        We train the model through trial and error, adjusting the
        synaptic weights each time to get a better result
        """
        for iteration in range(training_iterations):
            # Pass training set through the neural network
            output = self.solve(training_inputs)

            # Calculate the error rate
            error = training_outputs - output

            # Multiply error by input and gradient of the sigmoid function
            # Less confident weights are adjusted more through the nature of the function
            adjustments = dot(training_inputs.T, error * self.sigmoid_derivative(output))

            # Adjust synaptic weights
            self.synaptic_weights += adjustments
        with open("synaptic_weights.p", "wb") as file:
            pickle.dump(self.synaptic_weights, file)

    def solve(self, inputs):
        """
        Pass inputs through the neural network to get output
        """

        inputs = inputs.astype(float)
        output = self.sigmoid(dot(inputs, self.synaptic_weights))
        return output
