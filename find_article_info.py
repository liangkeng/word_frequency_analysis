#将每篇文章内容存在txt

from bs4 import BeautifulSoup
import requests
from find_url_list import item_url
import pymongo
import time

def  find_article_info():
    item_urls = item_url.find()
    num=0
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'http://www.calaw.cn/'
    }
    for url in item_urls:
        try:
            time.sleep(2)
            wb_data = requests.get(url['url'],headers=headers,timeout=4)
            soup = BeautifulSoup(wb_data.content.decode(requests.utils.
                                get_encodings_from_content(wb_data.text)[0], 'ignore'),'lxml')
            context = soup.select('table.center table#__5 tr:nth-of-type(1)')[0].text.replace('\r','').replace('\n','').replace('\t','').replace(' ','')
            # 有点想删除英文
            # print(context)
            wb_text = open('wb_text2.txt', 'a+', encoding="utf-8") #window默认'gbk'编码
            wb_text.write(context)
            num += 1
            print('已经爬取{}篇文章'.format(num))
        except requests.exceptions:
            print('超时，暂停10s再爬')
            time.sleep(10)

# find_article_info()
