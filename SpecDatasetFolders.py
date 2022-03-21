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


samples = 7000
classes = 7


# t = np.linspace(0,TotalTime, SamplingFrequency*TotalTime)

def SpecDatasetGen():
  Signals = []
  Classes = []
  samples = 7000
  classes = 7
  for i in tqdm(range(int(samples/classes))):
    AM,t, SamplingFrequency= RanAMSignal()
    fig = plot.figure(frameon = False)
    ax = plot.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(AM,SamplingFrequency)
    fig.savefig('Samples/AM/training'+str(i)+'.jpg')
    plot.close(fig)
    del(AM)
  for i in tqdm(range(int(samples/classes))):
    FM,t, SamplingFrequency = RanFMSignal()
    fig = plot.figure(frameon = False)
    ax = plot.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(FM,SamplingFrequency)
    fig.savefig('Samples/FM/training'+str(i)+'.jpg')
    plot.close(fig)
    del(FM)
  for i in tqdm(range(int(samples/classes))):
    ASK,t, SamplingFrequency = RanASKSignal()
    fig = plot.figure(frameon = False)
    ax = plot.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(ASK,SamplingFrequency)
    fig.savefig('Samples/ASK/training'+str(i)+'.jpg')
    plot.close(fig)
    del(ASK)
  for i in tqdm(range(int(samples/classes))):
    FSK,t, SamplingFrequency = RanFSKSignal()
    fig = plot.figure(frameon = False)
    ax = plot.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(FSK,SamplingFrequency)
    fig.savefig('Samples/FSK/training'+str(i)+'.jpg')
    plot.close(fig)
    del(FSK)
  for i in tqdm(range(int(samples/classes))):
    PSK,t, SamplingFrequency = RanPSKSignal()
    fig = plot.figure(frameon = False)
    ax = plot.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(PSK,SamplingFrequency)
    fig.savefig('Samples/PSK/training'+str(i)+'.jpg')
    plot.close(fig)
    del(PSK)
  for i in tqdm(range(int(samples/classes))):
    QPSK,t, SamplingFrequency = RanQPSKSignal()
    fig = plot.figure(frameon = False)
    ax = plot.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(QPSK,SamplingFrequency)
    fig.savefig('Samples/QPSK/training'+str(i)+'.jpg')
    plot.close(fig)
    del(QPSK)
  for i in tqdm(range(int(samples/classes))):
    QAM16,t, SamplingFrequency = RanQAM16Signal()
    fig = plot.figure(frameon = False)
    ax = plot.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(QAM16,SamplingFrequency)
    fig.savefig('Samples/QAM16/training'+str(i)+'.jpg')
    plot.close(fig)
    del(QAM16)
  return

