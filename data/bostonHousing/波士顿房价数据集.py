__author__ = 'wyj'
#encoding=utf-8
'''
说明：boston数据集包含506条房价记录，属性有13个， 类标1条，无缺失值。
      详细见https://archive.ics.uci.edu/ml/machine-learning-databases/housing/
data：1*13的属性
feature_names:属性名
DESCR：作者信息等
target：1*506的类标，与data相对应
'''
from sklearn import datasets
import matplotlib.pyplot as plt

boston = datasets.load_boston()
print u"字典keys：",boston.keys()
print u"data维度",boston.data.shape
print u"data样例类型",boston.data[0]
print u"特征名：",boston.feature_names
print u"DESCR:",boston.DESCR
print u"target维度：",boston.target.shape
print u"target样例：",boston.target[0]
