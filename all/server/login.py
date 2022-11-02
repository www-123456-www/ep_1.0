# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  login.py.py
# @Time    : 2021/11/9 15:59
# @Function:
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  login.py
# @Time    : 2021/11/1 15:40
# @Function:

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# class login():
from all.log import logger

from_ = []


def set_header(token):
    user_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    headers = {
        "token": token,
        "Host": "uat.yqwliot.com:5001",
        "Connection": "keep-alive",
        "Accept": ": */*",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "lr_adms_core_lang=chinese",
        "User-Agent": user_Agent
    }


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
        logger.info(token.text)
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


def getfrom(token, StationEncode, WhichDayS, WhichDayE):
    new_rows = {}
    data_page = request_my(token, StationEncode, WhichDayS, WhichDayE, page=1)
    rows = data_page[0]
    c = []
    WhichDay_set = set()
    for i in rows:
        c.append([i["WhichDay"], i["CabinetEncode"], i["JsonField"], i["EP0"], i["EP1"], i["EP2"], i["EP3"], i["EP4"],
                  i["EP5"], i["EP6"], i["EP7"], i["EP8"], i["EP9"], i["EP10"], i["EP11"], i["EP12"], i["EP13"],
                  i["EP14"], i["EP15"], i["EP16"], i["EP17"], i["EP18"], i["EP19"], i["EP20"], i["EP21"], i["EP22"],
                  i["EP23"]])
        # a.append(i["WhichDay"])
        WhichDay_set.add(i["WhichDay"])
    page = data_page[1]
    if page > 1:
        for page_ in range(page - 1):
            data_page = request_my(token, StationEncode, WhichDayS, WhichDayE, page=page_ + 2)
            for i in data_page[0]:
                c.append([i["WhichDay"], i["CabinetEncode"], i["JsonField"], i["EP0"], i["EP1"], i["EP2"], i["EP3"],
                          i["EP4"],
                          i["EP5"], i["EP6"], i["EP7"], i["EP8"], i["EP9"], i["EP10"], i["EP11"], i["EP12"], i["EP13"],
                          i["EP14"], i["EP15"], i["EP16"], i["EP17"], i["EP18"], i["EP19"], i["EP20"], i["EP21"],
                          i["EP22"],
                          i["EP23"]])
                # a.append(i["WhichDay"])
                WhichDay_set.add(i["WhichDay"])

        print("---------长度+", len(c).__str__())
    from_ = [c, list(WhichDay_set)]
    return from_  #


def request_my(token, StationEncode, WhichDayS, WhichDayE, page=1):
    url = "http://uat.yqwliot.com:5001/EnergyManager/DailyEPApi/GetPageList"
    st = {"StationEncode": StationEncode, "JsonField": "", "IsReport": "1", "IsPage": "0",
          "PK_stationId": "", "WhichDayS": WhichDayS, "WhichDayE": WhichDayE}

    data = {"queryJson": str(st), "page": page}
    headers = {
        "token": token,
        "Host": "uat.yqwliot.com:5001",
        "Connection": "keep-alive",
        "accept": ": */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "lr_adms_core_lang=chinese",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

    }
    re = requests.get(url, params=data, headers=headers)

    json_ = {}
    if re.status_code == 200:
        json_ = re.json()
        # print(json_)
    else:
        print("错误")
    data = json_["data"]
    data_page = []
    print(data["rows"][1])
    if data is not None:
        data_page.append(data["rows"])

        data_page.append(data["total"])
    return data_page


def get_data(user, pwd, StationEncode, WhichDayS, WhichDayE):
    token = user_token(user=user, pwd=pwd)
    return getfrom(token, StationEncode, WhichDayS, WhichDayE)


if __name__ == '__main__':
    user = "wwwww"
    pwd = "wwwww"
    get_data(user, pwd, "TSLST10kV", 20211001, 20211031)  #
