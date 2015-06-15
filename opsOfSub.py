__author__ = 'Su Lei'

import cv2 as cv
import numpy as np
import math

def createRollingBall(r):
    if r <= 10:
        shrinkFactor = 1
        arcTrimPer  = 24
    elif r <= 30:
        shrinkFactor = 2
        arcTrimPer = 24
    elif r <= 100:
        shrinkFactor = 4
        arcTrimPer = 32
    else:
        shrinkFactor = 8
        arcTrimPer = 40
    smallballradius = r / float(shrinkFactor)
    if smallballradius < 1:
        smallballradius = 1
    rsquare = smallballradius * smallballradius
    xtrim = math.floor(arcTrimPer * smallballradius / 100.0)
    halfWidth = math.floor(smallballradius - xtrim)
    width = halfWidth * 2 + 1
    data = np.zeros(width, width)
    for i in xrange(width):
        for j in xrange(width):
            xval = j - (halfWidth + 1)
            yval = i - (halfWidth + 1)
            temp = rsquare - xval * xval - yval * yval
            temp = np.float32(temp)
            if temp > 0:
                data[i, j] = math.sqrt(temp)
            else:
                data[i, j] = 0
    return data, shrinkFactor
    pass

def filter3(inImage, l, pixel0, inc, t):
    shiftBy = 0
    i = 0
    p = pixel0
    v3 = inImage.take(pixel0)
    v2 = v3
    while i < l:
        v1 = v2
        v2 = v3
        if i < l - 1:
            v3 = inImage.take(p + inc)
        if t ==  'MAXIMUM':
            if v1 > v3:
                max = v1
            else:
                max = v3
            if v2 > max:
                max = v2
            shiftBy += max - v2
            inImage.put(p, max)
        else:
            inImage.put(p, (v1 + v2 + v3) * 1 / 3)
        p += inc
        i += 1



    pass

def filter3x3(inImage, t):
    height, width = inImage.shape
    shiftBy = 0
    for y in xrange(height):
        inImage, t = filter3(inImage, width, y * width, 1, t)
        shiftBy += t
    for x in xrange(width):
        inImage, t = filter3(inImage, height, x, height, t)
        shiftBy += t
    temp = shiftBy / width / height
    pass

def getMinMax(inImage):
    pass

def shrinkImage(inImage, f):
    pass

def rollBall(b, inImage):
    pass

def enlargeImage(inImage, h, w, f):
    pass
