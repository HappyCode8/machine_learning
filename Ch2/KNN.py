__author__ = 'wyj'
# -*- coding: UTF-8 -*-

from numpy import *
import operator
import matplotlib.pyplot as plt

def creatDataSet():#创建数据
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

def file2matrix(filename):
    fr=open(filename);
    numberOfLines = len(fr.readlines())         #得到文件行数
    returnMat = zeros((numberOfLines,3))        #用0填充这个矩阵，行数*3列
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()#移除字符串头尾指定的字符，默认移除空格
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]#选取前三个元素存储到矩阵中
        classLabelVector.append(int(listFromLine[-1]))#python可以用-1索引取最后一列
        index += 1
    return returnMat,classLabelVector

if __name__=="__main__":
    group,label=creatDataSet();
    # print group;
    # print label;
    # print classify0([1, 2], group, label, 3);
    datingDataMat, datingLabels=file2matrix("datingTestSet2.txt");
    # print  datingDataMat;#属性
    # print datingLabels[0:20];#类标
    plt.rcParams['font.sans-serif']=['SimHei']; #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False; #用来正常显示负号
    f1 = plt.figure();
    ax1 = f1.add_subplot(111);#一行一列一个
    ax1.set_title(u'示意图');#标题
    plt.xlabel(u"玩视频游戏所耗时间百分比");#x坐标
    plt.ylabel(u"每周消费的冰淇淋公升数"); #y坐标
    # for i in range(len(datingLabels)):
    #     if datingLabels[i] == 1:
    #         p1=ax1.scatter(datingDataMat[i:i+1, 1], datingDataMat[i:i+1 ,2],color = 'red')
    #     if datingLabels[i] == 2:
    #         p2=ax1.scatter(datingDataMat[i:i+1, 1], datingDataMat[i:i+1, 2], color='green')
    #     if datingLabels[i] == 3:
    #         p3=ax1.scatter(datingDataMat[i:i+1, 1], datingDataMat[i:i+1, 2], color='black')
    # plt.legend([p1, p2,p3], [u'不喜欢', u'魅力一般', u'极具魅力'], loc='lower right', scatterpoints=1)
    ax1.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels));#分别是x,y，尺

    f2 = plt.figure();
    ax2 = f2.add_subplot(111);#一行一列一个
    ax2.set_title(u'示意图2');#标题
    plt.xlabel(u"每年获取的飞行常客里程数");#x坐标
    plt.ylabel(u"玩视频游戏所耗时间百分比"); #y坐标
    for i in range(len(datingLabels)):
        if datingLabels[i] ==1:
            p1=ax2.scatter(datingDataMat[i:i+1, 0], datingDataMat[i:i+1 ,1],color = 'red')
        if datingLabels[i] == 2:
            p2=ax2.scatter(datingDataMat[i:i+1, 0], datingDataMat[i:i+1, 1], color='green')
        if datingLabels[i] == 3:
            p3=ax2.scatter(datingDataMat[i:i+1, 0], datingDataMat[i:i+1, 1], color='black')
    plt.legend([p1,p2,p3], [u'不喜欢', u'魅力一般', u'极具魅力'], loc='upper left', scatterpoints=1)
    # ax2.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels));#分别是x,y，尺寸，色彩
    plt.show();



