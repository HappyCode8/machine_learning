__author__ = 'wyj'
#encoding=utf-8
'''
说明：iris数据集包含150条鸢尾花记录，属性有4个， 类标1个，无缺失值。
      详细见https://goo.gl/U2Uwz2
data：4属性
feature_names:属性名
DESCR：作者信息等
target：150的类标，与data相对应,3类
'''
from sklearn import datasets

iris = datasets.load_iris()
print u"字典keys：",iris.keys()
print u"属性维度：",iris.data.shape
print u"属性样例：",iris.data[0]
print u"属性名：",iris.feature_names
print u"类标维度：",iris.target.shape
print u"类标名：",iris.target_names
print u"类标样例：",iris.target[0]
print u"DESCR：",iris.DESCR


# print u"images维度：",digits.images.shape
# print u"data维度：",digits.data.shape
# print u"images样例类型：",digits.images[1]
# print u"datas样例类型：",digits.data[1]
# print u"target：",digits.target_names
# print u"target维度：",digits.target_names.shape
# print u"DESCR：",digits.DESCR
# print u"target：",digits.target
# print u"target维度：",digits.target.shape
# print u"图像样例："
# plt.imshow(digits.images[0])
# plt.gray()
# plt.show()