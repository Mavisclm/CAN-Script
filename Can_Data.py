class Can_Data():

    def __init__(self):

        self.bit_list = [ 7, 6, 5, 4, 3, 2, 1, 0,
                         15,14,13,12,11,10, 9, 8,
                         23,22,21,20,19,18,17,16,
                         31,30,29,28,27,26,25,24,
                         39,38,37,36,35,34,33,32,
                         47,46,45,44,43,42,41,40,
                         55,54,53,52,51,50,49,48,
                         63,62,61,60,59,58,57,56 ]

        self.empty_bit_list = [ 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0 ]

    def return_original_value(self, physical_value, offset, resolution):
        raw_value = (physical_value - offset) / resolution # 原始值 = （物理值 - 偏移量） / 精度
        print(raw_value)
        # return raw_value

    def return_bin_value(self, original_value, bit_length):
        """
        输入CAN信号的原始值和位宽，返回一个转换后的二进制值。\n
        :param original_value: CAN信号的原始值
        :param bit_length: CAN信号的位宽（信号长度）
        :return: CAN信号的原始值转换的二进制值
        """
        _value = original_value
        _length = bit_length

        _bin_value = bin(_value)[2:] # 去掉二进制前面的0b
        _bin_value = _bin_value.rjust(_length,'0') # 按照位宽从左到右填充0

        return _bin_value


    def return_bin_list(self, start_bit, bit_length, bin_value):
        """
        输入CAN信号的起始位和位宽，和CAN信号的原始值转换的二进制值，返回一个列表，列表存放的是64位二进制的数据。\n
        :param start_bit: CAN信号的起始位
        :param bit_length: CAN信号的位宽（信号长度）
        :param bin_value: CAN信号的原始值转换的二进制值
        :return: 64位二进制的列表
        """
        _bin_list = self.empty_bit_list
        _index = self.bit_list.index(start_bit) # 返回起始位在字节表中的索引值
        _value = bin_value

        for i in range(bit_length): # 根据位宽进行for循环
            _bin_list[_index + i] = int(_value[i]) # 将二进制值填入空字节表，按索引值依次往下填

        return _bin_list # 返回一个填充好字节的64位二进制列表

    def return_can_data_list(self, bin_list):
        """
        输入一个64位二进制的列表，返回一个CAN数据列表，例如：[255, 0, 0, 0, 0, 0, 0, 0]\n
        :param bin_list: 64位二进制的列表
        :return: 返回一个CAN数据列表，例如：[255, 0, 0, 0, 0, 0, 0, 0]
        """

        _bin_list = bin_list

        _str64 = '' # 创建一个空字符串
        _can_data_list = [] # 创建一个空列表

        for i in _bin_list: # 64位二进制列表的元素
            _str64 = _str64 + str(i) # 字符串和字符串相加会一直往后补位
        # print(_str) # 将64位二进制列表转换为64位的字符串

        for j in range(8):
            _str8 = _str64[ j*8 : (j+1)*8 ] #将64位的字符串，分成8份，通过索引值读取，例如：[0:7],[8:15]...
            _int_str8 = int(_str8,2) # 将二进制字符串转换为十进制int类型，例如255
            _can_data_list.append(_int_str8) # 加十进制int类型到空列表中

        return _can_data_list # 将转换好的CAN数据列表返回，例如：[255, 0, 0, 0, 0, 0, 0, 0]

if __name__ == '__main__':

    a = Can_Data()

    b = a.return_bin_value(original_value=255, bit_length=8)
    print(type(255),255,' ---> ',type(b),b)

    c = a.return_bin_list(start_bit=7, bit_length=8 ,bin_value=b)
    print(type(b),b,' ---> ',type(c),c)

    d = a.return_can_data_list(c)
    print(type(c),c,' ---> ',type(d),d)