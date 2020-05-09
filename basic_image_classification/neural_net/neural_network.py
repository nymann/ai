import numpy
import tensorflow as tf
from tensorflow import keras

from neural_net.training_data import TEST_IMAGES, TEST_LABELS, TRAIN_IMAGES, TRAIN_LABELS


class NeuralNetwork:
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10)
        ])

    def train(self, epochs=10):
        self.model.compile(optimizer='adam',
                           loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                           metrics=['accuracy'])
        # Feed the model
        self.model.fit(TRAIN_IMAGES, TRAIN_LABELS, epochs=epochs)
        test_loss, test_acc = self.model.evaluate(TEST_IMAGES, TEST_LABELS, verbose=2)

        print('\nTest accuracy:', test_acc)

    def solve(self):
        probability_model = tf.keras.Sequential([self.model,
                                                 tf.keras.layers.Softmax()])
        predictions = probability_model.predict(TEST_IMAGES)
        return numpy.argmax(predictions[0])
