# -*- coding: utf-8 -*-
'''
@author: Ant

@file: haomingzi.py

@time: 2022/3/8 23:57

@desc: 好名字网

'''
import requests

if __name__ == "__main__":
    url = "https://www.hmz.com/bbqm/bestnameauto/"

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    params = "黄_男_2022,3,8,23,0_2_158,1479,44637,535524/"

    response = requests.get(url=url + params, headers=headers)
    response.encoding = "gb2312"
    fp = open("name.html", mode="w", encoding="gb2312")
    fp.write(response.text)
    fp.close()
