# CAN-Script
 一个CAN工具的自动化脚本。
> Github链接：https://github.com/Mavisclm/CAN-Script

## Can_Data.py
通过CAN数据所需要的5个属性：物理值、偏移量精度、位宽、起始位，输出原始值。

```python
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
```