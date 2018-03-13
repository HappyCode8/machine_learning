__author__ = 'wyj'
# -*- coding:UTF-8 -*-
from math import log
import operator

'''
功能：创建数据集
输入：无
输出：属性集、类标集
'''
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

'''
功能：计算信息熵
输入：数据集
输出：信息熵
'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)#数据长度
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]#得到最后一列值
        if currentLabel not in labelCounts.keys():#创建字典
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries#计算信息熵
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

'''
功能：计算划分
输入：数据集，划分数据集选择的特征（即第几列）、特征的返回值。
输出：划分以后符合特征返回值的字典
'''
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

'''
功能：选择最好的数据集划分方式
输入：数据集
输出：选择划分的特征
'''
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #最后一列
    baseEntropy = calcShannonEnt(dataSet)   #计算信息熵
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #迭代计算所有属性集
        featList = [example[i] for example in dataSet]#得到所有第i列的值，存于example[i]
        # print featList
        uniqueVals = set(featList)       #得到去重以后i列的属性值
        # print uniqueVals
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #计算到目前为止最好的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature                      #返回最好信息增益所在列值

'''
功能：
输入：
输出：
'''
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

if __name__ == "__main__":
    myData,labels=createDataSet();
    print myData;
    # print calcShannonEnt(myData);
    # print splitDataSet(myData,0,1)
    # print splitDataSet(myData,0,0)
    print chooseBestFeatureToSplit(myData)
