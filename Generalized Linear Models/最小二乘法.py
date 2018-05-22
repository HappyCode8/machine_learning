__author__ = 'wyj'
#coding=utf-8
'''
线性预测：reg.coef_是系数组，reg.intercept_是常量
'''
from sklearn import linear_model

reg = linear_model.LinearRegression()        #使用线性回归
reg.fit ([[0, 0], [1, 1], [2, 2]], [4, 5, 6])#属性与类标
print reg.coef_,reg.intercept_              #预测值

'''
一个线性预测实例
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()#载入糖尿病数据集

diabetes_X = diabetes.data[:, np.newaxis, 2]#只使用第二列，如果不用np.newaxis输出的是一个行向量，这里需要列向量
#[1,2,3,4]变为[[1],[2],[3],[4]]

# 切分训练集与测试集的属性
diabetes_X_train = diabetes_X[:-20]#除去最后20行的数据作为训练
diabetes_X_test = diabetes_X[-20:]#最后20行作为测试

# 切分训练集与测试集的类标
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# 线性回归
regr = linear_model.LinearRegression()

# 训练集训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

#预测测试集的结果
diabetes_y_pred = regr.predict(diabetes_X_test)

#系数
print u"系数：",regr.coef_
print u"常数：",regr.intercept_
#均方误差
print(u"均方误差: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# 解释方差评价，又叫R^2评价，这个评价与均值相比，看能好多少，1表示完美预测，0与均值代替的相同效果，小于0表示还不如不预测，直接使用均值代替就好了
# 计算方法是1-（实际值-预测值）的方差/实际值的方差
print(u'方差得分: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# 画图，带类标的散点图，预测直线
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()