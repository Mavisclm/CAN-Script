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

        self.data_list = [ 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0 ]


    def return_data_list(self,start_bit,bit_length):
        """
        输入CAN信号的起始位和位宽，返回一个列表，列表存放的是64位二进制的数据
        :param start_bit: 该CAN信号的起始位
        :param bit_length: 该CAN信号的位宽（信号长度）
        :return: 64位二进制的列表
        """
        list = self.data_list
        _index = self.bit_list.index(start_bit)

        for i in range(bit_length):
            list[_index + i] = 1

        return list


if __name__ == '__main__':
    a = Can_Data()
    b = a.return_data_list(10,6)
    print(b)