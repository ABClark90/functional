import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
import pandas as pd

(x_train, y_train), (x_test, y_test) = mnist.load_data()

