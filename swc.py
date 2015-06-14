__author__ = 'Su Lei'

import numpy as np

swcType = np.dtype({
    'names': ['serial', 'nodeTye', 'x', 'y', 'z', 'r', 'parentSerial'],
    'formats': [np.int, np.int, 'f', 'f', 'f', 'f', 'i']
}, align=True)


def readSwc(filename):
    f = open(filename)
    swcNum = []
    for eachLine in f:
        tmpStr = eachLine.strip().split(' ')
        tmpNum = []
        for i in xrange(len(tmpStr)):
            if i is 0 or i is 1 or i is 6:
                tmpNum.append(int(tmpStr[i]))
            else:
                tmpNum.append(float(tmpStr[i]))
        swcNum.append(tmpNum)
    return swcNum

def readSwcNp(filename):
    f = open(filename)
    swc = []
    for eachLine in f:
        tmpStr = eachLine.strip().split(' ')
        tmpNum = []
        for i in xrange(len(tmpStr)):
            if i is 0 or i is 1 or i is 6:
                tmpNum.append(int(tmpStr[i]))
            else:
                tmpNum.append(float(tmpStr[i]))
        swc.append(tmpNum)
    swcNp = np.array([], dtype=swcType)
    for i in xrange(len(swc)):
        tmpSwcNp = np.array(tuple(swc[i]), dtype=swcType)
        # print tmpSwcNp
        swcNp = np.append(tmpSwcNp, swcNp)
    return swcNp

def cmp1(x, y):
    if x[4] > y[4]:
        return 1
    else:
        return -1

def sortSwc(s):
    s.sort(cmp1)

outSwcNum = readSwc('test1.swc')
print outSwcNum
fo = open('test2.swc', 'w')
sortSwc(outSwcNum)
for i in xrange(len(outSwcNum)):
    outSwcNum[i].append('\n')
    fo.write(' '.join([str(x) for x in outSwcNum[i]]))

fo.close()
print outSwcNum




