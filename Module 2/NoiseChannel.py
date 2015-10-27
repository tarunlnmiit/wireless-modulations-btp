from math import sqrt
from numpy import random

def NoiseChannel(inp_X1, inp_X2, inpSize, snrArray, snrSize):
	# Addition of noise to transmitted signal
	
	noisedSignal_X1 = []
	noisedSignal_X2 = []
	
	for i in range(snrSize):
		noise = [0]*inpSize
		l = []
		for k in range(inpSize):
			noise[k] = float(sqrt(10**((-snrArray[i])/10.0)) * random.randn(1,1))
			noise[k] *= (2**8)
			l.append(inp_X1[k]+noise[k])
		noisedSignal_X1.append(l)

	for i in range(snrSize):
		noise = [0]*inpSize
		l = []
		for k in range(inpSize):
			noise[k] = float(sqrt(10**((-snrArray[i])/10.0)) * random.randn(1,1))
			noise[k] *= (2**8)
			l.append(inp_X2[k]+noise[k])
		noisedSignal_X2.append(l)
	
	return noisedSignal_X1, noisedSignal_X2