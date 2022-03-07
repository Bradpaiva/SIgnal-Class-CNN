

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

Samples=100

def MergeSignals(Signal1,Signal2,offset):
	Signal1=Signal1.tolist()
	Offset = [0] * (offset)
	Merge1=np.append(Signal1,Offset)
	Signal2=Signal2.tolist()
	Merge2=np.append(Offset,Signal2)
	Merge = Merge1+Merge2
	t = np.linspace(0,
			TotalTime+offset/SamplingFrequency, 
			int(SamplingFrequency*(TotalTime+ offset/SamplingFrequency)))
	if (len(Merge)>len(t)):
		Merge=Merge[:-1]
	return Merge, t


def MergeTwo(Class1,Class2):
	Signal1=[]
	Signal2=[]
	Merge=[]

	del(Signal1)
	del(Signal2)
	del(Merge)

	options = {0 : RanAMSignal,
	           1 : RanFMSignal,
	           2 : RanASKSignal,
	           3 : RanFSKSignal,
	           4 : RanPSKSignal,
	           5 : RanQPSKSignal,
	           6 : RanQAM16Signal,
	}

	offset = random.randrange(0, 2000)
	Signal1 = options[Class1]()
	Signal2 = options[Class2]()
	Merge, t2 = MergeSignals(Signal1,Signal2,offset)
	return Merge

def MergeTwoFolders():
	classes = {0 : 'AM',
	           1 : 'FM',
	           2 : 'ASK',
	           3 : 'FSK',
	           4 : 'PSK',
	           5 : 'QPSK',
	           6 : 'QAM16',
		}

	for i in range(6):
		for j in range (6):			
			for k in tqdm(range(Samples)):
				Merge = MergeTwo(i,j)
				plot.specgram(Merge,SamplingFrequency)
				if i<j :
					name1 = i
					name2 = j
				else :
					name1 = j
					name2 = i
				plot.savefig('Concurrent/'+str(classes[name1])+
					str(classes[name2])+'/training'+str(k)+'.jpg')
	return

MergeTwoFolders()
