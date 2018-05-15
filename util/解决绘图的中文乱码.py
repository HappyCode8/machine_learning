__author__ = 'wyj'
#encoding=utf-8
from sklearn import datasets
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
plt.rcParams['font.sans-serif']=['SimHei']; #用来正常显示中文标签
plt.title(u'数字分布状况')
plt.xlabel(u'数字')
plt.ylabel(u'频率')
plt.show()