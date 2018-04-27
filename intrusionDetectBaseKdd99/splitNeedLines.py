__author__ = 'wyj'
# coding=utf-8
import random
from sets import Set

'''
功能：从指定文件随机无重复抽取若干行数据
输入：输入文件，输出文件，行数
输出：包含指定行数的文件
'''

def get_file(srcFileNmae, dstFileName, linenum):
     result = []
     srcfd = open(srcFileNmae,'r')
     dstfd = open(dstFileName,'wb')
     srclines = srcfd.readlines()
     srclen = len(srclines)
     while len(Set(result)) < int(linenum):
         s = random.randint(0,srclen-1)
         result.append(srclines[s])
     for content in Set(result):
         dstfd.write(content)
     srcfd.close()
     dstfd.close()

if __name__ == "__main__":
    get_file("kddcup.data_10_percent_corrected","newfile",10000)