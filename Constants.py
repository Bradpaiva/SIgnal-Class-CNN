#constants

class constant:
	def __init__(self):
		self.TotalTime = 2

		self.CarrierFreqMin = 500

		self.CarrierFreqMax = 1500

		self.SamplingFrequency = 3000

		self.BinaryFrequency = 100 #SamplingFrequency/BinaryFrequency must be int

		self.Fdev = 50   #frequency deviation, make higher than bitrate

		self.NoiseRatio = .1

		self.samples = 100