__author__ = 'wyj'
#encoding=utf-8

import time
if __name__=="__main__":
    start=time.clock()
    sum=0
    for i in range(1,10000001):
      sum=sum+i
    print sum
    end=time.clock()
    print('Running time: %s Seconds'%(end-start))