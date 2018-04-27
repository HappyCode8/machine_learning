__author__ = 'wyj'
# coding=utf-8

from dataWeHope import *
from myClassifier import *
from rocDraw import *

if __name__ == "__main__":
    X_train, X_test, y_train, y_test=data("test.txt",dataDimission=8,testRation=0.99)
    knn_score=myKnn(5,X_train,y_train,X_test)
    svm_score=mySvm('RBF',X_train,y_train,X_test)
    myDecTree_score=myDecisionTree(5,X_train,y_train,X_test)
    drawRoc(y_test, knn_score,'red','knn')
    drawRoc(y_test, svm_score,'yellow','SVM')
    drawRoc(y_test, myDecTree_score,'blue','decesionTree')