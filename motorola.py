import math

# def bytes_hex(data):
#     hex_data = []
#     for i in range(len(data)):
#         datas = data[i]
#         # print(type(datas))
#         hex_data.append(datas)
#     return hex_data

def motorola(value,startbit:int,width:int):

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
        # print(lines)
    #10进制转2进制
    binvalue = bin(value)[2:]
    # print(binvalue)
    if lines == 1:
        # 右填充0,8代表补充至8位
        finalvalue = binvalue.rjust(8,'0')
        # print(finalvalue)
        #2进制转十进制
        decimal = int(finalvalue, 2)
        # print(decimal)
        #10进制转16进制
        hexadecimal = hex(decimal).upper()    #type:str
        # print(decimal)
        #写入数据
        data[startbyte] = hexadecimal

    #跨字节
    elif lines > 1:
        binvalue = binvalue.rjust(width, '0')
        # print(binvalue)
        #第一个字节填充数据
        finalvalue1 = binvalue[:startoffsetbit+1]
        # print(finalvalue1)
        # 2进制转十进制
        decimal1 = int(finalvalue1, 2)
        # 10进制转16进制
        hexadecimal1 = hex(decimal1).upper()    #type:str
        # 写入数据
        data[startbyte] = hexadecimal1

        #填充后面的字节
        remainbits = width - (startoffsetbit + 1)
        remainbytes = math.ceil(remainbits / 8)

        if remainbytes == 1:
            finalvalue2 = binvalue[startoffsetbit + 1:]
            # 右填充0,8代表补充至8位
            finalvalue2 = finalvalue2.rjust(8, '0')
            # print(finalvalue2)
            # 2进制转十进制
            decimal2 = int(finalvalue2, 2)
            # 10进制转16进制
            hexadecimal2 = hex(decimal2).upper()    #type:str
            # 写入数据
            data[startbyte + 1] = hexadecimal2
        i = 1
        while remainbytes > 1:
            finalvalue3 = binvalue[startoffsetbit + 1 + 8 * (i - 1):startoffsetbit + 1 + 8 * i]
            # finalvalue3 = binvalue[startoffsetbit + 2:startoffsetbit + 2 + 8]
            # print(finalvalue3+'12X')
            if finalvalue3 == '':
                data[startbyte + i] = 0
            elif finalvalue3 != '':
                # print('finalvalue3='+finalvalue3)
                # 2进制转十进制
                decimal3 = int(finalvalue3, 2)
                # 10进制转16进制
                hexadecimal3 = hex(decimal3).upper()    #type:str
                # 写入数据
                data[startbyte + i] = hexadecimal3

            i += 1
            # print("i="+str(i))
            remainbits = width - (startoffsetbit + 1) - 8 * (i - 1)
            # print(remainbits)
            remainbytes = math.ceil(remainbits / 8)
            # print('remainbytes='+str(remainbytes))
            if remainbytes == 1:
                finalvalue4 = binvalue[startoffsetbit + 1 + 8 * (i - 1):]
                # 右填充0,8代表补充至8位
                finalvalue4 = finalvalue4.rjust(8, '0')
                # print(finalvalue4)
                # 2进制转十进制
                decimal4 = int(finalvalue4, 2)
                # 10进制转16进制
                hexadecimal4 = hex(decimal4).upper()    #type:str
                # 写入数据
                data[startbyte + i] = hexadecimal4
                # break
            # else:
            #     i += 1
            #     continue
    # data = data.replace("'","")
    # print(data)
    return data
    # return bytes_hex(data)

if __name__ == '__main__':
    motorola(15360, 39, 14)
    print(motorola(15360, 39, 14))
    # print(list(map(lambda x, y: x + y, motorola(12, 19, 4), motorola(15360, 39, 14))))
    print(motorola(12, 19, 4))
    # print(motorola(12, 19, 4)+motorola(15360, 39, 14))
    # motorola(2, 21, 2)
    # motorola(1, 7, 2)
    motorola(1234567, 15, 32)
    print(motorola(1234567, 15, 32))