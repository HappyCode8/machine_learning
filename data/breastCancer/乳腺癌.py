__author__ = 'wyj'
#encoding=utf-8
'''
说明：breast_cancer数据集包含569条乳腺癌记录，属性有30个， 类标1条，无缺失值。
      详细见https://goo.gl/U2Uwz2
data：30个属性
feature_names:属性名
DESCR：作者信息等
target：569的类标，与data相对应,0，1区分良性恶性
'''
from sklearn import datasets

cancer = datasets.load_breast_cancer()
print u"字典keys：",cancer.keys()
print u"data属性名：",cancer.feature_names
print u"data维度：",cancer.data.shape
print u"data样例类型：",cancer.data[0]
print u"类标名：",cancer.target_names
print u"target维度：",cancer.target.shape
print u"target样例类型：",cancer.target[0]
print u"DESCR：",cancer.DESCR

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