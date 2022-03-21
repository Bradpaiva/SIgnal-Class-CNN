import numpy as np
import pylab as pl
import scipy.signal.signaltools as sigtool
import scipy.signal as signal
from numpy.random import sample
import random
from Constants import constant
# from Constants import *

# c.TotalTime = 2
# c.CarrierFreqMin = 500
# c.CarrierFreqMax = 1500
# c.SamplingFrequency = 1000
# c.BinaryFrequency = 100 #SamplingFrequency/c.BinaryFrequency must be int
# c.Fdev = 50   #frequency deviation, make higher than bitrate
# c.NoiseRatio = .1
# samples = 100

c = constant()

# t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)

def RanSignalGen(): #Generates random analog signal
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    y = 0
    result = []
    for _ in t:
        result.append(y)
        y += np.random.normal(scale=1) 
    result = HighPass(np.array(result))
    return NormalizeSignal(result)

def HighPass(Ransig): #highpass filter with a cutoff of 50hz to normalize signals/reduce dc offset
    a = signal.butter(3, 50, btype='high', fs = c.SamplingFrequency ,output = 'sos')
    y = signal.sosfilt(a, Ransig)
    return y

def NormalizeSignal(signal): #sets the maximum value in the signal to 1 and scales
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))

def RanBinaryGen(): #generates random binary array (length matches time dimensions)
    result = []
    for x in range(int(c.BinaryFrequency*c.TotalTime)):
        temp= random.randint(0, 1)
        for m in range(int(c.SamplingFrequency/c.BinaryFrequency)):
            result.append(temp)
    return np.array(result)

def RanBinaryGen2(): #generates random binary array (length = bits)
    m=[]
    for i in range(c.BinaryFrequency*c.TotalTime):
        m.append(random.randint(0, 1))   # message signal (binary)
    return m

def RanAMSignal(): #Amplitude Modulation (OOK) with random carrier frequency and random analog signal
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    CarrierFreq = random.randint(c.CarrierFreqMin,c.CarrierFreqMax)
    RandomSignal = RanSignalGen()
    carrier = np.sin(CarrierFreq * t)
    y = carrier * RandomSignal
    y = y+np.random.normal(0, c.NoiseRatio, size=c.SamplingFrequency*c.TotalTime) #Add WGN
    return y,t, c.SamplingFrequency

def RanFMSignal():
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    CarrierFreq = random.randint(c.CarrierFreqMin,c.CarrierFreqMax)
    b = 15
    data = RanSignalGen()
    phi = CarrierFreq*t + b * data
    fm = np.sin(2*np.pi * phi)
    fm = fm + np.random.normal(0, c.NoiseRatio, size=c.SamplingFrequency*c.TotalTime) #Add WGN
    return fm,t, c.SamplingFrequency

def RanASKSignal(): #Amplitude shift keying with random carrier frequency and binary signal
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    CarrierFreq = random.randint(c.CarrierFreqMin,c.CarrierFreqMax)
    RandomSignal = RanBinaryGen()
    carrier = np.sin(CarrierFreq * t)
    y = carrier * RandomSignal
    y = y+np.random.normal(0, c.NoiseRatio, size=c.SamplingFrequency*c.TotalTime) #Add WGN
    return y,t, c.SamplingFrequency

def RanFSKSignal(): #Frequency shift keying with random carrier frequency and binary signal
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    CarrierFreq = random.randint(c.CarrierFreqMin,c.CarrierFreqMax)
    data_in_temp = []
    for x in range(int(c.BinaryFrequency*c.TotalTime)):
        data_in_temp.append(random.randint(0, 1))
    data_in = np.array(data_in_temp)
    m = np.zeros(0).astype(float)
    for bit in data_in:
        if bit == 0:
            m=np.hstack((m,np.multiply(np.ones(int(c.SamplingFrequency/c.BinaryFrequency)),CarrierFreq+c.Fdev)))
        else:
            m=np.hstack((m,np.multiply(np.ones(int(c.SamplingFrequency/c.BinaryFrequency)),CarrierFreq-c.Fdev)))
    y=np.zeros(0)
    y=np.cos(np.multiply(m,t))
    y = y+np.random.normal(0, c.NoiseRatio, size=c.SamplingFrequency*c.TotalTime) #Add WGN
    return y,t, c.SamplingFrequency

