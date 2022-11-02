# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  to_pandas.py
# @Time    : 2021/11/12 16:01
# @Function:
import pandas as pp


def data_to_daysData(data, day):
    """
    :param data: 所有的data
    :param day:
    :return: 每天的 df
    """
    df = pp.DataFrame(data)
    return df[df[0] == day]


def set_index_if(df, df_if):
    """
    :param df: 每天的 df    : data_to_daysData(data,day)
    :param df_if:  过滤条件
    :return:
    """
    setindex_df = df.set_index([1, 2])  # 设置索引 df.set_index(*column_indexer|*row_indexer )
    # 已存在的列标签设置为 DataFrame 行索引
    df = setindex_df.loc[df_if]  # df.loc(*row_indexer,*column_indexer)
    return df


def r_xlsx(path, sheetName_list):
    """
    :param path:
    :param sheetName_list:
    :return: {Sheetname ：df，  name: df  }
    """
    df = {}
    with pp.ExcelFile(path) as xlsx:  # 获取文件
        for name in sheetName_list:
            df[name] = pp.read_excel(xlsx, name)
    return df


def w_xlsx(path, sheetName_list, data):
    with pp.ExcelWriter(path) as writer:  # 获取文件
        for name in sheetName_list:
            df = pp.DataFrame(data)
            df.to_excel(writer, sheet_name=str(name), index=False, header=False)
