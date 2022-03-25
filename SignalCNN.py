# from SignalGen import *
# from DatasetMaker import DatasetGen
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
epochs = 3
steps_per_epoch=10

def RunCNN():


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

  # # plot.figure(figsize=(10, 10))
# for images, labels in ds_train.take(1):
#   for i in range(9):
#     ax = plot.subplot(3, 3, i + 1)
#     plot.imshow(images[i].numpy().astype("uint8"))
#     plot.title(class_names[labels[i]])
#     plot.axis("off")
# plot.show()
  
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
      epochs=epochs, 
      steps_per_epoch=steps_per_epoch,
      validation_data= ds_validation.repeat(), 
      validation_steps=2
  )

  predictions = model.predict(val_dataset)
  print(predictions)
