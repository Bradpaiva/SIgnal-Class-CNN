import numpy as np
from ssqueezepy import cwt
from ssqueezepy.visuals import plot, imshow
from SignalGen import *



x,t,sf = RanQAM16Signal()

pi = np.pi
# v1, v2, v3 = 64, 128, 32

# plot(x, title="Original Signal" , show=1)

def Scalogram(x,t):
	# plot(x, title="Original Signal" , show=1)
	Wx, scales = cwt(x, 'morlet')
	imshow(Wx, yticks=scales, abs=1,
	title="abs(CWT) | Morlet wavelet",
	ylabel="scales", xlabel="samples")

Scalogram(x,t)
