import math

def motorola(value,startbit,width):

    data = [0,0,0,0,0,0,0,0]
    #求起始字节
    #//：求商的整数
    startbyte = startbit // 8
    #求起始字节中的起始位
    staroffsetbit = startbit % 8
    #求字节数
    #math.ceil：向上取整
    lines = math.ceil((width- (8 - staroffsetbit)) / 8)
    #10进制转2进制
    binvalue = bin(value)
    if lines == 1:
        #右填充0的个数
        count = 8 - (7 - staroffsetbit) - width
        finalvalue = binvalue.rjust(count,0)
        #2进制转十进制
        decimal = int(finalvalue, 2)
        #10进制转16进制
        hexadecimal = hex(decimal)
        #写入数据
        data[startbyte] = hexadecimal

    #跨字节
    elif lines > 1:
        #第一个字节填充数据
        finalvalue1 = binvalue[:staroffsetbit+1]
        # 2进制转十进制
        decimal1 = int(finalvalue1, 2)
        # 10进制转16进制
        hexadecimal1 = hex(decimal1)
        # 写入数据
        data[startbyte] = hexadecimal1

        #填充后面的字节
        remainbits = width - (staroffsetbit + 1)
        remainbytes = math.ceil(remainbits / 8)

        while remainbytes >= 1:
            