def RanPSKSignal():
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    Xpsk=np.zeros(c.TotalTime*c.SamplingFrequency)
    I = RanBinaryGen2()
    fc = random.randint(c.CarrierFreqMin,c.CarrierFreqMax)
    x1 = np.sin(2 * np.pi * fc * t)
    x2 = -1*np.sin(2 * np.pi * fc * t)
    tb = c.SamplingFrequency/c.BinaryFrequency
    t1=0
    t2=tb
    for n in range(c.BinaryFrequency*c.TotalTime):
        if (I[n] == 1):
            Xpsk[int(t1):int(t2)]=x1[int(t1):int(t2)]
        elif(I[n] != 1):
            Xpsk[int(t1):int(t2)]=x2[int(t1):int(t2)]
        t1=t1+tb
        t2=t2+tb
    Xpsk = Xpsk+np.random.normal(0, c.NoiseRatio, size=c.SamplingFrequency*c.TotalTime) #Add WGN
    return Xpsk,t, c.SamplingFrequency

def RanQPSKSignal():
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    Xpsk=np.zeros(c.TotalTime*c.SamplingFrequency)
    I = RanBinaryGen2()
    fc = random.randint(c.CarrierFreqMin,c.CarrierFreqMax)
    x1 = np.sin(2 * np.pi * fc * t + (2 * np.pi *45/360))
    x2 = np.sin(2 * np.pi * fc * t + (2 * np.pi *135/360))
    x3 = np.sin(2 * np.pi * fc * t + (2 * np.pi *225/360))
    x4 = np.sin(2 * np.pi * fc * t + (2 * np.pi *315/360))
    tb = 2*c.SamplingFrequency/c.BinaryFrequency
    t1=0
    t2=tb
    for n in range(c.BinaryFrequency*c.TotalTime-1):
        if ((I[n] == 0) and (I[n+1] == 0)):
            Xpsk[int(t1):int(t2)]=x1[int(t1):int(t2)]
        elif((I[n] == 0) and (I[n+1] == 1)):
            Xpsk[int(t1):int(t2)]=x2[int(t1):int(t2)]
        elif((I[n] == 1) and (I[n+1] == 0)):
            Xpsk[int(t1):int(t2)]=x3[int(t1):int(t2)]
        elif((I[n] == 1) and (I[n+1] == 1)):
            Xpsk[int(t1):int(t2)]=x4[int(t1):int(t2)]   
        t1=t1+tb
        t2=t2+tb
        n+=1
    Xpsk = Xpsk+np.random.normal(0, c.NoiseRatio, size=c.SamplingFrequency*c.TotalTime) #Add WGN
    return Xpsk,t, c.SamplingFrequency

def RanQAM16Signal():
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    QAM=np.zeros(c.TotalTime*c.SamplingFrequency)
    I = RanBinaryGen2()
    fc = random.randint(c.CarrierFreqMin,c.CarrierFreqMax)

    tb = 2*c.SamplingFrequency/c.BinaryFrequency
    t1=0
    t2=tb

    for n in range(c.BinaryFrequency*c.TotalTime-3):
        Value = I[n:n+4]
        if Value ==[0,0,0,0]:
            Am = 1.4142
            phase = 135
        elif Value ==[0,0,0,1]:
            Am = 1.1180
            phase = 116.565
        elif Value ==[0,0,1,0]:
            Am = 1.4142
            phase = 45
        elif Value ==[0,0,1,1]:
            Am = 1.1180
            phase = 63.435
        elif Value ==[0,1,0,0]:
            Am = 1.4142
            phase = 225
        elif Value ==[0,1,0,1]:
            Am = 1.1180
            phase = 243.435
        elif Value ==[0,1,1,0]:
            Am = 1.4142
            phase = 315
        elif Value ==[0,1,1,1]:
            Am = 1.1180
            phase = 296.565
        elif Value ==[1,0,0,0]:
            Am = 1.1180
            phase = 153.435
        elif Value ==[1,0,0,1]:
            Am = .7071
            phase = 135
        elif Value ==[1,0,1,0]:
            Am = 1.1180
            phase = 26.565
        elif Value ==[1,0,1,1]:
            Am = .7071
            phase = 45
        elif Value ==[1,1,0,0]:
            Am = 1.1180
            phase = 206.565
        elif Value ==[1,1,0,1]:
            Am = .7071
            phase = 225
        elif Value ==[1,1,1,0]:
            Am = 1.1180
            phase = 333.435
        elif Value ==[1,1,1,1]:
            Am = .7071
            phase = 315

        tx=t[int(t1):int(t2)]
        Carrier = Am*np.sin(2 * np.pi * fc * tx + (2 * np.pi *phase/360))

        QAM[int(t1):int(t2)]=Carrier

        t1=t1+tb
        t2=t2+tb
        n+=3

    QAM = QAM+np.random.normal(0, c.NoiseRatio, size=c.SamplingFrequency*c.TotalTime) #Add WGN
    return QAM,t,c.SamplingFrequency

