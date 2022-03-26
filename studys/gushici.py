# -*- coding: utf-8 -*-
'''
@author: Ant

@file: gushici.py

@time: 2022/3/25 22:16

@desc: 获取古诗词相关内容

'''
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}


def getByClass(url):
    '''
    获取各个年级的古诗词
    :param url: 各个年级的链接
    :return: None
    '''
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = etree.HTML(response.content)
    class_list = html.xpath("//div[@class='typecont']")
    content_list = []
    if class_list:
        for book in class_list:
            book_dict = dict()
            book_name = book.xpath(".//strong/text()")[0]
            # 获取年级下面的所有古诗名称和链接
            gushi_list = book.xpath(".//a/@href")
            book_dict['book_name'] = book_name
            book_dict['gushi_list'] = gushi_list
            content_list.append(book_dict)

    print(content_list)

    # 开始获取具体的古诗内容
    for item in content_list:
        book_name = item.get('book_name')
        gushi_list = item.get('gushi_list')
        article_list = []
        for article_url in gushi_list:
            article = dict()
            article_resp = requests.get(article_url, headers=headers)
            article_resp.encoding = 'utf-8'
            article_html = etree.HTML(article_resp.content)
            article['title'] = article_html.xpath('//*[@id="sonsyuanwen"]/div[1]/h1/text()')[0]
            article['source'] = article_html.xpath('//*[@id="sonsyuanwen"]/div[1]/p//text()')
            article['content'] = article_html.xpath('//*[@id="sonsyuanwen"]/div[1]/div[@class="contson"]/text()')

            # 判断是否有阅读全文


            # 获取注释和释义，https://so.gushiwen.cn/nocdn/ajaxfanyi.aspx?id=FD66AB3E1BC36781

            article_list.append(article)


def main():
    xiaoxue_url = 'https://so.gushiwen.cn/gushi/xiaoxue.aspx'
    getByClass(xiaoxue_url)


if __name__ == "__main__":
    main()
