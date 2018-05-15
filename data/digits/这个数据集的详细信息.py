__author__ = 'wyj'
#encoding=utf-8
'''
说明：digits数据集包含1797条手写记录，包含了数字0到9的记录，属性有64个，取值介于0-16之间
      类标1条，为数字0-9，共有10类。样例分布均匀，无缺失值。
      详细见http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits
      这里可能只加载了测试集，源文件还包含一个更大的训练集，更详细的描述源文件带有描述
digits数据集
images：包含一个1797*8*8的手写图片的属性
data：将8*8的图像转化为1*64的图像，是一个1797*64的数组
target_names：1*10的类标去重集合（0-9）
DESCR：作者信息等
target：1*1797的类标，与images或者data相对应
'''
from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()
print u"字典keys：",digits.keys()
print u"images维度：",digits.images.shape
print u"data维度：",digits.data.shape
print u"images样例类型：",digits.images[1]
print u"datas样例类型：",digits.data[1]
print u"target：",digits.target_names
print u"target维度：",digits.target_names.shape
print u"DESCR：",digits.DESCR
print u"target：",digits.target
print u"target维度：",digits.target.shape
print u"图像样例："
plt.imshow(digits.images[0])
plt.gray()
plt.show()