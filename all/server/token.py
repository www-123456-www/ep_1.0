# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  token.py
# @Time    : 2021/12/2 11:03
# @Function:
import requests
from requests_toolbelt import MultipartEncoder


def user_token(user, pwd):
    # md5_pwd=hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()
    body = {
        "username": user,
        "password": pwd
    }
    m = MultipartEncoder(fields=body)

    # data = encode_multipart_formdata(body, boundary="----WebKitFormBoundaryOFPi6wpYefHHYqOj")
    post_url = "http://uat.yqwliot.com:5001/User/Login"
    # r = requests.post(post_url,  data=data[0], headers={'Content-Type': data[1]} ,verify=False)
    token = requests.post(post_url, data=m, headers={'Content-Type': m.content_type}, verify=False)
    # print(token.status_code)
    # print(token.text)
    if token.status_code == 200:
        # print(token.text)
        str_to_dict = eval(token.text)
        if str_to_dict["code"] == 200:
            data = str_to_dict["data"]
            token = data
        else:
            token = "账号密码不匹配"
    else:
        token = "token获取失败"
    # print(token)
    return token
