import math

def motorola(value,startbit,width):

    data = [0,0,0,0,0,0,0,0]
    #求起始字节
    #//：求商的整数
    startbyte = startbit // 8
    #求起始字节中的起始位
    startoffsetbit = startbit % 8
    #求字节数
    #math.ceil：向上取整
    lines = math.ceil((width- (8 - startoffsetbit)) / 8) + 1
    print(lines)
    #10进制转2进制
    binvalue = bin(value)[2:]
    print(binvalue)
    if lines == 1:
        #右填充0的个数
        count = 8 - (7 - startoffsetbit) - width
        finalvalue = binvalue.rjust(count,'0')
        #2进制转十进制
        decimal = int(finalvalue, 2)
        #10进制转16进制
        hexadecimal = hex(decimal)[2:]
        #写入数据
        data[startbyte] = hexadecimal

    #跨字节
    elif lines > 1:
        #第一个字节填充数据
        finalvalue1 = binvalue[:startoffsetbit+1]
        print(finalvalue1)
        # 2进制转十进制
        decimal1 = int(finalvalue1, 2)
        # 10进制转16进制
        hexadecimal1 = hex(decimal1)[2:]
        # 写入数据
        data[startbyte] = hexadecimal1

        #填充后面的字节
        remainbits = width - (startoffsetbit + 1)
        remainbytes = math.ceil(remainbits / 8)

        if remainbytes == 1:
            finalvalue2 = binvalue[startoffsetbit + 1:]
            print(finalvalue2)
            # 右填充0数
            count = 8 - len(finalvalue2)
            finalvalue2 = finalvalue2.rjust(count, '0')
            # 2进制转十进制
            decimal2 = int(finalvalue2, 2)
            # 10进制转16进制
            hexadecimal2 = hex(decimal2)[2:]
            # 写入数据
            data[startbyte + 1] = hexadecimal2

        while remainbytes > 1:
            i = 2
            remainbits = width - (startoffsetbit + 1) - 8 * (i - 1)
            remainbytes = math.ceil(remainbits / 8)
            finalvalue3 = binvalue[startoffsetbit + 1 + 8 * (i- 2):startoffsetbit + 1 + 8 * (i- 1)]
            print(finalvalue3)
            # 2进制转十进制
            decimal3 = int(finalvalue3, 2)
            # 10进制转16进制
            hexadecimal3 = hex(decimal3)[2:]
            # 写入数据
            data[startbyte + i] = hexadecimal3

            if remainbytes == 1:
                finalvalue4 = binvalue[startoffsetbit + 1 + 8 * (i - 1):]
                # 右填充0数
                count = 8 - len(finalvalue4)
                finalvalue4 = finalvalue4.rjust(count, '0')
                # 2进制转十进制
                decimal4 = int(finalvalue4, 2)
                # 10进制转16进制
                hexadecimal4 = hex(decimal4)[2:]
                # 写入数据
                data[startbyte + i] = hexadecimal4
                break

            i += 1

    print(data)
    return data

if __name__ == '__main__':
    motorola(15360, 39, 14)
    # motorola(8, 19, 4)