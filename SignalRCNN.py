from SignalGen import *
from DatasetMaker import DatasetGen
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plot
from tensorflow import keras
from scipy import signal
from scipy.fft import fftshift


img_height = 640
img_width = 480
batchsize = 100


ds_train = keras.preprocessing.image_dataset_from_directory(
  '/Users/bradpaiva/Documents/Python/CNN/Samples',
  labels = 'inferred',
  label_mode = "int",
  color_mode = 'rgb',
  batch_size = batchsize,
  image_size = (img_height,img_width),
  shuffle = True,
  seed = 123,
  validation_split = 0.1,
  subset = "training",
  )

ds_validation = keras.preprocessing.image_dataset_from_directory(
  '/Users/bradpaiva/Documents/Python/CNN/Samples',
  labels = 'inferred',
  label_mode = "int",
  color_mode = 'rgb',
  batch_size = batchsize,
  image_size = (img_height,img_width),
  shuffle = True,
  seed = 123,
  validation_split = 0.1,
  subset = "validation",
  )



model = keras.Sequential([
  layers.Input((640,480,3)),
	layers.Conv2D(16, 3, padding = 'same'),
	layers.Conv2D(32, 3, padding = 'same'),
	layers.MaxPooling2D(),
	layers.Flatten(),
	layers.Dense(10),
])

model.compile(optimizer='adam', 
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
 
history = model.fit(
    ds_train.repeat(), 
    epochs=10, 
    steps_per_epoch=500,
    validation_data= ds_validation.repeat(), 
    validation_steps=2
)

predictions = model.predict(val_dataset)
print(predictions)