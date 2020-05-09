from tensorflow import keras

FASHION_MNIST = keras.datasets.fashion_mnist

(TRAIN_IMAGES, TRAIN_LABELS), (TEST_IMAGES, TEST_LABELS) = FASHION_MNIST.load_data()
TRAIN_IMAGES = TRAIN_IMAGES / 255.0
TEST_IMAGES = TEST_IMAGES / 255.0
CLASS_NAMES = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
