__author__ = 'wyj'
# -*- coding: UTF-8 -*-

from numpy import *
from os import listdir
from knnLearn.KNN import classify0
'''
功能：将32*32的矩阵转换为1*1024的矩阵
输入：文件名
输出：1*1024矩阵
'''
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
'''
功能：对手写进行分类
输入：无
输出：分类结果、准确率等，内部输出，无返回值
'''
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #加载训练集
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #取得没有.txt的文件名
        classNumStr = int(fileStr.split('_')[0])#取得文件是哪个数字
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)#文件路径名
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))

if __name__=="__main__":
    handwritingClassTest()