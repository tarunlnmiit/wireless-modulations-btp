def transmitter(inp, size):
	# Conversion to BPSK signal
	out = [0]*size
	for i in range(size):
		if inp[i] == 0:
			out[i] = -1
		else:
			out[i] = 1
	#Fixed Point
	for i in range(size):
		out[i] *= (2**8)
	return out