# -*- codeing =utf-8 -*-
# @Time :2021/6/16 11:19
# @Author :chen
# @File : 词频分析.py
# @Software :PyCharm
import jieba
txt = open("300001(2).txt",encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(30):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))