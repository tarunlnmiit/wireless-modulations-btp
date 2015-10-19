def receiver(inp, inpSize, hval):
    # Demodultaion of signal
    
    for i in range(inpSize):
        for j in range(len(inp[i])):
            inp[i][j] /= (2**8)

    for i in range(inpSize):
        for j in range(len(inp[i])):
            inp[i][j] /= hval

    for i in range(inpSize):
        for j in range(len(inp[i])):
            if inp[i][j] >= 0:
                inp[i][j] = 1
            else:
                inp[i][j] = -1
    
    for i in range(inpSize):
        for j in range(len(inp[i])):
            if inp[i][j] == -1:
                inp[i][j] = 0
            else:
                inp[i][j] = 1

    return inp