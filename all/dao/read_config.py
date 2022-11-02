# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  read_config.py
# @Time    : 2021/11/12 16:02
# @Function:
import json

json_path = "config/config_json.txt"
time_path = "config/time.txt"
name_path = "config/name.txt"


def objName_name(obj):
    """
    :param obj: json 中的对象{}
    :return:
    """
    return list(obj.keys())


def data_config():
    f = open(json_path, "r", encoding="utf-8")  # 读取文件参数
    return json.load(f)


def data_time():
    f = open(time_path, "r", encoding="utf-8")  # 读取文件参数
    return json.load(f)


def dats_name():
    f = open(name_path, "r", encoding="utf-8")  # 读取文件参数
    return json.load(f)


def get_StationEncode_s():
    return objName_name(data_config())


def get_StationEncode_time():
    return objName_name(data_time())


def get_days(StationEncode):  # 【起始时间，终止时间】
    # return data_config()[ StationEncode ][0]["days"] 配置文件更改
    return data_time()[StationEncode]


def getsheets(StationEncode):
    return data_config()[StationEncode][0]["file"]


def get_Sheetnames(StationEncode):  # 某个电站下的 多个 sheet [ {},{},{}]  #有序 且 {}中只有一个对象
    name = []
    for i in getsheets(StationEncode):
        name.append(objName_name(i)[0])
    return name


def get_params(StationEncode, SheetName):
    list_sheet = getsheets(StationEncode)
    params = []
    for i in list_sheet:
        name = objName_name(i)[0]
        if name == SheetName:
            params = i[SheetName]
    return params


def get_df_If(params):
    """
    :param params: get_params(StationEncode,SheetName)
    :return: [(柜子，参数),(),()]
    """
    df_If = []
    for i in params:
        key_ = objName_name(i)[0]  # guizi
        for j in i[key_]:
            df_If.append((key_, j))
    print(df_If)
    return df_If


def get_name():
    k_v = dats_name()[0]
    name = objName_name(k_v)[0]
    pwd = k_v[name]
    return [name, pwd]


"""
def get_days_list(day):

    days=[]
    i=0
    while i+day[0] <= day[1]:
        days.append(str(i+day[0]))
        i += 1
    return days
"""
