from math import sqrt
from numpy import random

def NoiseChannel(inp, inpSize, snrArray, snrSize):
	# Addition of noise to transmitted signal
	noisedSignal = []

	for i in range(snrSize):
		noise = [0]*inpSize
		l = []
		for k in range(inpSize):
			noise[k] = sqrt(10**((-snrArray[i])/10.0)) * random.randn(1,1)
			noise[k] *= (2**8)
			l.append(inp[k]+noise[k])
		noisedSignal.append(l)

	return noisedSignal