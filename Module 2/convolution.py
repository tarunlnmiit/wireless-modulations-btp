import numpy

def multiplethreading(inp_X1, inp_X2, H):
	X = numpy.matrix([inp_X1, inp_X2])
	
	temp = H*X
	
	temp1 = temp[0].tolist()
	temp1 = temp1[0]
	temp2 = temp[1].tolist()
	temp2 = temp2[0]
	
	return temp1, temp2