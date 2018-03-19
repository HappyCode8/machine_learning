__author__ = 'wyj'
# -*- coding:UTF-8 -*-
from math import log
import operator

'''
功能：创建数据集
输入：无
输出：数据集、属性名称集
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
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:#建立类标字典
        currentLabel = featVec[-1]#得到最后一列值
        if currentLabel not in labelCounts.keys():
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
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)   #计算信息熵
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #迭代计算所有属性集
        featList = [example[i] for example in dataSet]#得到所有第i列的值，存于example[i]
        uniqueVals = set(featList)       #得到去重以后i列的属性值
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        print infoGain;
        if (infoGain > bestInfoGain):       #计算到目前为止最好的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature                      #返回最好信息增益所在列值

'''
功能：求出现次数最多的分类名称
输入：分类名称的列表
输出：出现次数最多的分类名称
'''
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

'''
功能：建树
输入：数据集、类标
输出：树
'''
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree

if __name__ == "__main__":
    myData,labels=createDataSet();
    print myData,labels;
    # print calcShannonEnt(myData);
    # print splitDataSet(myData,0,1)
    # print splitDataSet(myData,0,0)
    #print calcShannonEnt(myData);
    #print chooseBestFeatureToSplit(myData)
    # myTree=createTree(myData,labels);
    # print myTree
