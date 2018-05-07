__author__ = 'wyj'
# coding=utf-8
#调参，检查异常维度（注释部分）
from myClassifier import *
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from dataWeHope import *
from itertools import cycle

if __name__ == "__main__":
    # f = open("test.txt",'r')
    # i=0
    # for lines in f:
    #     line=lines.split(",")
    #     if(line.__len__()!=123):
    #         print i
    #     i+=1;

     train = np.loadtxt(open("train.txt", "rb"), delimiter=",", skiprows=0)
     X_trainOriginal = train[:,0:-1]
     y_train = train[:,-1]

     test = np.loadtxt(open("test.txt", "rb"), delimiter=",", skiprows=0)
     X_testOriginal = test[:,0:-1]
     y_test = test[:,-1]

     cs=[0,1,5,10,50,100,500,1000]
     colors = cycle(['cyan','yellow','red','green','black','brown','blue','deeppink'])
     linestyles=cycle([':','-.','-','--'])
     plt.figure()
     plt.xlim([0.0, 1.0])#x轴刻度范围
     plt.ylim([0.0, 1.05])#y轴刻度范围
     plt.xlabel('False Positive Rate')
     plt.ylabel('True Positive Rate')
     plt.title("different coef0")
     plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')#参考线
     for c,color,line in zip(cs,colors,linestyles):
         pca=PCA(n_components=3)
         X_train= preprocessing.scale(X_trainOriginal)# 将每一列特征标准化为标准正态分布
         X_train=pca.fit_transform(X_train)
         X_test=preprocessing.scale(X_testOriginal)
         X_test=pca.fit_transform(X_test)

         classifier = OneVsRestClassifier(svm.SVC(kernel='poly', probability=True,random_state=0,coef0=c))
         y_score = classifier.fit(X_train, y_train).decision_function(X_test)

         fpr, tpr, _ =roc_curve(y_test, y_score)
         roc_auc=auc(fpr,tpr)
         plt.plot(fpr, tpr, color=color,lw=2, linestyle=line,label='ROC curve of coef0:{0} (area = {1:0.2f})'
             ''.format(c, roc_auc))
     plt.legend(loc="lower right")
     plt.show()