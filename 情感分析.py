# -*- codeing =utf-8 -*-
# @Time :2021/6/14 0:12
# @Author :chen
# @File : tongji.py
# @Software :PyCharm
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import matplotlib.pyplot as plt
gupiao=['300001','600016','600036','601919']

l1=[]
l2=[]
def get_sentiment_cn(text):
    s = SnowNLP(text)
    return s.sentiments
for gu in gupiao:
    df=pd.read_csv(gu+'.csv')
    df = df[~df['标题'].str.contains('？')]
    df = df[~df['标题'].str.contains('吗')]
    df = df[~df['标题'].str.contains('怎么')]
    df = df[~df['标题'].str.contains('哪里')]
    s1 = SnowNLP(df['标题'])
    df['得分']=df.标题.apply(get_sentiment_cn)
    a=df['得分'].mean()
    b=len(df[df['得分']>0.5])/len(df)
    l1.append(a)
    l2.append(b)
    print(a,b)

fig=plt.figure()
ax1=fig.add_subplot(211)
ax1.barh(gupiao,l1)
ax2=fig.add_subplot(212)
ax2.barh(gupiao,l2)
plt.show()
print(l1)
print(l2)