__author__ = 'wyj'
# coding=utf-8

import numpy as np
from sklearn.model_selection import train_test_split

'''
功能：读取文件为测试集与训练集
输入：filename：文件名（文件以“，”分割，文件每行除最后一列做label，其余都坐attribute），
输出：分离后的测试集与训练集
'''
def data(filename):
   matrix = np.loadtxt(open(filename, "rb"), delimiter=",", skiprows=0)
   x = matrix[:,0:-1]
   y = matrix[:,-1]
   X_train, X_test, y_train, y_test = train_test_split(x, y ,random_state=0)
   return X_train, X_test, y_train, y_test

if __name__ == "__main__":
   X_train, X_test, y_train, y_test=data('./data/test/txt1')
   print X_train,y_train,X_test,y_test