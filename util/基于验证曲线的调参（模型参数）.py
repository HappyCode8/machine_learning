__author__ = 'wyj'
#encoding=utf-8

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

digits = load_digits()#数字集
X, y = digits.data, digits.target
print X.shape,y.shape
param_range = np.logspace(-6, -1, 5)#创建10^-6到10^-1范围的5个等比数列

train_scores, test_scores = validation_curve(
    SVC(), X, y, param_name="gamma", param_range=param_range,
    cv=10, scoring="accuracy", n_jobs=1)#十折交叉验证调gamma值
train_scores_mean = np.mean(train_scores, axis=1)#对各行求均值
train_scores_std = np.std(train_scores, axis=1)#对各行求标准差
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
print train_scores,test_scores
print train_scores_mean,train_scores_std
print test_scores_mean,test_scores_std

plt.title("Validation Curve with SVM")
plt.xlabel("$\gamma$")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
lw = 2
plt.semilogx(param_range, train_scores_mean, label="Training score",
             color="darkorange", lw=lw)#将X轴对数化，对数化将坐标缩放到一个维度上
plt.fill_between(param_range, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.2,
                 color="darkorange", lw=lw)#曲线部分填充，在得分的一个标准差内填充
plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
             color="navy", lw=lw)
plt.fill_between(param_range, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.2,
                 color="navy", lw=lw)
plt.legend(loc="best")
plt.show()