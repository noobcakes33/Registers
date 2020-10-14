### Import necessary libraries
# import ............
from single_reg import read_reg


def write_multi_regs(from_reg, to_reg, data, ubit, mbit):
    for reg in range(from_reg, to_reg+1):
        result = '10' + str(ubit) + str(mbit) +'0000' + '{0:08b}'.format(reg) + str(bin(data))[2:18].zfill(16)
        print "[result] ",result
        
        msb1 = int(result[0:8],2)
        msb2 = int(result[8:16],2)
        lsb1 = int(result[16:24],2)
        lsb2 = int(result[24:],2)
        print [msb1, msb2, lsb1, lsb2]
        
        print "[write] Register: ", reg
        #final = spi.xfer([msb1, msb2, lsb1, lsb2])
        #print(final)
        
        for i in range(3): # This will read the register 3 times
            print "[read] Register: ", reg
            read_reg(reg, ubit, mbit)
        print ''

if __name__ == '__main__':
    write_multi_regs(42, 50, 0000000011111111, 0, 1)

