__author__ = 'wyj'
# coding=utf-8
import random
from sets import Set

'''
功能：从指定文件抽取若干行出来并写入到一个新文件,新文件不存在将新建，存在将重写
输入：源文件，输出文件，抽取行数
输出：有指定抽取行数的文件
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
    get_file("./data/test/txt1","./data/test/txt2",7)

