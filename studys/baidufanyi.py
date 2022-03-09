# -*- coding: utf-8 -*-
'''
@author: Ant

@file: baidufanyi.py

@time: 2022/3/8 23:39

@desc: 模拟百度翻译

'''
import json

import requests

if __name__ == "__main__":
    # 定义URL
    url = "https://fanyi.baidu.com/sug"

    # 输入要翻译的单词
    word = input("请输入单词...")

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    # 翻译请求
    data = {
        "kw": word
    }
    response = requests.post(url=url, data=data, headers=headers)
    fp = open(word + ".json", mode="w", encoding="utf-8")
    json.dump(obj=response.json(), fp=fp, ensure_ascii=False)
    fp.close()
