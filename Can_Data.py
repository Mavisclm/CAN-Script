# -*- coding: utf-8 -*-
# @Time ： 2023/4/4 18:18
# @Auth ： JeremyChim
# @File ：Can_Script.py
# @IDE ：PyCharm
# @Github ：https://github.com/Mavisclm/CAN-Script

class Can_Data():

    def __init__(self, physical_value, offset, resolution, bit_length, start_bit, byte=8):
        """
        CAN数据所需要的属性有5个：
        :param physical_value: 物理值
        :param offset: 偏移量
        :param resolution: 精度
        :param bit_length: 位宽（信号长度）
        :param start_bit: 起始位
        :param byte: 字节长度，CAN类型为8个字节，CANFD类型为64字节，默认为CAN类型
        """
        self.physical_value = physical_value
        self.offset = offset
        self.resolution = resolution
        self.bit_length = bit_length
        self.start_bit = start_bit
        self.byte = byte
        # print(byte)

        self.bit_list,self.empty_bit_list = self.creation_bit_list(self.byte) # 创建 字节索引表，空字节表
        # print(self.bit_list,self.empty_bit_list)

        # self.bit_list = [ 7, 6, 5, 4, 3, 2, 1, 0,
        #                  15,14,13,12,11,10, 9, 8,
        #                  23,22,21,20,19,18,17,16,
        #                  31,30,29,28,27,26,25,24,
        #                  39,38,37,36,35,34,33,32,
        #                  47,46,45,44,43,42,41,40,
        #                  55,54,53,52,51,50,49,48,
        #                  63,62,61,60,59,58,57,56 ]

        # self.empty_bit_list = [ 0, 0, 0, 0, 0, 0, 0, 0,
        #                         0, 0, 0, 0, 0, 0, 0, 0,
        #                         0, 0, 0, 0, 0, 0, 0, 0,
        #                         0, 0, 0, 0, 0, 0, 0, 0,
        #                         0, 0, 0, 0, 0, 0, 0, 0,
        #                         0, 0, 0, 0, 0, 0, 0, 0,
        #                         0, 0, 0, 0, 0, 0, 0, 0,
        #                         0, 0, 0, 0, 0, 0, 0, 0 ]

    def return_can_data(self):
        """
        根据Can_Data类的实例属性，通过四个函数，返回一个CAN数据列表。 \n
        函数1：return_raw_value，返回原始值 \n
        函数2：return_bin_value，返回二进制值 \n
        函数3：return_bin_list， 返回二进制表 \n
        函数4：return_can_data_list，返回CAN报文表 \n
        :return:返回一个CAN数据列表，例如：[255, 0, 0, 0, 0, 0, 0, 0]
        """
        raw_value = self.return_raw_value(physical_value = self.physical_value,
                                          offset = self.offset,
                                          resolution = self.resolution
                                          )
        # print(raw_value)

        bin_value = self.return_bin_value(raw_value = raw_value,
                                          bit_length = self.bit_length
                                          )
        # print(bin_value)

        bin_list = self.return_bin_list(bin_value = bin_value,
                                        start_bit = self.start_bit,
                                        bit_length = self.bit_length)
        # print(bin_list)

        can_data_list = self.return_can_data_list(bin_list = bin_list,
                                                  byte = self.byte)
        # print(can_data_list)
        return can_data_list

    def return_raw_value(self, physical_value, offset, resolution):
        """
        输入一个物理值、偏移量、精度，
        根据公式：原始值 = （物理值 - 偏移量） / 精度，
        返回原始值。\n
        :param physical_value:物理值
        :param offset:偏移量
        :param resolution:精度
        :return:返回原始值，注意类型是float
        """
        raw_value = (physical_value - offset) / resolution # 原始值 = （物理值 - 偏移量） / 精度
        # print(raw_value)
        return raw_value # 返回原始值，注意类型是float

    def return_bin_value(self, raw_value, bit_length):
        """
        输入CAN信号的原始值和位宽，返回一个转换后的二进制值。\n
        :param raw_value: CAN信号的原始值
        :param bit_length: CAN信号的位宽（信号长度）
        :return: CAN信号的原始值转换的二进制值
        """
        raw_value = int(raw_value) # 原始值一般为float类型，转换int类型，去除小数点
        bin_value = bin(raw_value)[2:] # 去掉二进制前面的0b
        bin_value = bin_value.rjust(bit_length,'0') # 按照位宽从左到右填充0
        return bin_value

    def return_bin_list(self, bin_value, start_bit, bit_length):
        """
        输入CAN信号的起始位和位宽，和CAN信号的原始值转换的二进制值，
        将二进制值填入空字节表，按索引值依次往下填，填入顺序遵循Motorola MSB顺序，
        返回一个列表，列表存放的是64位二进制的数据。\n
        :param bin_value: CAN信号的原始值转换的二进制值
        :param start_bit: CAN信号的起始位
        :param bit_length: CAN信号的位宽（信号长度）
        :return: 64位二进制的列表
        """
        bin_list = self.empty_bit_list
        start_bit_index = self.bit_list.index(start_bit) # 返回起始位在字节表中的索引值

        for i in range(bit_length): # 根据位宽进行for循环
            bin_list[start_bit_index + i] = int(bin_value[i]) # 将二进制值填入空字节表，按索引值依次往下填，填入顺序遵循Motorola MSB顺序

        return bin_list # 返回一个填充好字节的64位二进制列表

    def return_can_data_list(self, bin_list, byte):
        """
        输入一个64位二进制的列表，返回一个CAN数据列表，例如：[255, 0, 0, 0, 0, 0, 0, 0]\n
        :param bin_list: 64位二进制的列表
        :return: 返回一个CAN数据列表，例如：[255, 0, 0, 0, 0, 0, 0, 0]
        """

        str64 = '' # 创建一个空字符串，用来存放二进制的字符串，一共64位
        can_data_list = [] # 创建一个空列表，用来存放8位16进制的CAN报文，不过由于是int类型，所以显示为十进制，例如：FF显示为255

        for i in bin_list: # 64位二进制列表的元素
            str64 = str64 + str(i) # 字符串和字符串相加会一直往后补位
        # print(_str) # 将64位二进制列表转换为64位的字符串

        for j in range(byte):
            str8 = str64[ j*8 : (j+1)*8 ] #将64位的字符串，分成8份，通过索引值读取，例如：[0:7],[8:15]...
            int_str8 = int(str8,2) # 将二进制字符串转换为十进制int类型，例如255
            can_data_list.append(int_str8) # 加十进制int类型到空列表中

        return can_data_list # 将转换好的CAN数据列表返回，例如：[255, 0, 0, 0, 0, 0, 0, 0]

    def creation_bit_list(self, byte):
        """
        创建一个字节索引表，空字节表\n
        :param byte: 字节长度，CAN类型为8个字节，CANFD类型为64字节，默认为CAN类型
        :return: 返回两个列表，一个字节索引表和一个空字节表
        """

        bit_list = []
        empty_bit_list = []

        for i in range(byte): # 如果byte=8 ，for循环8次；如果byte=64 ，for循环64次。
            for j in range(8): # 一个字节8个bit位
                bit = 8 * (i + 1) - (j + 1) # 根据索引值计算字节位，例如i=0，j=0，bit = 7 ，所以字节索引表第一位是7
                bit_list.append(bit) # 填充8个字节位置 到 字节索引表
                empty_bit_list.append(0) # 填充8个0 到 空字节表

        # a, b = bit_list, empty_bit_list
        # print(len(a), a)
        # print(len(b), b)
        return bit_list, empty_bit_list

