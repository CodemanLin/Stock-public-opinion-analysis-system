# -*- codeing =utf-8 -*-
# @Time :2021/6/13 19:31
# @Author :chen
# @File : test3.py
# @Software :PyCharm
import requests
import pandas as pd
from lxml import etree
import csv
import jieba

ab1=[]

#daimas=['300001','600016','600036','601919'] #定义爬取的股票
daimas=['002594']
for daima in daimas:

    for a in range(1,200):
        url = 'http://guba.eastmoney.com/list,'+daima+'_'+str(a)+'.html'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
        res = requests.get(url=url,headers=headers)
        res.encoding ='utf-8'
        tree = etree.HTML(res.text)
        li1 = tree.xpath('//*[@id="articlelistnew"]/div/span[1]/text()')
        li1.remove('阅读')
        li2 = tree.xpath('//*[@id="articlelistnew"]/div/span[2]/text()')
        li2.remove('评论')
        li3 = tree.xpath('//*[@id="articlelistnew"]/div/span[3]/a/text()')
        li4 = tree.xpath('//*[@id="articlelistnew"]/div/span[4]/a/font/text()')
        li5 = tree.xpath('//*[@id="articlelistnew"]/div/span[5]/text()')
        li5.remove('最后更新')

        for i in range(len(li1)):
                list1 = [li1[i],li2[i],li3[i],li4[i],li5[i]]
                ab1.append(list1)
    filename=daima+'.csv'
    print(filename)
    with open(filename, 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('阅读','评论','标题','作者','最后更新'))
        writer.writerows(ab1)

