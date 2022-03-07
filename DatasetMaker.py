import numpy as np
import pylab as pl
import scipy.signal.signaltools as sigtool
import scipy.signal as signal
from numpy.random import sample
import matplotlib.pyplot as plot
from SignalGen import *

samples = 100
classes = 7
TotalTime = 2
CarrierFreqMin = 500
CarrierFreqMax = 500
SamplingFrequency = 1000
BinaryFrequency = 4 #SamplingFrequency/BinaryFrequency must be int
Fdev = 50     #frequency deviation, make higher than bitrate


t = np.linspace(0,TotalTime, SamplingFrequency*TotalTime)

def DatasetGen(samples):
	Signals = []
	Classes = []
	for i in range(int(samples/classes)):
		AM = RanAMSignal()
		Signals.append(AM)
		Classes.append(0)
	for i in range(int(samples/classes)):
		FM = RanFMSignal()
		Signals.append(FM)
		Classes.append(1)
	for i in range(int(samples/classes)):
		ASK = RanASKSignal()
		Signals.append(ASK)
		Classes.append(2)
	for i in range(int(samples/classes)):
		FSK = RanFSKSignal()
		Signals.append(FSK)
		Classes.append(3)
	for i in range(int(samples/classes)):
		PSK = RanPSKSignal()
		Signals.append(PSK)
		Classes.append(4)
	for i in range(int(samples/classes)):
		QPSK = RanQPSKSignal()
		Signals.append(QPSK)
		Classes.append(5)
	for i in range(int(samples/classes)):
		QAM16 = RanQAM16Signal()
		Signals.append(QAM16)
		Classes.append(6)
	return Signals,Classes


# (Signals,Classess) = DatasetGen(samples)
# plot.plot(t,Signals[1]) #am
# plot.show()
#plot.plot(t,Signals[27]) #fm
#plot.show()
# plot.plot(t,Signals[51]) #ASK
# plot.show()
# plot.plot(t,Signals[76]) #FSK
# plot.show()
