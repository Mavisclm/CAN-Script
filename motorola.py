import math

def motorola(startbit:int,width:int,phy_value,offset,resolution):
    """
    :param startbit: 起始位
    :param width: 位宽
    :param phy_value: 物理值
    :param offset: 偏移量
    :param resolution: 精度
    :return:
    """
    #原始值=（物理值-偏移量）/精度
    value = int((phy_value-offset)/resolution)
    data = [0,0,0,0,0,0,0,0]
    #求起始字节
    #//：求商的整数
    startbyte = startbit // 8
    #求起始字节中的起始位
    startoffsetbit = startbit % 8
    #求字节数
    flag = width- (8 - startoffsetbit)
    if flag > 0:
        #math.ceil：向上取整
        lines = math.ceil((width- (8 - startoffsetbit)) / 8)
        # print(lines)
    elif flag < 0:
        # math.ceil：向上取整
        lines = math.ceil((width + startoffsetbit) / 8)
    elif flag == 0:
        lines = 1
    #10进制转2进制
    binvalue = bin(value)[2:]
    # print(binvalue)
    if lines == 1:
        # 从右填充0,8代表补充至8位
        finalvalue = binvalue.rjust(width,'0')  #在左边填充0至位宽
        finalvalue = finalvalue.ljust(startoffsetbit+1,'0')     #右边空位补充0
        #2进制转十进制
        decimal = int(finalvalue, 2)
        #写入数据
        data[startbyte] = decimal

    #跨字节
    elif lines > 1:
        binvalue = binvalue.rjust(width, '0')
        #第一个字节填充数据
        finalvalue1 = binvalue[:startoffsetbit+1]
        # 2进制转十进制
        decimal1 = int(finalvalue1, 2)
        # 写入数据
        data[startbyte] = decimal1

        #填充后面的字节
        remainbits = width - (startoffsetbit + 1)
        remainbytes = math.ceil(remainbits / 8)

        if remainbytes == 1:
            finalvalue2 = binvalue[startoffsetbit + 1:]
            # 从右填充0,8代表补充至8位
            finalvalue2 = finalvalue2.ljust(8, '0')
            # 2进制转十进制
            decimal2 = int(finalvalue2, 2)
            # 写入数据
            data[startbyte + 1] = decimal2
        i = 1
        while remainbytes > 1:
            finalvalue3 = binvalue[startoffsetbit + 1 + 8 * (i - 1):startoffsetbit + 1 + 8 * i]
            if finalvalue3 == '':
                data[startbyte + i] = 0
            elif finalvalue3 != '':
                # 2进制转十进制
                decimal3 = int(finalvalue3, 2)
                # 写入数据
                data[startbyte + i] = decimal3

            i += 1
            remainbits = width - (startoffsetbit + 1) - 8 * (i - 1)
            remainbytes = math.ceil(remainbits / 8)
            if remainbytes == 1:
                finalvalue4 = binvalue[startoffsetbit + 1 + 8 * (i - 1):]
                # 从右填充0,8代表补充至8位
                finalvalue4 = finalvalue4.rjust(8, '0')
                # 2进制转十进制
                decimal4 = int(finalvalue4, 2)
                # 写入数据
                data[startbyte + i] = decimal4

    return data

if __name__ == '__main__':
    print(motorola(39,14,18,3,0.0009765625))
    print(motorola(31, 8, 55,0,1))
    print(motorola(54, 1, 1, 0, 1))
    print(motorola(45, 3, 6, 0, 1))
    # print(list(map(lambda x, y: x + y, motorola(12, 19, 4), motorola(15360, 39, 14))))