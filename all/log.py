# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :ep_1.0/all/log.py
# @Time      :2022/6/1 10:41
# @Author    :FIREBAT-wyy
import logging

# logging.basicConfig(level=logging.DEBUG,  format='%(asctime)s-%(filename)s%(funcName)s(%(lineno)d)[%(thread)d]-[%(levelname)s]%(message)s')  # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s-%(filename)s%(funcName)s(%(lineno)d)[%(thread)d]-[%(levelname)s]%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == "__main__":
    pass
