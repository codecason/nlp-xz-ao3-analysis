import os
import logging
from collections import Counter
import jieba
import jieba.analyse
import re
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

jieba.load_userdict(os.path.join(os.path.dirname('.'), 'static/dict.txt.small.txt'))
jieba.analyse.set_stop_words('./stopwords.txt')


class CountDown():
    cnt = 0
    def print(self, text):
        if self.cnt < 10:
            self.cnt += 1
            print(text)


def load_file():
    all_text = []
    res = ''
    cprint = CountDown()
    logging.info('start to load file...')
    with open('xz-QA-data-1.csv', 'r', encoding='utf-8') as f:
        all_text = f.readlines()
    all_cnt = 0
    for text in all_text[1:]:
        text_list = text.split(',')
        if len(text_list) > 12:
            all_cnt += 1
            res += text_list[12]
        # break
        # cprint.print(text_list)
    logging.info('...finish loading file')
    return res


def remind_load_file():
    """
    追忆似水年华
    """
    all_text = []
    res = ''
    cprint = CountDown()
    logging.info('start to load file...')
    with open('追忆似水年华.txt', 'r', encoding='utf-8') as f:
        all_text = f.readlines()
    res = ' '.join(all_text)
    print(f'all_cnt = {len(res)}')
    logging.info('...finish loading file')
    return res


def word_segment(text):
    jieba_word = jieba.cut(text, cut_all=False)
    new_list = []
    for word in jieba_word:
        if not re.match(r'[a-z0-9]+', word):
            new_list.append(word)
    new_list = ' '.join(new_list)
    return new_list


def generate_wordcloud(text):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    d = os.path.dirname('.')
    # alice_mask = np.array(Image.open(path.join(d, "images/alice_mask.png")))
    font_path = os.path.join(d, "static/font/msyh.ttf")
    with open('./stopwords.txt', 'r', encoding='utf-8') as f:
        res = f.readlines()
    res = [r.strip() for r in res]
    stopwords = set(STOPWORDS) | set(res)
    print('stop words = ', stopwords)
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=2000, # 词云显示的最大词数
        #    mask=alice_mask, # 设置背景图片
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
         )

    # 生成词云
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(os.path.join(d, "static/images/alice.png"))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()


if __name__ == '__main__':
    # text = remind_load_file()
    text = load_file()
    word_list = word_segment(text)
    generate_wordcloud(word_list)
