__author__ = 'wyj'
#encoding=utf-8
'''
说明：diabetes数据集包含442条糖尿病记录，属性有10个， 类标1条，无缺失值，这个数据值经过中心化
      和标准化，还有一些其它处理。
data：1*13的属性
feature_names:属性名
DESCR：作者信息等
target：1*442的类标，与data相对应
'''
from sklearn import datasets

diabetes = datasets.load_diabetes()
print u"字典keys：",diabetes.keys()
print u"data维度",diabetes.data.shape
print u"data样例类型",diabetes.data[0]
print u"特征名：",diabetes.feature_names
print u"target维度：",diabetes.target.shape
print u"target样例：",diabetes.target[0]
print u"DESCR:",diabetes.DESCR

