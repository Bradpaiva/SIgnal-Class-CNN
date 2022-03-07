#region selection


from DatasetMaker import DatasetGen
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plot
from tensorflow import keras
from scipy import signal
from scipy.fft import fftshift
import cv2




img = cv2.imread("Samples/AM/training0.jpg") #Users/bradpaiva/Documents/Python/CNN/

x = 0
y = 0
w = 400
h = 400

crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
img_height = 640
img_width = 480


# FreqThreshold = 1000

# RegionFrequencies = []
# for y in img_height:
# 	FrequencyMag = 0
# 	for x in img_width:
# 		FrequencyMag = FrequencyMag + #some vecotr to determine stretght
# 	if FrequencyMag > FreqThreshold
# 	RegionFrequencies.append(y)


