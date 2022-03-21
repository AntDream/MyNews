# -*- coding: utf-8 -*-
'''
@author: Ant

@file: haomingzi.py

@time: 2022/3/8 23:57

@desc: 好名字网

'''
import requests
from lxml import etree
import time

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

name_list = []


def getHaoMingZi():
    '''
    获取好名字
    :return:
    '''
    url = "https://www.hmz.com/bbqm/bestnameauto/"

    params = "黄_男_2022,3,8,23,0_2_158,1479,44637,535524/"

    response = requests.get(url=url + params, headers=headers)
    response.encoding = "gb2312"

    html = etree.HTML(response.content)

    # 获取名字信息
    name_list = html.xpath('//div[@class="list_new"]/div[contains(@class,"nameBox")]//ul[@class="name"]')
    # 获取名字里的具体字段
    name_infos = []
    if name_list:
        for name_item in name_list:
            name_info = {}
            name_dict = name_item.xpath('li/text()')
            first_name = name_dict[0]
            if len(name_dict) > 2:
                last_name = name_dict[1] + name_dict[2]
            else:
                last_name = name_dict[1]
            name_info['first_name'] = first_name
            name_info['last_name'] = first_name + last_name
            name_infos.append(name_info)

    print(len(name_infos))
    print(name_infos)


def getBaiJiaXing():
    '''
    获取百家姓
    :return:百家姓
    '''
    url = 'https://www.hmz.com/xing/'
    response = requests.get(url=url, headers=headers)
    response.encoding = "gb2312"
    html = etree.HTML(response.content)
    xing_list = html.xpath("//div[@class='xingshi']//li/a/text()")
    return xing_list


def getXmData(first_name, sex, ns):
    '''
    获取姓名信息
    :param first_name:姓氏
    :param sex:性别
    :param ns:单名还是双名，1-单名，2-双名
    :return:
    '''
    try:
        url = 'https://www.hmz.com/xmdata1.html'
        data = {
            'xing': first_name,
            'sex': sex,
            'ymd': '',  # 年月日时
            'cymd': '',
            'ns': ns,  # 名字形式，单字和双字
            'sduyin': '',
            'wduyin': '',
            'szi': '',
            'wzi': '',
            'swx': '',
            'wwx': '',
            'bh': '',
            'city': ''
        }

        response = requests.post(url=url, data=data, headers=headers)
        response.encoding = "gb2312"
        json = response.json()
        lastname_list = json['list']
        if lastname_list and type(lastname_list) == list:
            for item in lastname_list:
                name_dict = dict()
                name_dict['first_name'] = first_name
                name_dict['sex'] = sex
                name_dict['name'] = first_name + item['ming']
                name_list.append(name_dict)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # getHaoMingZi()
    first_name_list = getBaiJiaXing()
    total_name = 0

    for i in range(100):
        first_name = first_name_list[i]
        fb = open("haomingzi.txt", mode="a+", encoding="utf-8")
        print("正在获取{}姓名字".format(first_name))
        name_list = []
        # 每个姓氏获取男女、单双名各获取1000次
        num = 1000
        print("正在获取{}姓名字，男孩，双名".format(first_name))
        for i in range(num):
            getXmData(first_name, '男', 2)
        time.sleep(60)

        print("正在获取{}姓名字，男孩，单名".format(first_name))
        for i in range(num):
            getXmData(first_name, '男', 1)
        time.sleep(60)

        print("正在获取{}姓名字，女孩，双名".format(first_name))
        for i in range(num):
            getXmData(first_name, '女', 2)
        time.sleep(60)

        print("正在获取{}姓名字，女孩，单名".format(first_name))
        for i in range(num):
            getXmData(first_name, '女', 1)
        time.sleep(60)

        for name in name_list:
            fb.write(str(name) + "\r")

        total_name = total_name + len(name_list)
        print("{}姓名字共{}个".format(first_name, len(name_list)))
        fb.close()

    print("姓名共个数为：", total_name)
    # fp = open("name.html", mode="w", encoding="gb2312")
    # fp.write(response.text)
    # fp.close()
