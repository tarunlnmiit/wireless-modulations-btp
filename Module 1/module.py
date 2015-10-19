import matplotlib.pyplot as plt
import math
from random import randint
from Transmitter import transmitter
from NoiseChannel import NoiseChannel
from Receiver import receiver
from convolution import h


inputSize = int(raw_input('Enter the size of the input: '))
hValue = float(raw_input('Enter value of convolution impulse: '))
snrSize = int(raw_input('Enter size of SNR array: '))
snrArray = raw_input('Enter SNR array: ').split()

for i in range(snrSize):
	snrArray[i] = int(snrArray[i])

digitalInput = []
for i in range(inputSize):
	digitalInput.append(randint(0,1))

# Output of Transmitter
transmitSignal = transmitter(digitalInput, inputSize)

#Output after impulse convolution
convolved = h(transmitSignal, hValue)

# Output after noise addition
noisedSignal = NoiseChannel(convolved, inputSize, 				snrArray, snrSize)
#print noisedSignal

# Signal received at receiver and demodulated
receivedSignal = receiver(noisedSignal, len(noisedSignal),hValue)
#print receivedSignal, len(receivedSignal)
#print digitalInput
# Error per SNR calculations
err = []
for i in range(len(noisedSignal)):
    l = [0]*inputSize
    for j in range(len(digitalInput)):
    	l[j] = abs(receivedSignal[i][j] - digitalInput[j])
    err.append(sum(l))

# Error per bit calculations
for i in range(len(err)):
	err[i] /= float(inputSize)
#print err
# Theoritical bit error rate calculation
ber = [0]*snrSize
#print snrArray
for i in range(snrSize):
	ber[i] = 0.5*math.erfc(math.sqrt(10**(snrArray[i]/10.0)))

# Practical Plot
#plt.figure(1)
plt.semilogy(snrArray, err, 'r')
#plt.show()

# Theoritical Plot
#plt.figure(2)
plt.semilogy(snrArray, ber, 'b')
plt.title('Theoritical/Practical BER Curve')
plt.xlabel('SNR per bit in dB')
plt.ylabel('Bit Error Rate in dB')
plt.legend(['Practical', 'Theoritical'],loc=3)
plt.axis([snrArray[0],snrArray[-1],10**-5,10**0])
plt.show()