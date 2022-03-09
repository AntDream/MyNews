# -*- coding: utf-8 -*-
'''
@author: Ant

@file: haomingzi.py

@time: 2022/3/8 23:57

@desc: 好名字网

'''
import requests
from lxml import etree

if __name__ == "__main__":
    url = "https://www.hmz.com/bbqm/bestnameauto/"

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    params = "黄_男_2022,3,8,23,0_2_158,1479,44637,535524/"

    response = requests.get(url=url + params, headers=headers)
    response.encoding = "gb2312"

    html = etree.HTML(response.content)

    # 获取名字信息
    name_list = html.xpath('//div[@class="list_new"]/div')
    # 获取名字里的具体字段
    name_infos = []
    if name_list:
        for name_item in name_list:
            name_info = {}
            print(name_item)
            name_dict = name_item.xpath('//ul[@class="name"]/li/text()')
            first_name = name_dict[0]
            if len(name_dict) > 2:
                last_name = name_dict[1] + name_dict[2]
            else:
                last_name = name_dict[1]
            name_info['first_name'] = first_name
            name_info['last_name'] = last_name
            name_infos.append(name_info)

    print(len(name_infos))
    print(name_infos)

    # fp = open("name.html", mode="w", encoding="gb2312")
    # fp.write(response.text)
    # fp.close()
