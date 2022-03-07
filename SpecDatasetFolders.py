from SignalGen import *
from DatasetMaker import DatasetGen
import tensorflow as tf
import matplotlib.pyplot as plot
from tensorflow import keras
from scipy import signal
from scipy.fft import fftshift
from tqdm import tqdm
import numpy as np
import pylab as pl
import scipy.signal.signaltools as sigtool
import scipy.signal as signal
from numpy.random import sample
from tqdm import tqdm


samples = 1400
classes = 7


t = np.linspace(0,TotalTime, SamplingFrequency*TotalTime)

def DatasetGen(samples):
  Signals = []
  Classes = []
  for i in tqdm(range(int(samples/classes))):
    AM = RanAMSignal()
    plot.specgram(AM,SamplingFrequency)
    plot.savefig('Samples/AM/training'+str(i)+'.jpg')
    del(AM)
  for i in tqdm(range(int(samples/classes))):
    FM = RanFMSignal()
    plot.specgram(FM,SamplingFrequency)
    plot.savefig('Samples/FM/training'+str(i)+'.jpg')
    del(FM)
  for i in tqdm(range(int(samples/classes))):
    ASK = RanASKSignal()
    plot.specgram(ASK,SamplingFrequency)
    plot.savefig('Samples/ASK/training'+str(i)+'.jpg')
    del(ASK)
  for i in tqdm(range(int(samples/classes))):
    FSK = RanFSKSignal()
    plot.specgram(FSK,SamplingFrequency)
    plot.savefig('Samples/FSK/training'+str(i)+'.jpg')
    del(FSK)
  for i in tqdm(range(int(samples/classes))):
    PSK = RanPSKSignal()
    plot.specgram(PSK,SamplingFrequency)
    plot.savefig('Samples/PSK/training'+str(i)+'.jpg')
    del(PSK)
  for i in tqdm(range(int(samples/classes))):
    QPSK = RanQPSKSignal()
    plot.specgram(QPSK,SamplingFrequency)
    plot.savefig('Samples/QPSK/training'+str(i)+'.jpg')
    del(QPSK)
  for i in tqdm(range(int(samples/classes))):
    QAM16 = RanQAM16Signal()
    plot.specgram(QAM16,SamplingFrequency)      
    plot.savefig('Samples/QAM16/training'+str(i)+'.jpg')
    del(QAM16)
  return


DatasetGen(samples)
