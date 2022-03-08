# -*- coding: UTF-8 -*-

'''

@author: Ant

@file: baidu.py

@time: 2022/3/8 12:51

@desc: 模拟百度搜索功能,根据用户输入的关键字，返回搜索的HTML结果文件

'''
import requests

if __name__ == "__main__":
    # 定义搜索的url
    url = "https://www.baidu.com/s"

    # 获取用户输入的关键字
    word = input("请输入关键字...")
    # 使用request发送请求
    data = {
        "wd": word,
    }

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    response = requests.get(url=url, data=data, headers=headers)
    response.encoding = "utf-8"  # 设置响应内容的编码
    fp = open("result.html", mode="w", encoding="utf-8")
    fp.write(response.text)
    fp.close()
