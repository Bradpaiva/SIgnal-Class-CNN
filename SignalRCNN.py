# from SignalGen import *
# from DatasetMaker import DatasetGen
import glob
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plot
from tensorflow import keras
from scipy import signal
from scipy.fft import fftshift
from PIL import Image
import numpy as np
from matplotlib import cm
from tqdm import tqdm
import os as os

img_height = 480
img_width = 640
batchsize = 100
epochs = 3
steps_per_epoch= 500
samples= 7000

left = 0
width = 40
right = left+ 40

images = []
for f in tqdm(glob.iglob("./Samples/*/*")):
    images.append(np.asarray(Image.open(f)))
images = np.array(images)

classes=glob.glob("./Samples/*", recursive = True)
print(classes)

labels =[]
for i in range(len(classes)):
  labels = labels+[i]*int(samples/len(classes))
labels=np.array(labels)
print(labels)

region_data = []
for i in tqdm(range(samples)):
    pic = images[i].astype("uint8")
    im=Image.fromarray(pic)
    im1 = im.crop((left, 0, right, img_height))
    region_data.append(np.asarray(im1))
region_data=np.array(region_data)

ds_Region = tf.data.Dataset.from_tensor_slices((region_data, labels))
SHUFFLE_BUFFER_SIZE = 100

ds_Region = ds_Region.shuffle(SHUFFLE_BUFFER_SIZE).batch(batchsize)


model = keras.Sequential([
  layers.Input((img_height,width,3)),
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
    ds_Region.repeat(), 
    epochs=epochs, 
    steps_per_epoch=steps_per_epoch,
    validation_data= ds_Region.repeat(), 
    validation_steps=2
)

predictions = model.predict(val_dataset)
print(predictions)

