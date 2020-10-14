### Import necessary libraries
# import .........

def read_reg(register, ubit, mbit):
    result = '11' + str(ubit) + str(mbit) + '0000' + '{0:08b}'.format(register) + 16*'0'
    msb1 = int(result[:8],2)
    msb2 = int(result[8:16],2)
    lsb1 = int(result[16:24],2)
    lsb2 = int(result[24:],2)
    #print spi.xfer([msb1, msb2, lsb1, lsb2])
    return [msb1, msb2, lsb1, lsb2]
