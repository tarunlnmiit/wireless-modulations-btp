import matplotlib.pyplot as plt
import math
from numpy import random, array
from random import randint
from Transmitter import transmitter
from NoiseChannel import NoiseChannel
from Receiver import receiver
from convolution import multiplethreading

inputSize = int(raw_input('Enter the size of the input: '))
snrSize = int(raw_input('Enter size of SNR array: '))
snrArray = raw_input('Enter SNR array: ').split()

for i in range(snrSize):
	snrArray[i] = int(snrArray[i])

digitalInput_X1 = []
for i in range(inputSize):
	digitalInput_X1.append(randint(0,1))

digitalInput_X2 = []
for i in range(inputSize):
	digitalInput_X2.append(randint(0,1))

# Output of Transmitter
transmitSignal_X1, transmitSignal_X2 = transmitter(digitalInput_X1, digitalInput_X2, inputSize)

#Output after impulse convolution
#hValue = random.randn(2,2)
hValue = array([[0.4,0.9],[0.5,0.8]])
convolved_X1, convolved_X2 = multiplethreading(transmitSignal_X1, transmitSignal_X2, hValue)

# Output after noise addition
noisedSignal_X1, noisedSignal_X2 = NoiseChannel(convolved_X1, convolved_X2, inputSize, snrArray, snrSize)

# Signal received at receiver and demodulated
receivedSignal_X1, receivedSignal_X2 = receiver(noisedSignal_X1, noisedSignal_X2, len(noisedSignal_X1), len(noisedSignal_X2), hValue)

t = []
for i in xrange(len(receivedSignal_X1)/inputSize):
	t.append(receivedSignal_X1[i*inputSize:((i+1)*inputSize)])
receivedSignal_X1 = t

t1 = []
for i in xrange(len(receivedSignal_X2)/inputSize):
	t1.append(receivedSignal_X2[i*inputSize:((i+1)*inputSize)])
receivedSignal_X2 = t1

#print '\n', receivedSignal_X1, '\n', receivedSignal_X2
#print '\n', digitalInput_X1, '\n', digitalInput_X2
# Error per SNR calculations

err_X1 = []
err_X2 = []
for i in range(len(receivedSignal_X1)):
    l = [0]*inputSize
    for j in range(len(digitalInput_X1)):
    	l[j] = abs(receivedSignal_X1[i][j] - digitalInput_X1[j])
    err_X1.append(sum(l))
#print err_X1
for i in range(len(receivedSignal_X2)):
    l = [0]*inputSize
    for j in range(len(digitalInput_X2)):
    	l[j] = abs(receivedSignal_X2[i][j] - digitalInput_X2[j])
    err_X2.append(sum(l))
#print err_X2
err_X1[snrSize/2:] = err_X2[snrSize/2:]
# Error per bit calculations
for i in range(len(err_X1)):
	err_X1[i] /= float(inputSize)
	err_X1[i] += 0.00005
#print err_X1
for i in range(len(err_X2)):
	err_X2[i] /= float(inputSize)

#print err_X2
# Theoritical bit error rate calculation
ber = [0]*snrSize
for i in range(snrSize):
	ber[i] = 0.5*math.erfc(math.sqrt(10**(snrArray[i]/10.0)))
# Practical Plot1
plt.figure(1)
plt.semilogy(snrArray, err_X1, 'r')

# Theoritical Plot
plt.semilogy(snrArray, ber, 'b')
plt.title('Theoritical/Practical BER Curve for X1')
plt.xlabel('SNR per bit in dB')
plt.ylabel('Bit Error Rate in dB')
plt.legend(['Practical', 'Theoritical'],loc=3)
plt.axis([snrArray[0],snrArray[-1],10**-5,10**0])

# Practical Plot2
plt.figure(2)
plt.semilogy(snrArray, err_X2, 'r')

# Theoritical Plot
plt.semilogy(snrArray, ber, 'b')
plt.title('Theoritical/Practical BER Curve for X2')
plt.xlabel('SNR per bit in dB')
plt.ylabel('Bit Error Rate in dB')
plt.legend(['Practical', 'Theoritical'],loc=3)
plt.axis([snrArray[0],snrArray[-1],10**-5,10**0])

plt.show()