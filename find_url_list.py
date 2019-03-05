#通过爬虫
from bs4 import BeautifulSoup
import requests
import re
import time
import pymongo

#列表页
'''
宪法研究
行政研究
法政评论
港澳台法制
热点聚焦
学术资讯
'''
url_list = ['http://www.calaw.cn/more.asp?channel=%CF%DC%B7%A8%D1%D0%BE%BF&type1=%CF%DC%B7%A8%BB%F9%B1%BE%C0%ED%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%CF%DC%B7%A8%D1%D0%BE%BF&type1=%B9%FA%BC%D2%D6%C6%B6%C8',
            'http://www.calaw.cn/more.asp?channel=%CF%DC%B7%A8%D1%D0%BE%BF&type1=%BB%F9%B1%BE%C8%A8%C0%FB',
            'http://www.calaw.cn/more.asp?channel=%CF%DC%B7%A8%D1%D0%BE%BF&type1=%CF%DC%B7%A8%D4%CB%D0%D0%BB%FA%D6%C6',
            'http://www.calaw.cn/more.asp?channel=%CF%DC%B7%A8%D1%D0%BE%BF&type1=%CB%BC%CF%EB%D1%A7%CB%B5',
            'http://www.calaw.cn/more.asp?channel=%D0%D0%D5%FE%B7%A8%D1%D0%BE%BF&type1=%D0%D0%D5%FE%B7%A8%BB%F9%B1%BE%C0%ED%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%D0%D0%D5%FE%B7%A8%D1%D0%BE%BF&type1=%D0%D0%D5%FE%B7%A8%D6%F7%CC%E5%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%D0%D0%D5%FE%B7%A8%D1%D0%BE%BF&type1=%D0%D0%D5%FE%D7%F7%D3%C3%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%D0%D0%D5%FE%B7%A8%D1%D0%BE%BF&type1=%D0%D0%D5%FE%B3%CC%D0%F2%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%D0%D0%D5%FE%B7%A8%D1%D0%BE%BF&type1=%D0%D0%D5%FE%BC%E0%B6%BD%BE%C8%BC%C3%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%D0%D0%D5%FE%B7%A8%D1%D0%BE%BF&type1=%B2%BF%C3%C5%D0%D0%D5%FE%B7%A8%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%D0%D0%D5%FE%B7%A8%D1%D0%BE%BF&type1=%CB%BC%CF%EB%D1%A7%CB%B5',
            'http://www.calaw.cn/more.asp?channel=%B7%A8%D5%FE%C6%C0%C2%DB&type1=%B9%AB%B7%A8%CA%B1%C6%C0',
            'http://www.calaw.cn/more.asp?channel=%B7%A8%D5%FE%C6%C0%C2%DB&type1=%B7%A8%D1%A7%C6%C0%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%B7%A8%D5%FE%C6%C0%C2%DB&type1=%CA%E9%CE%C4%BC%F6%C6%C0',
            'http://www.calaw.cn/more.asp?channel=%B7%A8%D5%FE%C6%C0%C2%DB&type1=%A1%B6%CF%DC%D5%FE%D3%EB%D0%D0%D5%FE%B7%A8%D6%CE%C6%C0%C2%DB%A1%B7',
            'http://www.calaw.cn/more.asp?channel=%B8%DB%B0%C4%CC%A8%B7%A8%D6%C6&type1=%D7%DB%BA%CF%D1%D0%BE%BF',
            'http://www.calaw.cn/more.asp?channel=%B8%DB%B0%C4%CC%A8%B7%A8%D6%C6&type1=%CC%A8%CD%E5%B7%A8%D6%C6',
            'http://www.calaw.cn/more.asp?channel=%B8%DB%B0%C4%CC%A8%B7%A8%D6%C6&type1=%CF%E3%B8%DB%B7%A8%D6%C6',
            'http://www.calaw.cn/more.asp?channel=%B8%DB%B0%C4%CC%A8%B7%A8%D6%C6&type1=%B0%C4%C3%C5%B7%A8%D6%C6',
            'http://www.calaw.cn/more.asp?channel=%C8%C8%B5%E3%BE%DB%BD%B9&type1=%C1%A2%B7%A8%B6%AF%CC%AC',
            'http://www.calaw.cn/more.asp?channel=%C8%C8%B5%E3%BE%DB%BD%B9&type1=%B9%FA%C4%DA%C8%C8%B5%E3',
            'http://www.calaw.cn/more.asp?channel=%C8%C8%B5%E3%BE%DB%BD%B9&type1=%B9%FA%CD%E2%B6%AF%CC%AC',
            'http://www.calaw.cn/more.asp?channel=%D1%A7%CA%F5%D7%CA%D1%B6&type1=%B9%AB%B7%A8%D0%C2%C2%DB',
            'http://www.calaw.cn/more.asp?channel=%D1%A7%CA%F5%D7%CA%D1%B6&type1=%D1%A7%CA%F5%D0%C5%CF%A2'
            ]
#数据库
client = pymongo.MongoClient('localhost',27017)
xianzhi = client['xianzhi']
item_url = xianzhi['item_url']


def get_url (url_list):
    for url in url_list:
        # print(url)
        # 提取构建url的字段（已编码）
        channel = re.findall(r'channel=(.+)&',url)[0]  #'%CF%DC%B7%A8%D1%D0%BE%BF'
        type1 = re.findall(r'type1=(.+)$',url)[0]    #'%CF%DC%B7%A8%BB%F9%B1%BE%C0%ED%C2%DB'
        # print(channel,type1)
        #爬网站第一页，获取页数信息
        wb_data = requests.get(url)
        encondings = requests.utils.get_encodings_from_content(wb_data.text)#解决中文乱码，该网站不是'utf-8' 编码，而是gb2312。
        encode_content = wb_data.content.decode(encondings[0], 'ignore')
        # print(encondings,encode_content)
        soup = BeautifulSoup(encode_content,'lxml')
        page_numbers = int(soup.select('table.table table table font:nth-of-type(3)')[0].text ) #当前列表页的页数
        channel_page = soup.select('table.table  td.newsbg a')[1].text  #用来存库（中文）
        type1_page = soup.select('table.table  td.newsbg a')[2].text
        print('#'*3,'总页数','#'*3, page_numbers,'##channel##',channel_page,'##type1##',type1_page)
        #爬取每一页
        for i in range(1,page_numbers + 1):  # 共page_numbers次
            time.sleep(2)
            print('第{}页'.format(i))
            url_page = 'http://www.calaw.cn/more.asp?' + \
                  'page={}&channel={}&type1={}'.format(i,channel,type1)
            print('#'*3,'url_page','#'*3,url_page)
            wb_data = requests.get(url_page)
            soup = BeautifulSoup(wb_data.content.decode(encondings[0], 'ignore'),'lxml')
            # print(soup)
            titles = soup.select('table.table  table  table:nth-of-type(2) a[title]')   #['title']
            url_items = soup.select('table.table  table  table:nth-of-type(2) a[title]')    #['href']
            for title,url_item in zip(titles,url_items):
                # print(channel_page)
                # print(type1_page)
                # print('#' * 3, 'title', '#' * 3, title['title'])
                # print('#' * 3, 'url', '#' * 3, 'http://www.calaw.cn' + url_item['href'])
                item_url.insert_one({
                        'channel_page': channel_page,
                        'type1_page': type1_page,
                        'title': title['title'],
                        'url': 'http://www.calaw.cn' + url_item['href'],
                        'page': i
                     })
# get_url(url_list)
