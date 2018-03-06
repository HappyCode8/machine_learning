__author__ = 'wyj'
# -*- coding: UTF-8 -*-

from numpy import *
import operator

def creatDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]);
    label=['A','A','B','B'];
    return group,label;

def classify0(inX, dataSet, labels, k):#inX为输入向量，dataSet训练集，labels标签，k最近邻居的数目
    dataSetSize = dataSet.shape[0]     #得到训练集的行数，即知道有几个训练集
    diffMat = tile(inX, (dataSetSize,1)) - dataSet#将inX重复dataSetSize次，结果为4*1的，然后得到了目标与训练数据之间的差值
    sqDiffMat = diffMat**2#每个差值元素都平方
    sqDistances = sqDiffMat.sum(axis=1)#按行求和，当axis=0时按列求和
    distances = sqDistances**0.5#开根号
    sortedDistIndicies = distances.argsort()#升序排序
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)#按照第二个元素逆序排列
    return sortedClassCount[0][0]#返回频次最高的元素

if __name__=="__main__":
    group,label=creatDataSet();
    print group;
    print label;
    print classify0([0,0], group, label, 3);