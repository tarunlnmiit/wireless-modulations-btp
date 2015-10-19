def transmitter(inp_X1, inp_X2, size):
	# Conversion to BPSK signal

	out_X1 = [0]*size
	out_X2 = [0]*size
	for i in range(size):
		if inp_X1[i] == 0:
			out_X1[i] = -1
		else:
			out_X1[i] = 1
		if inp_X2[i] == 0:
			out_X2[i] = -1
		else:
			out_X2[i] = 1
	
	#Fixed Point
	for i in range(size):
		out_X1[i] *= (2**8)
		out_X2[i] *= (2**8)
	
	return out_X1, out_X2