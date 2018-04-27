__author__ = 'wyj'
# coding=utf-8

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.decomposition import PCA

'''
输入：filename：文件名（文件以“，”分割，文件每行除最后一列做label，其余都坐attribute），
      dataDimission：数据降到多少维
      testRation:交叉验证时抽取多大比例做测试
'''
def data(filename,dataDimission,testRation):
   matrix = np.loadtxt(open(filename, "rb"), delimiter=",", skiprows=0)
   x = matrix[:,0:-1]
   y = matrix[:,-1]
   x= preprocessing.scale(x)
   pca=PCA(n_components=dataDimission)
   x=pca.fit_transform(x)
   X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=testRation,random_state=0)
   return X_train, X_test, y_train, y_test

if __name__ == "__main__":
   data('test.txt',5,0.9)