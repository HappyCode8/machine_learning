__author__ = 'wyj'
# coding=utf-8

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

'''
功能：绘制roc曲线
输入：实际标签，标签判定概率，标题，yanse
输出：roc曲线
'''
def drawRoc(y_test, y_score,color,title):
    fpr, tpr, _ =roc_curve(y_test, y_score)
    plt.figure()
    plt.plot(fpr, tpr, color=color,
             lw=2, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')#参考线
    plt.xlim([0.0, 1.0])#x轴刻度范围
    plt.ylim([0.0, 1.05])#y轴刻度范围
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.show()