if __name__ == '__main__':

    a = Can_Data(physical_value=25.5, offset=0, resolution=0.1, bit_length=8, start_bit=511, byte=64)
    print(a.return_can_data())

    a = Can_Data(physical_value=25.5, offset=0, resolution=0.1, bit_length=8, start_bit=63)
    print(a.return_can_data())

    #独立调用每个函数
    b = a.return_raw_value(physical_value=25.5, offset=0, resolution=0.1)
    print('输入一个物理值，返回原始值。', end=' '*5)
    print(type(255),255,' ---> ',type(b),b)

    c = a.return_bin_value(raw_value=b, bit_length=8)
    print('输入原始值，返回二进制值。', end=' '*5)
    print(type(b),b,' ---> ',type(c),c)

    d = a.return_bin_list(start_bit=7, bit_length=8 ,bin_value=c)
    print('输入二进制值，返回二进制表。', end=' '*5)
    print(type(c),c,' ---> ',type(d),d)

    e = a.return_can_data_list(bin_list = d, byte=8)
    print('输入二进制表，返回CAN报文表。', end=' ' * 5)
    print(type(d),d,' ---> ',type(e),e)

    bit_list, empty_bit_list = a.creation_bit_list(byte=64)
    print('创建一个字节索引表', end=' ' * 5)
    print(bit_list)
    print('创建一个空字节表', end=' ' * 5)
    print(empty_bit_list)
