'''
@中国宪政网 词频分析
@liangkeng
@2019.3.3
1.通过爬虫获取所有文章url
2.将所有文章内容存入mongodb
3.词频分析
'''
from find_url_list import get_url
from find_url_list import url_list
from find_article_info import find_article_info
import jieba
import jieba.analyse
from wordcloud import WordCloud
import cv2
import numpy
from PIL import Image

text_dict = {'宪法': 1.0, '国家': 0.6111562133388255, '法律': 0.48839287853024893, '社会': 0.34720818972092204, '权利': 0.30283269389292944, '规定': 0.281912804697708, '制度': 0.257116655263658, '政治': 0.253417575848865, '权力': 0.24668974244322, '地方': 0.23227321275340765, '问题': 0.2232733143813417, '中国': 0.21325519695246134, '政府': 0.20499681705038406, '公民': 0.18645049609830272, '作为': 0.18380671486530042, '进行': 0.17099559550309562, '人民': 0.16147389023686992, '具有': 0.15675121102804715, '规范': 0.15669639061870236, '没有': 0.15505026908989322, '原则': 0.15312488084097314, '发展': 0.15250660530175417, '基本权利': 0.1499209822655072, '行政': 0.14404572333685717, '认为': 0.13811703046842994, '民主': 0.1365426451356243, '基本': 0.13553722003759144, '保护': 0.13413966996918902, '解释': 0.13059905961170193, '理论': 0.12852318043643265, '保障': 0.12530681499314317, '关系': 0.12316766107852085, '宪政': 0.11914434396993412, '司法': 0.11748388422453267, '法院': 0.11720116048457985, '存在': 0.11597029622503366, '义务': 0.11249318244053179, '机关': 0.1121588875623014, '需要': 0.11191037426643934, '经济': 0.11117280433132011, '行为': 0.10896333048235801, '人权': 0.10467277440367388, '可能': 0.1039391012701907, '个人': 0.1038766019762396, '要求': 0.10366459047547925, '价值': 0.1025873114742807, '美国': 0.10187032022351657, '成为': 0.10111929748600172, '审查': 0.10034883538514153, '代表': 0.09924392184808649}
#要定义在main前面
def word_frequency_analysis():
    file = open('wb_text2.txt', 'r',encoding="utf-8")
    text = file.read()
    for x, w in jieba.analyse.textrank(text,topK=50, withWeight=True):
        text_dict.update({x:w})
        # print('%s %s' % (x, w))
    print('###########词频##########',text_dict)

def word_cloud(text_dict):
    # color_mask = cv2.imread('tiananmen.jpg')
    # 读入背景图片
    color_mask = numpy.array(Image.open('tiananmen.jpg'))
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path=" C:\Windows\Fonts\STXINWEI.TTF",
        # 设置背景色
        background_color='white',
        # 词云形状
        mask = color_mask,
        # 允许最大词汇
        max_words=50,
        # 最大号字体
        max_font_size=40
    )
    wCloud = cloud.generate_from_frequencies(text_dict)
    wCloud.to_file('cloud_result.jpg')


if __name__ == '__main__':
    #依次运行1.2.3，并将3的结果给4
    # get_url(url_list)   #1.得到文章url
    #
    #find_article_info()   #2.爬取文章内容

    # word_frequency_analysis()  #3.词频分析

    word_cloud(text_dict)            #4词云

    print(1)


