#统计爬了多少个url地址

import time
from find_url_list import item_url

while True:
    print('已爬取{}个url'.format(item_url.find().count()))
    time.sleep(5)