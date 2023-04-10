# -*- coding: utf-8 -*-
#####
"""
# author：vehicle_ma, 2023/2/10
"""
######

import cantools

class DbcInfo:
    """
    用于读取dbc文件，返回dbc信息
    """
    def __init__(self, input_file):
        """
        init
        """
        self.dbc_file = input_file
        self.dbc_info = cantools.db.load_file(self.dbc_file)

    def get_message(self, frame_id):
        """
        return message，特别强调，frame_id输入10进制即可，同时必须是int型数据，不能是字符串
        """
        return self.dbc_info.get_message_by_frame_id(frame_id)   #直接返回message的所有信息

    def get_message_name(self, frame_id):
        """
        return message name
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).name

    def get_message_name_by_message_id(self, frame_name):
        """
        return message id by message name
        """
        return self.dbc_info.get_message_by_name(frame_name).frame_id

    def get_signals_list(self, frame_id):
        """
        return signals list
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).signal_tree    #这里返回的是message中signal的list，包含一个message中所有的signal

    def get_signal(self, frame_id, signal_name):
        """
        return signal, 输入message id和signal name
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).get_signal_by_name(signal_name)

    def get_signal_config_maximum(self, frame_id, signal_name):
        """
        return signal maximum
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).get_signal_by_name(signal_name).maximum

    def get_signal_config_minimum(self, frame_id, signal_name):
        """
        return signal minimum
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).get_signal_by_name(signal_name).minimum

    def get_signal_config_scale(self, frame_id, signal_name):
        """
        return signal scale，这里指的是signal定义中其取值范围的间隔，
        比如从1到10，每个2取一个值，scale就是2
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).get_signal_by_name(signal_name).scale

    def get_signal_config_comment(self, frame_id, signal_name):
        """
        return signal comment，signal说明
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).get_signal_by_name(signal_name).comment

    def signal_config_value_description_to_num(self, frame_id, signal_name, value_str):
        """
        return signal value description
        这里需要特别说明下，有些signal取值不是正常的数值，而是文字描述，
        这个在定义中是个表，比如1：open, 2:close, 4:ignore，
        本函数的意思是当你取到这个字符串，比如close时，能够返回这个字符串在对应中的数字2，
        这在解析和保存以及后续发送中是很有用的。
        """
        return self.dbc_info.get_message_by_frame_id(frame_id).get_signal_by_name(signal_name).\
            choice_string_to_number(value_str)


if __name__ == '__main__':
    dbc_info = DbcInfo('BJEV_C62XF06_ICAN_Telematics_CAN_V1.15_20220810.dbc')
    #test，根据自己需求使用上述函数即可
    #frame_id输入10进制即可，同时必须是int型数据，不能是字符串
    # print(dbc_info.get_message_name(0x280))
    info1 = dbc_info.get_signal(0x180,'STEERING_ANGLE_SPEED')
    print(info1)
    # print(dbc_info.get_message_name_by_message_id('EMS_GENERAL_STATUS'))

