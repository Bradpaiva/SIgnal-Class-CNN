from SignalGen import *
from DatasetMaker import DatasetGen
import tensorflow as tf
import matplotlib.pyplot as plot
from tensorflow import keras
from scipy import signal
from scipy.fft import fftshift
from tqdm import tqdm

TrainingSamples = 100
ValidatingSamples = 100
SamplingRate= 1000

(x_train_time, y_train) = DatasetGen(TrainingSamples)
(x_val_time, y_val) = DatasetGen(ValidatingSamples)

for i in tqdm(range(len(x_train_time))):
  plot.specgram(x_train_time[i],SamplingRate)
  plot.savefig('training'+str(i)+'.jpg')


for i in tqdm(range(len(x_val_time))):
  plot.specgram(x_val_time[i],SamplingRate)
  plot.savefig('validating'+str(i)+'.jpg')