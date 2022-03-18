# -*- coding: UTF-8 -*-
'''

@author: Ant

@file: meimingteng.py

@time: 2022/3/17 5:57

@desc：美名腾名字大全

'''
import requests
from bs4 import BeautifulSoup


def getName(url, headers, filename=""):
    '''
    获取名字函数
    :param url:链接
    :param headers：请求头
    :param filename:写入的文件
    :return:无
    '''
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    xingming_div = soup.select("div.xingming2")
    boy_name_div = xingming_div[0]
    girl_name_div = xingming_div[1]
    name_list = []
    # 获取男宝宝姓名
    boy_name_list = boy_name_div.select("ul > li > a")
    for boy in boy_name_list:
        name_list.append({"sex": "男", "name": boy.text})
    # 获取女宝宝姓名
    girl_name_list = girl_name_div.select("ul > li > a")
    for gril in girl_name_list:
        name_list.append({"sex": "男", "name": gril.text})

    # 将结果写入文件
    fb = open("names.txt", "a+",encoding="utf-8")
    for i in range(len(name_list)):
        fb.write(str(name_list[i]) + "\r")

    fb.close()


if __name__ == "__main__":
    '''
    1、数据获取地址：https://www.meimingteng.com/Sample/，GET方式
    2、获取所有的姓氏，采用BeautifulSoup4数据解析方式
    3、获取姓氏对应的名字
    4、每个姓氏一个文件保存
    '''

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    url = "https://www.meimingteng.com/Sample/"

    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"

    # 创建bs4对象
    soup = BeautifulSoup(response.text, "lxml")
    # 提取所有的姓氏
    firstName_li_list = soup.select('.xingshi2 > ul > li')
    name_root_url = "https://www.meimingteng.com/Sample/"
    for i in range(len(firstName_li_list)):
        li = firstName_li_list[i]
        firstName = li.a.text
        sub_url = name_root_url + li.a['href']
        getName(sub_url, headers)
    print(1)
