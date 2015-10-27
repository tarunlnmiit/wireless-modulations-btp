import numpy

def receiver(inp_X1, inp_X2, inpSize_X1, inpSize_X2, H):
    # Demodultaion of signal
    
    for i in range(inpSize_X1):
        for j in range(len(inp_X1[i])):
            inp_X1[i][j] /= (2**8)

    for i in range(inpSize_X2):
        for j in range(len(inp_X2[i])):
            inp_X2[i][j] /= (2**8)
    
    tempH = numpy.linalg.inv((numpy.matrix.transpose(H)*H)) * numpy.matrix.transpose(H)

    tempY1 = []
    tempY2 = []

    for i in xrange(len(inp_X1)):
        for j in xrange(len(inp_X1[i])):
            tempY1.append(inp_X1[i][j])

    for i in xrange(len(inp_X2)):
        for j in xrange(len(inp_X2[i])):
            tempY2.append(inp_X2[i][j])
    
    tempY = numpy.matrix([tempY1, tempY2])
    
    tempX = tempH * tempY
    tempX = tempX.tolist()
    
    for i in range(len(tempX)):
        for j in range(len(tempX[i])):
            if tempX[i][j] >= 0:
                tempX[i][j] = 1
            else:
                tempX[i][j] = -1
    
    for i in range(len(tempX)):
        for j in range(len(tempX[i])):
            if tempX[i][j] == -1:
                tempX[i][j] = 0
            else:
                tempX[i][j] = 1
    
    return tempX[0], tempX[1]