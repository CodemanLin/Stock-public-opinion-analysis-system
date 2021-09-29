# -*- codeing =utf-8 -*-
# @Time :2021/6/17 12:28
# @Author :chen
# @File : 训练语料库.py
# @Software :PyCharm
from snownlp import sentiment

if __name__ == "__main__":
  # 重新训练模型
  sentiment.train('./neg.txt', './pos.txt')
  # 保存好新训练的模型
  sentiment.save('sentiment2.marshal')
