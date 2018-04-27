__author__ = 'wyj'
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
'''
功能：绘制ROC曲线
'''
# 导入数据
iris = datasets.load_iris()
X = iris.data#属性值
y = iris.target#标签值

# 二值化
y = label_binarize(y, classes=[0, 1, 2])#用几位值代替（100,010,001）
n_classes = y.shape[1]#3类,shape0是行数，shape1是列数

# 添加噪音使数据变复杂，将150*4的数据变为150*804的数据
random_state = np.random.RandomState(0)#伪随机数产生的种子
n_samples, n_features = X.shape
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]#扩充为(150L,804L),符合标准正态分布（0,1）

# 切分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5,random_state=0)

# 预测
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,random_state=random_state))
y_score = classifier.fit(X_train, y_train).decision_function(X_test)#75L,3L

# 得到每一个fpr[i]与tpr[i]
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])#21L,35L,33L,这个函数最后会返回一个阈值
    roc_auc[i] = auc(fpr[i], tpr[i])#曲线下的面积

# 最后将数据合为一维
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())#将多维数组降为一维
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])#95L,95L

##############################################################################
# 绘制第二分类的roc
plt.figure()
lw = 2#线宽
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')#参考线
plt.xlim([0.0, 1.0])#x轴刻度范围
plt.ylim([0.0, 1.05])#y轴刻度范围
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()


##############################################################################
# 多类问题的ROC曲线
#计算平均宏观ROC曲线和ROC面积
# 首先收集所有假正
all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))#重组，由大到小无重复排序
# 然后在这些点上插值所有ROC曲线。
mean_tpr = np.zeros_like(all_fpr)#跟all_fpr一样大的用0填充的数组
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])#插值

# 计算平均值与AUC面积
mean_tpr /= n_classes

fpr["macro"] = all_fpr
tpr["macro"] = mean_tpr
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
# 绘制所有的ROC曲线
plt.figure()
plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["micro"]),
         color='deeppink', linestyle=':', linewidth=4)

plt.plot(fpr["macro"], tpr["macro"],
         label='macro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["macro"]),
         color='navy', linestyle=':', linewidth=4)

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()