from SignalGen import *


class AM:

    def __init__(self):
        self.signal = []

    def RanAMSignal(self):
        self.signal = RanAMSignal()

    def Plot(self):
        pl.plot(t, self.signal)
        pl.show()

    def Spectogram(self):
        pl.specgram(self.signal,SamplingFrequency)
        pl.show()

d = AM()

d.RanAMSignal()
d.Plot()
d.Spectogram()
