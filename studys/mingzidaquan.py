# -*- coding: UTF-8 -*-

'''

@author: Ant

@file: mingzidaquan.py

@time: 2022/3/17 7:22

@desc: 抓取名字大全网站上的名字，并存储在文件中，名字大全网址：http://www.resgain.net/xmdq.html

'''
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
name_list = []


def main():
    '''
          1、数据获取地址：http://www.resgain.net/xmdq.html，GET方式
          2、获取所有的姓氏，采用BeautifulSoup4数据解析方式
          3、获取姓氏对应的名字
          4、每个姓氏一个文件保存
          '''
    url = "http://www.resgain.net/xmdq.html"

    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")
    first_name_list = soup.select('a.btn.btn2')
    first_names = []

    # 获取姓氏
    for item in first_name_list:
        first_name_item = {}
        first_name_item["value"] = item.text[0:item.text.index('姓')]
        first_name_item["href"] = 'http:' + item['href']
        first_names.append(first_name_item)

    # 依次获取姓氏下面的名字
    for i in range(0, len(first_names)):
        first_item = first_names[i]
        name_href = first_item['href']
        name_href = name_href[0:name_href.find("name_list.html")]
        first_name = first_item['value']

        # 获取男孩名链接和女孩名链接
        url_list = [name_href + 'name/boys.html', name_href + 'name/girls.html']
        # 分别获取男孩和女孩的名字
        for i in range(len(url_list)):
            sex = "男" if i == 0 else "女"
            getNames(url_list[i], first_name, sex)

    print("Over...........!")


def getNames(url, first_name, sex):
    '''
    根据传入的url，获取名字并保存在文件中
    :param url:
    :param first_name:姓
    :param sex:性别
    :return:
    '''
    # 获取姓名
    print(url)
    name_response = requests.get(url=url, headers=headers)
    name_response.encoding = 'utf-8'
    name_soup = BeautifulSoup(name_response.text, 'lxml')
    name_div_list = name_soup.select('div.btn.btn-default.btn-lg.namelist > div:nth-of-type(1)')
    fb = open("mingzidaquan.txt", "a+", encoding="utf-8")
    for item in name_div_list:
        name_item = dict()
        name_item["first_name"] = first_name
        name_item["name"] = item.text
        name_item["sex"] = sex
        fb.write(str(name_item) + "\r")
    fb.close()

    # 判断是否有下一页
    pagination = name_soup.select("ul.pagination > li")
    if pagination:
        for page in pagination:
            page_name = page.find("a").text
            if page_name == "下一页":
                getNames(url[0:url.find("/name")] + page.find("a")["href"], first_name, sex)


if __name__ == "__main__":
    main()
