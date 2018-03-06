__author__ = 'wyj'

from numpy import *
import operator

def creatDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]);
    label=['A','A','B','B'];
    return group,label;


if __name__=="__main__":
    group,label=creatDataSet();
    print group;
    print label;