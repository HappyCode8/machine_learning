__author__ = 'wyj'
# coding=utf-8

from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
import numpy as np

'''
功能：以概率分类标签
输入：从第二个参数起依次为训练集属性，训练集标签，测试集属性
输出：分为指定类的概率
'''

#第一个参数为k
def myKnn(k,X_train, y_train,X_test):
  classifier = KNeighborsClassifier(k)
  res = classifier.fit(X_train, y_train).predict_proba(X_test)
  y_score= [x[1] for x in res]
  return y_score

#第一个参数为核
def mySvm(kernel,X_train, y_train,X_test):
  classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,random_state=0))
  y_score = classifier.fit(X_train, y_train).decision_function(X_test)
  return y_score

#第一个参数为决策树的层数
def myDecisionTree(maxd,X_train, y_train,X_test):
  classifier = DecisionTreeClassifier(max_depth=maxd)
  res = classifier.fit(X_train, y_train).predict_proba(X_test)
  y_score= [x[1] for x in res]
  return y_score