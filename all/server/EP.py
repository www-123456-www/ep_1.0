# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  EP.py
# @Time    : 2021/12/2 11:02
# @Function:

import requests

from all.log import logger
from all.server.token import user_token


# logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

def request_my_daliyEP(token, StationEncode, WhichDay, JsonField="Ep", page=1):
    url = "http://uat.yqwliot.com:5001/EnergyManager/DailyEPApi/GetPageList"
    st = {"StationEncode": StationEncode, "JsonField": JsonField, "WhichDay": WhichDay}
    data = {"queryJson": str(st), "page": page, "rows": 1000}
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
    if data is not None:
        data_page.append(data["rows"])
        data_page.append(data["total"])
    return data_page


def getfrom(token, StationEncode, WhichDay, *JsonField):
    new_rows = {}
    data_page = request_my_daliyEP(token, StationEncode, WhichDay, page=1, JsonField=JsonField[0])
    rows = data_page[0]
    c = []
    WhichDay_set = set()
    for i in rows:
        c.append([i["WhichDay"], i["CabinetEncode"], i["MeterEncode"], i["LoopTitle"], i["EP0"], i["EP1"], i["EP2"],
                  i["EP3"], i["EP4"],
                  i["EP5"], i["EP6"], i["EP7"], i["EP8"], i["EP9"], i["EP10"], i["EP11"], i["EP12"], i["EP13"],
                  i["EP14"], i["EP15"], i["EP16"], i["EP17"], i["EP18"], i["EP19"], i["EP20"], i["EP21"], i["EP22"],
                  i["EP23"], i["EP24"], i["DResult"]])
        # a.append(i["WhichDay"])
        WhichDay_set.add(i["WhichDay"])
    page = data_page[1]
    if page > 1:
        for page_ in range(page - 1):
            data_page = request_my_daliyEP(token, StationEncode, WhichDay, page=page_ + 2)
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
    logger.debug(c[0])
    from_ = [c, list(WhichDay_set)]
    return from_  #


if __name__ == '__main__':
    user = "33333"
    pwd = "333333"
    token = user_token(user=user, pwd=pwd)
    getfrom(token, "TSLBKL10kV", 20211001, 'Ep')
