__author__ = 'Su Lei'

import numpy as np
import math

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

def trimSwc(s):
    while s[len(s) - 1][6] is -1:
        s.pop(len(s) - 1)
        if len(s) is 0:
            break
    pass

def convert2line(s):
    sn = len(s)
    if sn == 0:
        exit()
    lines = []
    i = 0
    for col in s:
        print col
        if col[6] != col[0] - 1:
            if i is not 0:
                lines.append(tmp)
            tmp = []
        print tmp
        tmp.append(col)
        if i == sn - 1:
            lines.append(tmp)
        i += 1
    return lines

def printLineHeadAndTail(ls):
    for i in xrange(len(ls)):
        lineLength = len(ls[i])
        head = (ls[i][0][0], ls[i][0][6])
        tail = (ls[i][lineLength - 1][0], ls[i][lineLength - 1][6])
    print head, tail

def distanceOf2p(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def insertLines(ls, minDistance):
    coordinatesOfLines = []
    for i in xrange(len(ls)):
        line = ls[i]
        coordinatesOfLine = []
        for j in xrange(len(line) - 1):
            cp = line[j]
            np = line[j + 1]
            d = distanceOf2p((cp[2], cp[3], cp[4]), (np[2], np[3], np[4]))
            if d <= minDistance:
                coordinatesOfLine.append([cp[2], cp[3], cp[4]])
            else:
                coordinatesOfLine.append([cp[2], cp[3], cp[4]])
                insertedNumOfP = int(math.ceil(d / minDistance))
                slopeOfX = (np[2] - cp[2]) / (insertedNumOfP + 1)
                slopeOfY = (np[3] - cp[3]) / (insertedNumOfP + 1)
                slopeOfZ = (np[4] - cp[4]) / (insertedNumOfP + 1)
                for k in xrange(insertedNumOfP):
                    cx = cp[2] + slopeOfX * (k + 1)
                    cy = cp[3] + slopeOfY * (k + 1)
                    cz = cp[4] + slopeOfZ * (k + 1)
                    coordinatesOfLine.append([cx, cy, cz])
            if j == (len(line) - 2):
                coordinatesOfLine.append([np[2], np[3], np[4]])
        coordinatesOfLines.append(coordinatesOfLine)
    return coordinatesOfLines



outSwcNum = readSwc('test1.swc')
trimSwc(outSwcNum)
linesInSwc = convert2line(outSwcNum)
print insertLines(linesInSwc, 5)






# fo = open('test2.swc', 'w')
# # sortSwc(outSwcNum)
# for i in xrange(len(outSwcNum)):
#     outSwcNum[i].append('\n')
#     fo.write(' '.join([str(x) for x in outSwcNum[i]]))
#
# fo.close()




