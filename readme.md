# 对中国宪治网(<http://www.calaw.cn>)爬虫

## 总体介绍
* BeautifulSoup爬虫
* jieba词频分析
* wordcloud词云展示

## 文件详情
1. main.py
2. find_url_list.py 获取文章url
3. find_article_info.py 爬虫函数
4. url_counters.py 检测已爬虫文章数量
5. wb_text.txt  爬虫原始文章
6. tiananmen.jpg  词云原始图样
7. cloud_result.jpg 词云结果

## 执行
按照main中1.2.3.4顺序执行

## todo
* [ ] 爬虫原始文章的存储格式：感觉txt不太好
* [ ] 多线程爬虫:Pool
* [ ] 反爬措施：可参照<https://www.cnblogs.com/zhisy/p/6897604.html>
* [ ] 自定义词库： 删除不需要的词语，还有目前结果只有两字词语。

