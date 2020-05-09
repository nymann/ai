from tensorflow import keras

FASHION_MNIST = keras.datasets.fashion_mnist

(TRAIN_IMAGES, TRAIN_LABELS), (TEST_IMAGES, TEST_LABELS) = FASHION_MNIST.load_data()
